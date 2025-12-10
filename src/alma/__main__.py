import typer
from rich.console import Console
from rich.panel import Panel
import sys
from pathlib import Path

# Importar funciones y módulos
from .core.chat import chat as chat_command
from .core.memory import app as memory_app
from .core.test import app as test_app

console = Console()

app = typer.Typer(
    name="alma",
    help="Alma - AI Assistant CLI with Memory",
    no_args_is_help=True,
    add_completion=False
)

# Registrar comandos
app.command()(chat_command)           # alma chat
app.add_typer(memory_app, name="memory")  # alma memory list/search/show/stats
app.add_typer(test_app, name="test")      # alma test all/db/llm

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
        
        # Import db module to initialize
        from .core.db import memory_db
        
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

def ensure_initialized():
    """Ensure database is initialized before running commands"""
    db_path = Path("db/alma.db")
    if not db_path.exists():
        console.print("[yellow]Database not found. Running initialization...[/yellow]")
        init()

def main():
    # Check if we're running a command that needs db
    if len(sys.argv) > 1 and sys.argv[1] not in ['version', 'init', 'test']:
        ensure_initialized()
    
    # Run the app
    app()

if __name__ == "__main__":
    main()