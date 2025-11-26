# Meta Directory - Alma's Blueprints

This directory contains schemas, templates, and configuration definitions that structure Alma's data and behavior.

## Contents

```
meta/
├── idea.yaml        # Schema for idea entries
├── log.yaml         # Schema for log entries  
├── memory.yaml      # Schema for memory entries
├── decision.yaml    # Schema for decision records
└── schema.sql       # Database schema definitions
```

## Purpose

These files define:
- **Data Structures**: How information is organized and validated
- **Templates**: Standard formats for different content types
- **Relationships**: How different data elements connect
- **Constraints**: Rules that ensure data quality and consistency

## Usage

- Schemas are used for data validation
- Templates provide starting points for new entries
- Database schema defines persistent storage structure
- All meta files are version controlled and evolve with the project