# Weather agent

## Introduction

Introductory example on how to start creating agents with Strands. This agent uses tools to get the information of the requested location and the weather information and offer this information to the user in human-friendly format.

## What do you need to run this project

* You need to create a Google API project an activate Geolocation API and Weather API. On the project you will create an API Key for web project. IMPORTANT NOTE: do not expose the key publicly, do not commit it with your source code and you do not share it with the models, they do not need to use the tools. This project can cost you some money, so once you tested, delete the API Key for the Google project. The project is free, but amount of requests to those API's can incurr on costs.

* Create you own `.env` file and add `API_KEY=<key_placeholder>`

* Create your own AWS account, for this example is used Amazon Bedrock.

## Installation

* Clone the project 
* Create your own virtual environment with `python3 -m venv .venv`
* Run `pip install -Ur requirements.txt`. This will install all the dependencies you need.

```bash
$ python3 -m venv .venv
$ pip install -Ur requirements.txt
```

## Run the agent

* Run `python agent.py`