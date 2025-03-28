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

This section will teach you how to run the application that has been created using Flask.


#### PreRequisites

Before starting this section, it is assumed that you have successfully completed the [Virtual Environment Set Up](#Virtual-Environment-Set-Up)
and the [Packages Set Up](#Packages-Set-Up).


#### Installing Flask
Before Flask is ready to be installed, the virtual environment must first be activated using the following commands:

##### 1.Folder Navigation
type the following command into Terminal/Linux Command Line/PowerShell/Command Prompt to
navigate to the folder where the program is stored:

    cd subscriptionManager

Replace the name '*subscriptionManager*' with the name of the folder where the program is stored.

##### 2.Activating Virtual Environment

On macOS/Linux, type the following command into Terminal/Linux Command Line:

    source venv/bin/activate

On Windows, type the following command into PowerShell/Command Prompt:

    venv\Scripts\activate

Replace the name '*venv*' with the name of the virtual environment. 
Your shell prompt will change to show the name of the activated environment.

##### 3.Downloading Flask

If Flask is not already in the virtual environment, type the following command to install 
Flask:

    pip install Flask


#### Running Flask

Now that you have Flask in the virtual environment,
type in the following command to start up the application:

    flask --app main run

Replace the name '*main*' with the main file of this application.

This will start up the application in a development server at http://127.0.0.1:5000

You will know if the application is working when the following message pops up:

     * Serving Flask app 'main'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
#### References

https://flask.palletsprojects.com/en/stable/quickstart/

https://flask.palletsprojects.com/en/stable/installation/

https://python.land/virtual-environments/virtualenv

## Working Data
A small collection of default data is provided as a SQL script to allow you to work
with testable data.

The details of adding and restoring this data set is TBD.

## Running the Application

TBD

## Python Packages Set Up

To set up the required Python libraries for this project, follow these steps:

### 1. Create a Virtual Environment
Run the following command to create a virtual environment:

```sh
python -m venv venv
```

- On **macOS/Linux**, activate it using:
  ```sh
  source venv/bin/activate
  ```
- On **Windows**, use:
  ```sh
  venv\Scripts\activate
  ```

### 2. Install Dependencies
Use the package manager `pip` to install all necessary libraries from the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### 3. Verify Installation
Check that the packages are correctly installed:

```sh
pip list
```

### References
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [pip Install Requirements](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
=======
