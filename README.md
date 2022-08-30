# KenBox-python

The KenBox Example is an exercise to illustrate a problem with multiple programatic solutions where one can be preferred.

The example goes like this: the KenBox can be opened and can contain a smaller KenBox. The smaller one can be opened to contain another smaller KenBox. And so on and so forth. 

Problem: Return the number of children any one KenBox has contained within.

Sample Execution Output: 
![alt text][video]

[video]: KenBox-python_ScreenRecording.gif "KenBox-python Screen Recording"

## Setup and install

```sh
# Clone KenBox-python repo to local
$ git clone https://github.com/kascheri12/KenBox-python.git

# Change directory into repo root
$ cd KenBox-python

# Optional - Install virtualenv if desirec (recommended)
$ pip3 install virtualenv

# Optional - Create vitual env named venv with python3
$ virtualenv venv -p=python3

# Optional - Activate the venv virtual env
$ source venv/bin/activate

# Optional - Add flask dev env variables in root with .flaskenv file
FLASK_APP=app.py
FLASK_RUN_HOST=localhost
FLASK_RUN_PORT=5000
FLASK_ENV=development

# Install requirements into the virtual env for the listed app requirements
$ pip install -r requirements.txt

# Run the flask app in development
$ flask run

```
