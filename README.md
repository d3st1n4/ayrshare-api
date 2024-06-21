# Ayrshare API Integration Project

![CI](https://github.com/d3st1n4/ayrshare-api/actions/workflows/stylechecker.yaml/badge.svg)

This project demonstrates how to use the Ayrshare API to retrieve account information and post content to Twitter using Python. The code includes both a GET request to fetch account details and a POST request to create a new post on Twitter. Additionally, it incorporates SQL through its addition of the API data to a database.
## Project Structure

Separated into two sections — a get request and post request — the program makes a twitter post first, then proceeds to make a get request for the post. The last portion of the code adds the data to a database.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

### Libraries to Install

Install the required Python libraries using pip:

```
pip install requests sqlalchemy pandas
``` 

### Environment Variables

You can set the environment variable in your terminal session with the following command:

```
export AYRSHARE_API_KEY='your_ayrshare_api_key_here'
```

### How to Run Program
Clone the repository:

```
git clone <your-repo-url>
cd <your-repo-directory>
```

Set up environment variables:

Make sure your Ayrshare API key is correctly set in your environment variables.

Run the Python script:

```
python3 your_script_name.py
```
