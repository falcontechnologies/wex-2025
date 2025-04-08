> Project: wex-2025 Work Experience
>
> Purpose: A Subscription Manager to keep track of recurring subscriptions
>
> Description: A collection of records that track the subscription attributes,
> defined in a data model and provides a way to query and view the collection

# Work Experience 2025 - Subscription Manager

----
## Introduction
Subscription Manager is a **Python** application using the **Flask** framework and
the **SQLite** embedded database to provide a durable record of subscriptions and
their attributes.

---
## Getting Started
To set up an environment for development, you will need to follow the subsequent sections.
This assumes that you have the code base installed locally and tracked with git.

There are additional resources provided in the project wiki.

Note that we are using Python 3.13 for this application. Any dependencies
should be included in the file ```requirements.txt```. For information
on the format of this file, please refer to the
[pip documentation](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

### Virtual Environment Set Up  {#venv}

#### Checklist
* Check for Python
* Create a virtual environment (venv)
* Activate the venv
* Verify setup
* On exit: Deactivate the venv

#### Check for Python

Ensure Python is installed on your system by running:

```
python3 --version
```
You should confirm that you have an alias to the python commands to 
protect against the case that you also have Python 2.7 installed.

You can confirm this by running
```
python --version
```
and ensuring that it is not some other version of Python running.

Subsequent sections and commands assume that running any command will
execute the correct Python 3 family command.

#### Create a virtual environment
A virtual environment is used in this project to keep your project libraries
and packages separate from any other Python packages or versions. It stores
an optional Python version and the required packages for the project to run
in the virtual environment.

You can name the virtual environment anything you want. It **MUST** be excluded
from the files committed to *git*.

For example, we could use the name *wex* for the directory holding the
virtual environment.

Navigate to your project folder and run:

```
python -m venv wex
```

#### Activate the virtual environment
macOS/Linux: 
```
source wex/bin/activate
```

Windows (Command Prompt):
``` 
wex\Scripts\activate
```

Windows (PowerShell):
```
wex\Scripts\Activate.ps1
```
If you are running an integrated development tool like VSCode or IntelliJ,
please refer to the application documentation for the correct way to set up
a virtual environment.

#### Verify Setup
Check that the environment is working correctly:
```aiignore
pip list
```
or
```
python -m pip list
```

#### Deactivating the Virtual Environment:
To exit the virtual environment, run:

```
deactivate
```
---

### Packages Set Up  {#packages}
You must be inside the virtual environment. See the above steps.
To set up the required Python libraries for this project, run this step:
```
pip install -r requirements.txt
```
Note that packages should be pinned to specific versions or major.minor versions.

You can confirm the installed packages using this command:
```sh
pip list
```

Note that packages should remain installed in the *venv* between sessions.

---
### Connecting to SQLite

Connecting to SQLite is performed in code. Please refer to the codebase
for more details.

Note that as deployed, the application and database run locally.

---

## Database Migration Set Up and Changes to the Data Model

The selected migration tool for this project is [Alembic](https://alembic.sqlalchemy.org/en/latest/)

### Installation
To get started with **Alembic** and **SQLAlchemy**, install them using pip:
```bash
pip install alembic sqlalchemy
```

### Creating Migrations
To create a new migration based on your SQLAlchemy models:
```bash
alembic revision --autogenerate -m "Your migration message"
```

### Applying Migrations
To apply the latest migration:
```bash
alembic upgrade head
```

### Common Commands
#### Upgrade to the Latest Migration
```bash
alembic upgrade head
```

#### Upgrade to a Specific Migration
```bash
alembic upgrade <revision_id>
```

#### Downgrade to a Previous Migration
```bash
alembic downgrade <revision_id>
```

#### Downgrade to the Base (Initial State)
```bash
alembic downgrade base
```

#### Check Current Revision
```bash
alembic current
```

#### Show Migration History
```bash
alembic history
```

#### Generate a New Empty Migration
```bash
alembic revision -m "Your migration message"
```

### Example Workflow
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

----
## Running the Application

The application uses the Flask framework.

### Prerequisites

Before starting this section, it is assumed that you have successfully completed the [Virtual Environment Set Up](#Virtual-Environment-Set)
and the [Packages Set Up](#packages-set-up-packages).

### Installing Flask
Before Flask is installed, the virtual environment must be activated. See the above sections
for details.

If Flask is not already in the virtual environment, type the following command to install 
Flask:
```
pip install Flask
```
### Running Flask

Now that you have Flask in the virtual environment,
type in the following command to start up the application:

```
flask --app main run
```

Replace the name '*main*' with the main file of this application.

This will start up the application in a development server at http://127.0.0.1:5000

You will know if the application is working when the following message pops up:

     * Serving Flask app 'main'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit

### Notes

@security

Flask appears to require the installation of pyaudio (!!!) and may require a security review.
See the [pypi note](https://pypi.org/project/PyAudio/) on installation.

---

## Working Data

A small collection of default data is provided as a SQL script to allow you to work
with testable data.

The details of adding and restoring this data set is __TBD__.

---

## References

[Python Virtual Environments - venv](https://docs.python.org/3/library/venv.html)

[pip Install Requirements](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

[Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

https://flask.palletsprojects.com/en/stable/installation/

https://python.land/virtual-environments/virtualenv
