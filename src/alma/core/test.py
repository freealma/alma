import typer
from rich.console import Console
from rich.panel import Panel
from .llm_client import llm_client
from .db import memory_db
from ..utils.config import config

console = Console()
app = typer.Typer(help="Test Alma components")

@app.command()
def all():
    """Test all Alma components"""
    console.print(Panel.fit(
        "[bold cyan]Alma System Test[/bold cyan]",
        title="Testing"
    ))
    
    results = []
    
    # Test 1: Configuration
    console.print("[cyan]1. Testing configuration...[/cyan]")
    try:
        config.validate()
        results.append(("Configuration", "✅ OK"))
        console.print("[green]  ✓ Configuration loaded[/green]")
    except Exception as e:
        results.append(("Configuration", f"❌ {str(e)[:50]}"))
        console.print(f"[red]  ✗ Configuration error: {e}[/red]")
    
    # Test 2: Database
    console.print("[cyan]2. Testing database...[/cyan]")
    try:
        memory_db.init_db()
        
        # Try a simple operation
        test_key = "__test_memory__"
        memory_db.add_memory(test_key, "Test memory", scope="test")
        retrieved = memory_db.get_memory(test_key)
        
        if retrieved == "Test memory":
            results.append(("Database", "✅ OK"))
            console.print("[green]  ✓ Database operational[/green]")
        else:
            results.append(("Database", "❌ Data corruption"))
            console.print("[red]  ✗ Data retrieval failed[/red]")
        
        # Cleanup
        import sqlite3
        conn = sqlite3.connect(memory_db.db_path)
        conn.execute("DELETE FROM memories WHERE key = ?", (test_key,))
        conn.commit()
        conn.close()
        
    except Exception as e:
        results.append(("Database", f"❌ {str(e)[:50]}"))
        console.print(f"[red]  ✗ Database error: {e}[/red]")
    
    # Test 3: LLM Connection
    console.print("[cyan]3. Testing LLM connection...[/cyan]")
    if llm_client.test_connection():
        results.append(("LLM Connection", "✅ OK"))
        console.print("[green]  ✓ LLM connection successful[/green]")
    else:
        results.append(("LLM Connection", "❌ Failed"))
        console.print("[red]  ✗ LLM connection failed[/red]")
    
    # Summary
    console.print("\n" + "="*50)
    console.print("[bold]Test Summary:[/bold]")
    
    all_passed = True
    for component, status in results:
        console.print(f"  {component}: {status}")
        if "❌" in status:
            all_passed = False
    
    console.print("\n" + "="*50)
    
    if all_passed:
        console.print("[bold green]✅ All tests passed! Alma is ready.[/bold green]")
    else:
        console.print("[bold red]❌ Some tests failed. Check configuration.[/bold red]")
    
    return 0 if all_passed else 1

@app.command()
def db():
    """Test only database"""
    console.print("[cyan]Testing database...[/cyan]")
    try:
        memory_db.init_db()
        console.print("[green]✅ Database OK[/green]")
        return 0
    except Exception as e:
        console.print(f"[red]❌ Database error: {e}[/red]")
        return 1

@app.command()
def llm():
    """Test only LLM connection"""
    console.print("[cyan]Testing LLM connection...[/cyan]")
    if llm_client.test_connection():
        console.print("[green]✅ LLM connection OK[/green]")
        return 0
    else:
        console.print("[red]❌ LLM connection failed[/red]")
        return 1

if __name__ == "__main__":
    app()