"""
Some information should be kept secret (don't share or commit to git).
e.g. API keys, secret keys used in cryptography, personal information

Some things you don't want to hard-code because they depend on the environment they're running in.
e.g. Database settings, local vs prod settings
"""
import os


# OPTION 1
# Hard-coded (only do this on local when testing)

api_key = "<api key here>"         # Hard-coded


# OPTION 2
# Use environment variables

# Unix/Linux/Mac
#   Set: export VAR_NAME="var value"
#   Read: echo $VAR_NAME

# Windows
#   Set: $env:VAR_NAME="var value"
#   Read: echo $env:VAR_NAME

os.environ['API_KEY'] = 'some value oiej9f89' # Set in Python

print(os.getenv('API_KEY'))       # Read environment variable
print(os.environ.get('API_KEY'))  # environ is a dict of all variables


# OPTION 3
# Read from a text file (don't commit to git)
# Okay if only a small number in a specific order/format
with open('secrets.txt') as file:
    api_key = file.read().strip()


# OPTION 4
# Use a .env file
# Best for production projects
# python-dotenv shown here, but environs used in daily_email_project
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv(override=True)  # loads .env contents to os.environ

print(os.getenv('API_KEY'))  # Environment variables can come from .env file
