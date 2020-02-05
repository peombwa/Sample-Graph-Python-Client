# Sample Graph Python Client
This is a sample Python client for Microsoft Graph. 

# Generate a Client
#### 1. Install [AutoRest](https://github.com/Azure/autorest.python)
    npm install -g "@autorest/autorest"
#### 2. Clone this repo
    git clone https://github.com/peombwa/Sample-Graph-Python-Client.git
#### 3. Change directory to the cloned repo and run:
    AutoRest-Beta --python --input-file:.\users.user.yml --output-folder:.\src\
