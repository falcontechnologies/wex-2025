# wex-2025
Work Experience 2025 - Subscription Manager

## Flask Framework Set Up

This section will teach you how to run the application that has been created using Flask.


### PreRequisites

Before starting this section, it is assumed that you have successfully completed the [Python Virtual Set Up](#Python-Virtual-Set-Up)
and the [Python Package Set Up](#Python-Packages-Set-Up).


### Installing Flask
Before Flask is ready to be installed, the virtual environment must first be activated using the following commands:

#### 1.Folder Navigation
type the following command into Terminal/Linux Command Line/PowerShell/Command Prompt to
navigate to the folder where the program is stored:

    cd subscriptionManager

Replace the name '*subscriptionManager*' with the name of the folder where the program is stored.

#### 2.Activating Virtual Environment

On macOS/Linux, type the following command into Terminal/Linux Command Line:

    source venv/bin/activate

On Windows, type the following command into PowerShell/Command Prompt:

    venv\Scripts\activate

Replace the name '*venv*' with the name of the virtual environment. 
Your shell prompt will change to show the name of the activated environment.

#### 3.Downloading Flask

Now that you are in the virtual environment, type the following command to install 
Flask:

    pip install Flask


### Running Flask

Now that you have Flask in the virtual environment,
type in the following command to start up the application:

    flask --app main run

Replace the name '*main*' with the main file of this application.

This will start up the application in a development server at http://127.0.0.1:5000
### References

https://flask.palletsprojects.com/en/stable/quickstart/

https://flask.palletsprojects.com/en/stable/installation/

https://python.land/virtual-environments/virtualenv

