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

## Parsing Wrapper

This program takes .csv files containing match_ids returned from the parse dota API and creates two new .csv files for use with machine learning.

The two files generated contain:
1. Game information metadata
2. Player information for players who competed in a game.

### Running

To run this program, type:

```
$ parsing_wrapper.py [-h] input output key
```

Positional arguments are as follows:
  input       Input file path.
  output      Output file path.
  key         Your dota API key

  An example program run would be like so:

  ```
  $ python3 parsing_wrapper.py ./path/to/file.csv ./path/to/output.csv 12345-23455-57-685684356
  ```

  This will parse match_ids from file.csv and generate csv information.