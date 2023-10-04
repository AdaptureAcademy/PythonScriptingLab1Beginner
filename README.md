# Interacting with Cloudflare API with Python

---

## Pre-requisites

You must have Python installed and set up on your system to make API calls to Cloudflare and interacting with the
returned data.

### Installation of Python

- #### Windows

    1. Download the latest version of Python from [here](https://www.python.org/downloads/).
    2. Run the installer and follow the instructions.
    3. Make sure to check the box that says "Add Python to PATH".
    4. Click "Install Now".
    5. Once the installation is complete, click "Close".
    6. Open Command Prompt and type `python --version` to check if Python is installed correctly.
    7. If the version is displayed, you have successfully installed Python.
    8. If the version is not displayed, you may have to restart your computer and try again.

- #### Linux

    1. Open Terminal and type `sudo apt-get install python3`.
    2. Once the installation is complete, type `python3 --version` to check if Python is installed correctly.
    3. If the version is displayed, you have successfully installed Python.

### Make a virtual environment

- A virtual environment is a tool that helps to keep libraries required by different projects separate by creating
  isolated python virtual environments for them. This is one of the most important tools that most of the Python
  developers use.
- Every Python project has a `requirements.txt` file that contains the names of all the libraries required to run the
  project. You can install all the libraries by running `pip install -r requirements.txt` in the project
  directory. `requirements.txt` is similar to `package.json` in Node.js.
- To create a virtual environment, run `python3 -m venv venv` in the project directory.

### Activation of the Virtual Environment

- #### Windows

  To activate the virtual environment from your CMD/PowerShell, run `venv\Scripts\activate.bat` in the project
  directory.

- #### Linux

  To activate the virtual environment from your Terminal, run `source venv/bin/activate` in the project directory.

### Installation of libraries via pip

libraries are pre-built packages that allow you to perform various actions without writing code from scratch. It
speeds up the development process and adheres to the DRY (Don't Repeat Yourself) principle.

To install the libraries from `requirements.txt` file, run `pip install -r requirements.txt` in the project
directory. You can install a library individually by running `pip install <library-name>` in the project
directory.

---

# Getting Started

## Installing Necessary Libraries

For this lab, we need two libraries: `requests` and `python-dotenv`. `requests` is a library that allows you to make
HTTP requests. `python-dotenv` is a library that allows you to load environment variables from a `.env` file.

Use the following command in your CMD/Terminal to install the libraries:

```bash
pip install requests python-dotenv
```

## Initializing Code Files

To structure your project, you should organize your code into files. For this guide, we will create two files: `main.py`
for your script and `.env` for your environment variables.

- ### Creating the `.env` File

    1. In your project directory, create a new file named `.env`.
    2. Open the `.env` file and add your Cloudflare API token like so:
        ```plaintext
        CLOUDFLARE_API_TOKEN='your-api-token-here'
        ```

- ### Creating the `main.py` File

    1. In your project directory, create a new file named `main.py`.
    2. Open `main.py` with your text editor of choice.
    3. Import the necessary libraries and load the environment variables:

  ```python
  import os
  import requests
  from dotenv import load_dotenv
  
  load_dotenv()
  
  api_token = os.getenv('CLOUDFLARE_API_TOKEN')
  ```

    4. Now you can add the Cloudflare API calls as functions in `main.py` like so:

  ```python
   # Define headers for the API requests, including the Authorization token and the content type.
  headers = {
      'Authorization': f'Bearer {api_token}',
      'Content-Type': 'application/json',
  }
  
  
  # Function to fetch user details from Cloudflare's API
  def fetch_user_details():
      # Define the URL for the user details endpoint
      url = 'https://api.cloudflare.com/client/v4/user'
      # Send a GET request to the specified URL, with the defined headers
      response = requests.get(url, headers=headers)
      # Check if the response status code is 200 (OK)
      if response.ok:
          # Parse the JSON response and print it
          data = response.json()
          print(data)
      else:
          # If the response status code is not 200, print the error status code and response text
          print(f'Error: {response.status_code}')
          print(response.text)
  
  
  # Function to list zones in Cloudflare's account
  def list_zones():
      # Define the URL for the zones listing endpoint
      url = 'https://api.cloudflare.com/client/v4/zones'
      # Send a GET request to the specified URL, with the defined headers
      response = requests.get(url, headers=headers)
      # Check if the response status code is 200 (OK)
      if response.ok:
          # Parse the JSON response and print it
          data = response.json()
          print(data)
      else:
          # If the response status code is not 200, print the error status code and response text
          print(f'Error: {response.status_code}')
          print(response.text)
  
  
  # Function to create a DNS record in a specified zone
  def create_dns_record(zone_id, dns_record_data):
      # Define the URL for the DNS record creation endpoint, including the specified zone ID
      url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
      # Send a POST request to the specified URL, with the defined headers and JSON payload
      response = requests.post(url, headers=headers, json=dns_record_data)
      # Check if the response status code is 200 (OK)
      if response.ok:
          # Parse the JSON response and print it
          data = response.json()
          print(data)
      else:
          # If the response status code is not 200, print the error status code and response text
          print(f'Error: {response.status_code}')
          print(response.text)
  
  
  # Main execution starts here when the script is run
  if __name__ == "__main__":
      # Example usage of the defined functions
      fetch_user_details()  # Fetch and print user details
      list_zones()  # List and print zones
      # Create and print a new DNS record in a specified zone
      create_dns_record('your-zone-id-here', {
          'type': 'A',
          'name': 'example.com',
          'content': '192.0.2.1',
          'ttl': 120,
      })
  ```

---

With this structure, your project directory should have the following files and directory:

- `.env`: contains your environment variables.
- `main.py`: contains your script and Cloudflare API calls.
- `venv`: contains your virtual environment and libraries.

Now, you can easily run your script from the terminal with the command `python3 main.py`. This will execute the
Cloudflare API calls defined in your `main.py` file. Remember to replace placeholders like `'your-api-token-here'`
and `'your-zone-id-here'` with your actual values.

---

## Further Reading

- [Cloudflare API Documentation](https://developers.cloudflare.com/api)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)

This beginner's guide should now have provided you with the basics needed to set up Python on your system, install
necessary dependencies, and make API calls to Cloudflare's API. Remember to refer to the Cloudflare API documentation
for more detailed information on different API endpoints and how to interact with them.