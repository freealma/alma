import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.status import Status
from typing import List, Dict
from datetime import datetime

from .llm_client import llm_client
from .db import memory_db
from ..utils.config import config

console = Console()

class ChatSession:
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id
        self.conversation_history: List[Dict] = []
        self.console = Console()
    
    def get_relevant_memories(self, user_input: str) -> List:
        """Get relevant memories for the current input"""
        # Search for direct matches
        search_results = memory_db.search_memories(user_input, limit=3)
        
        # Get recent memories from this session
        session_memories = memory_db.get_recent_memories(
            limit=config.MEMORY_CONTEXT_SIZE,
            scope=self.session_id
        )
        
        # Get global memories
        global_memories = memory_db.get_recent_memories(
            limit=2,
            scope="global"
        )
        
        # Combine and deduplicate
        all_memories = []
        seen_keys = set()
        
        for mem in search_results + session_memories + global_memories:
            key = mem[0]
            if key not in seen_keys:
                all_memories.append(mem)
                seen_keys.add(key)
        
        return all_memories[:config.MEMORY_CONTEXT_SIZE]
    
    def add_to_memory(self, user_input: str, response: str):
        """Add conversation to memory"""
        # Create a memory key from the timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        memory_key = f"{self.session_id}_conversation_{timestamp}"
        
        # Store the exchange
        memory_value = f"User: {user_input}\nAlma: {response}"
        memory_db.add_memory(memory_key, memory_value, scope=self.session_id)
    
    def chat_loop(self):
        """Main chat loop"""
        self.console.print(Panel.fit(
            "[bold cyan]Alma[/bold cyan] - AI Assistant with Memory\n"
            "Type 'exit' or 'quit' to end the conversation.\n"
            "Type 'clear' to clear conversation history.",
            title="Welcome"
        ))
        
        while True:
            try:
                # Get user input
                user_input = self.console.input("[bold green]You:[/bold green] ").strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.lower() in ['exit', 'quit', 'q']:
                    self.console.print("[yellow]Goodbye![/yellow]")
                    break
                elif user_input.lower() == 'clear':
                    self.conversation_history.clear()
                    self.console.print("[yellow]Conversation history cleared.[/yellow]")
                    continue
                elif user_input.lower() == 'memory':
                    self.show_memory_status()
                    continue
                
                # Get relevant memories
                with Status("[cyan]Consulting memories...[/cyan]", console=self.console):
                    memories = self.get_relevant_memories(user_input)
                
                # Generate response
                with Status("[cyan]Thinking...[/cyan]", console=self.console):
                    response = llm_client.generate_response(
                        user_message=user_input,
                        memories=memories,
                        conversation_history=self.conversation_history
                    )
                
                # Display response
                self.console.print("\n[bold cyan]Alma:[/bold cyan]")
                self.console.print(Markdown(response["content"]))
                self.console.print()
                
                # Store in history
                self.conversation_history.append({
                    "role": "user",
                    "content": user_input,
                    "timestamp": datetime.now().isoformat()
                })
                
                self.conversation_history.append({
                    "role": "assistant",
                    "content": response["content"],
                    "timestamp": datetime.now().isoformat()
                })
                
                # Add to memory
                self.add_to_memory(user_input, response["content"])
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Type 'exit' to quit or continue chatting.[/yellow]")
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
    
    def show_memory_status(self):
        """Show current memory status"""
        memories = memory_db.get_recent_memories(limit=10)
        
        self.console.print(Panel.fit(
            f"[bold]Memory Status[/bold]\n\n"
            f"Total recent memories: {len(memories)}\n"
            f"Session: {self.session_id}\n",
            title="Memory"
        ))
        
        if memories:
            self.console.print("[bold]Recent Memories:[/bold]")
            for mem in memories[:5]:
                key, value, scope, timestamp = mem
                truncated_value = value[:50] + "..." if len(value) > 50 else value
                self.console.print(f"  • [cyan]{key}[/cyan]: {truncated_value}")
        else:
            self.console.print("[yellow]No memories found.[/yellow]")

def chat(session: str = "default"):
    """Start interactive chat session"""
    # Test connection
    console.print("[cyan]Testing connection to DeepSeek API...[/cyan]")
    if not llm_client.test_connection():
        console.print("[red]Failed to connect to DeepSeek API. Check your API key.[/red]")
        return
    
    console.print("[green]✓ Connection successful![/green]\n")
    
    # Initialize and start chat session
    chat_session = ChatSession(session_id=session)
    chat_session.chat_loop()

if __name__ == "__main__":
    import typer
    app = typer.Typer()
    app.command()(chat)
    app()