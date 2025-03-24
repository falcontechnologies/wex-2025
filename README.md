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



> Project: wex-2025 Work Experience
> 
> Purpose: A Subscription Manager to keep track of recurring subscriptions
> 
> Description: A collection of records that track the subscription attributes,
> defined in a data model and provides a way to query and view the collection
  
# Work Experience 2025 - Subscription Manager

## Introduction
Subscription Manager is a **Python** application using the **Flask** framework and
the **SQLite** embedded database to provide a durable record of subscriptions and
their attributes.

## Getting Started
To set up an enviroment for development, you will need to follow the subsequent sections.
This assumes that you have the code base installed locally and tracked with git.

There are additional resources provided in the project wiki.

### Virtual Environment Set Up

### Packages Set Up

### Connecting to SQLite

### Handling Changes to the Data Model

### Flask Set Up

## Working Data
A small collection of default data is provided as a SQL script to allow you to work
with testable data.

The details of adding and restoring this data set is TBD.

## Running the Application

TBD
