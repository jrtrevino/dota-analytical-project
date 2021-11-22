# Preprocessing

This folder contains the necessary code needed to preprocess data for our classification project.
Any and all preprocessing code should retrieve any necessary data from external sources.

## Parse_dota_api

A simple Python script that will request and parse data from the OpenDota API. 
You can view the api [here](https://www.opendota.com/)

### dependencies

#### API Key

You must obtain an API key to use the OpenDota API. Visit the site above for information obtaining one.

#### dotenv

This program uses the python-dotenv library to load an API key from a .env file. To install, run:

```
$ pip3 install python-dotenv
```

For setting up your .env file, follow these steps:

```
$ touch .env
$ echo "API_KEY=\"<YOUR_API_KEY>\"" > .env
```

### Running

To run this program, type:

```
# python3 parse_dota_api.py
```

This will, by default, request and parse 100 responses from the OpenDota API.