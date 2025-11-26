# Alma Core Package

The heart of Alma's intelligence - currently minimal but designed to grow.

## Current Modules

### `alma.py`
The main agent class that will evolve into Alma's core personality and capabilities.

**Current responsibilities:**
- Basic agent structure
- Foundation for future features
- Simple interaction patterns

## Planned Evolution

As Alma grows, we'll add modules for:

1. **Memory management** - Handling data from `/data/` directory
2. **Learning systems** - Processing logs and memories
3. **Security features** - Basic pentesting capabilities
4. **API interfaces** - External communication

## Development Approach

We're building Alma incrementally:
- Add features only when needed
- Keep code simple and maintainable
- Focus on one capability at a time
- Test thoroughly at each step

## Running Alma

```bash
# From project root
python -m src.alma.alma

# Or after installation
python -c "from alma.alma import Alma; alma = Alma()"
```

*Simple beginnings for complex futures*