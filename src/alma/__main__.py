import typer
from rich.console import Console
from rich.panel import Panel
import os
from pathlib import Path
from .core.chat import chat, memory, test

console = Console()

app = typer.Typer(
    name="alma",
    help="Alma - AI Assistant CLI with Memory",
    no_args_is_help=True,
    add_completion=False
)

app.command()(chat)
app.command()(memory)
app.command()(test)

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
        # Ensure db directory exists
        db_dir = Path("db")
        db_dir.mkdir(exist_ok=True)
        
        # Import schema and initialize database
        schema_path = Path(__file__).parent.parent.parent / "meta" / "schema.sql"
        
        if not schema_path.exists():
            console.print(f"[red]Schema file not found at: {schema_path}[/red]")
            return
        
        # Import db module to initialize
        from .core.db import memory_db
        
        # The db initialization happens automatically in MemoryDB.__init__
        console.print("[green]✓ Database initialized[/green]")
        
        # Test LLM client
        from .core.llm_client import llm_client
        console.print("[cyan]Testing LLM connection...[/cyan]")
        if llm_client.test_connection():
            console.print("[green]✓ LLM client initialized and connected[/green]")
        else:
            console.print("[yellow]⚠ LLM client initialized but connection test failed[/yellow]")
        
        console.print("\n[bold green]Alma is ready to use![/bold green]")
        console.print("Run [cyan]alma chat[/cyan] to start chatting")
        
    except Exception as e:
        console.print(f"[red]Initialization failed: {e}[/red]")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")

# Add a wrapper to automatically init db if needed
def ensure_initialized():
    """Ensure database is initialized before running commands"""
    db_path = Path("db/alma.db")
    if not db_path.exists():
        console.print("[yellow]Database not found. Running initialization...[/yellow]")
        init()

# Override the main entry point to ensure initialization
def main():
    # Check if we're running a command that needs db
    import sys
    if len(sys.argv) > 1 and sys.argv[1] not in ['version', 'init']:
        ensure_initialized()
    
    # Run the app
    app()

if __name__ == "__main__":
    main()