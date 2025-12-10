import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Optional
from .db import memory_db

console = Console()
app = typer.Typer(help="Manage Alma's memory system")

@app.command()
def list(
    limit: int = typer.Option(10, "--limit", "-l", help="Number of memories to show"),
    scope: Optional[str] = typer.Option(None, "--scope", "-s", help="Filter by scope")
):
    """List recent memories"""
    memories = memory_db.get_recent_memories(limit=limit, scope=scope)
    
    if not memories:
        console.print("[yellow]No memories found[/yellow]")
        return
    
    table = Table(title=f"Recent Memories (limit: {limit})")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")
    table.add_column("Scope", style="green")
    table.add_column("Updated", style="dim")
    
    for key, value, scope, updated in memories:
        # Truncar valor largo
        truncated = value[:50] + "..." if len(value) > 50 else value
        table.add_row(key, truncated, scope, updated)
    
    console.print(table)

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    limit: int = typer.Option(10, "--limit", "-l", help="Number of results")
):
    """Search memories by content"""
    results = memory_db.search_memories(query, limit=limit)
    
    if not results:
        console.print(f"[yellow]No memories found for '{query}'[/yellow]")
        return
    
    console.print(f"[bold]Search results for '{query}':[/bold]")
    for key, value, scope, updated in results:
        console.print(Panel(
            f"[bold cyan]Key:[/bold cyan] {key}\n"
            f"[bold]Scope:[/bold] {scope}\n"
            f"[bold]Time:[/bold] {updated}\n\n"
            f"{value}",
            title="Memory"
        ))

@app.command()
def show(key: str = typer.Argument(..., help="Memory key to display")):
    """Show a specific memory"""
    value = memory_db.get_memory(key)
    
    if value:
        console.print(Panel(value, title=f"Memory: {key}"))
    else:
        console.print(f"[yellow]Memory '{key}' not found[/yellow]")

@app.command()
def stats():
    """Show memory statistics"""
    try:
        import sqlite3
        conn = sqlite3.connect(memory_db.db_path)
        cursor = conn.cursor()
        
        # Total memories
        cursor.execute("SELECT COUNT(*) FROM memories")
        total = cursor.fetchone()[0]
        
        # By scope
        cursor.execute("SELECT scope, COUNT(*) FROM memories GROUP BY scope")
        by_scope = cursor.fetchall()
        
        # Oldest and newest
        cursor.execute("SELECT MIN(updated_at), MAX(updated_at) FROM memories")
        oldest, newest = cursor.fetchone()
        
        conn.close()
        
        console.print(Panel.fit(
            f"[bold]Memory Statistics[/bold]\n\n"
            f"Total memories: [cyan]{total}[/cyan]\n"
            f"Oldest: [dim]{oldest or 'N/A'}[/dim]\n"
            f"Newest: [dim]{newest or 'N/A'}[/dim]\n\n"
            f"By scope:\n" + "\n".join([f"  • {scope}: {count}" for scope, count in by_scope]),
            title="Alma Memory System"
        ))
        
    except Exception as e:
        console.print(f"[red]Error getting stats: {e}[/red]")

if __name__ == "__main__":
    app()