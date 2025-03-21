# wex-2025

Work Experience 2025 - Subscription Manager

Python Virtual Set Up

    1. Check if Python is Installed
        Ensure Python is installed on your system by running:

        python --version

        or, if you use python3:

        python3 --version

    2. Create a Virtual Environment
        Navigate to your project folder and run:

        python -m venv venv

        or if you use python3:

        python3 -m venv venv

    3. Activate the Virtual Environment
        Windows (Command Prompt): venv\Scripts\activate

        Windows (PowerShell): venv\Scripts\Activate.ps1

        macOS/Linux: source venv/bin/activate

    4. Install Dependencies
        Once inside the virtual environment, install the required dependencies with:

        pip install -r requiredfile
        (make sure requredfile is the dependencies you need)

    5. Verify Setup
        Check that the environment is working correctly:

        python -m pip list

    6. Deactivating the Virtual Environment:
        To exit the virtual environment, run:

        deactivate
