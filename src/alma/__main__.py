import typer
from rich.console import Console
from rich.panel import Panel

from .core.chat import app as chat_app

console = Console()

app = typer.Typer(
    name="alma",
    help="Alma - AI Assistant CLI with Memory",
    no_args_is_help=True,
    add_completion=False
)

# Add commands from chat module
app.add_typer(chat_app, name="chat")

@app.callback()
def callback():
    """Alma - Your intelligent AI assistant with memory"""
    pass

@app.command()
def version():
    """Show Alma version"""
    console.print(Panel.fit(
        "[bold cyan]Alma AI Assistant[/bold cyan]\n"
        "Version: 0.1.0\n"
        "With memory and DeepSeek integration",
        title="Alma"
    ))

@app.command()
def init():
    """Initialize Alma (setup database, etc.)"""
    console.print("[cyan]Initializing Alma...[/cyan]")
    
    try:
        from .core.db import memory_db
        memory_db.init_db()
        console.print("[green]✓ Database initialized[/green]")
        
        from .core.llm_client import llm_client
        console.print("[green]✓ LLM client initialized[/green]")
        
        console.print("\n[bold green]Alma is ready to use![/bold green]")
        console.print("Run [cyan]alma chat[/cyan] to start chatting")
        
    except Exception as e:
        console.print(f"[red]Initialization failed: {e}[/red]")

if __name__ == "__main__":
    app()