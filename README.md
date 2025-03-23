# wex-2025
Work Experience 2025 - Subscription Manager
## Database Migration Set Up

# Alembic & SQLAlchemy Migrations Guide

## Installation
To get started with **Alembic** and **SQLAlchemy**, install them using pip:
```bash
pip install alembic sqlalchemy
```

## Creating Migrations
To create a new migration based on your SQLAlchemy models:
```bash
alembic revision --autogenerate -m "Your migration message"
```

## Applying Migrations
To apply the latest migration:
```bash
alembic upgrade head
```

## Common Commands
### Upgrade to the Latest Migration
```bash
alembic upgrade head
```

### Upgrade to a Specific Migration
```bash
alembic upgrade <revision_id>
```

### Downgrade to a Previous Migration
```bash
alembic downgrade <revision_id>
```

### Downgrade to the Base (Initial State)
```bash
alembic downgrade base
```

### Check Current Revision
```bash
alembic current
```

### Show Migration History
```bash
alembic history
```

### Generate a New Empty Migration
```bash
alembic revision -m "Your migration message"
```

## Example Workflow
1. Make changes to your **SQLAlchemy models**.
2. Generate a new migration:
   ```bash
   alembic revision --autogenerate -m "Add new column to users table"
   ```
3. Review the generated migration script in `alembic/versions` directory.
4. Apply the migration:
   ```bash
   alembic upgrade head
   ```
5. If needed, revert the migration:
   ```bash
   alembic downgrade -1
   ```


