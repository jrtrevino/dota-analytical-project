from dotenv import load_dotenv
import json
import os
import requests
import sys
import time


api_endpoint = "https://api.opendota.com/api/"
radiant = 1  # set as appropriate for team_id
dire = -1

# Loads API Key from .env file.
# key_name -> string name for api key in .env file.
# return -> string representation of api key.


def load_api_key(key_name):
    try:
        load_dotenv()
        API_KEY = os.getenv(key_name)
    except:
        print("Could not grab API key from .env file.")
        sys.exit(-1)
    return API_KEY

# Performs a GET request on the /publicMatches route of the OpenDota api.
# Requires an OpenDota API key.
# api_key -> a string representation of an api_key
# num_matches -> number of unique matches to return (optiona - default 100).
# returns -> an array of unique match IDs.


def get_match_ids(api_key, num_matches=None):
    default_matches = 100
    num_api_calls = 0
    query_strings = f"api_key={api_key}"
    resource = "publicMatches"
    uri = f"{api_endpoint}{resource}?{query_strings}"
    response_json = None
    match_ids = set()
    match_id_qs = None
    print("Begin HTTP Request -> GET")
    while len(match_ids) <= (num_matches if num_matches else default_matches):
        try:
            response = requests.get(uri if not match_id_qs else uri+match_id_qs)
            response_json = response.json()
            # match id's are sorted from high to low
            next_match_id = response_json[-1]['match_id']
            match_id_qs = f"&less_than_match_id={next_match_id}"
            if not response.status_code == 200:
                print(f"Status Code Error: {response.status_code}")
                print(f"{response_json}")
                print("Waiting a minute before fetching next results...")
                time.sleep(2)
                continue
            # grab match ids
            num_api_calls += 1
            [match_ids.add(match['match_id']) for match in response_json]
            time.sleep(1) # 1 api call per second
            print("Number of api calls made: {}".format(num_api_calls))
            print("total number of unique match ids collected: {}".format(len(match_ids)))
        except Exception as e:
            print(f"Unable to fetch endpoint: {uri}")
            print(f"{e}")
            break
    print(f"Total API Calls made: {num_api_calls}")
    return sorted(list(match_ids)[:num_matches if num_matches else default_matches])

# Requests a specific match by id on the OpenDota API.
# The request is then prepared for entry into our dataset.
# match_list -> a list containing unique match_ids.
# api_key -> string representation of an api_key
# returns -> an array of entries to place into a .csv.


def get_match_by_id(match_list, api_key):
    query_strings = f"api_key={api_key}"
    resource = "matches/"
    route = f"{api_endpoint}{resource}"
    response_json = None
    dataset_entries = []
    for match_id in match_list:
        try:
            response = requests.get(f"{route}{match_id}?{query_strings}")
            response_json = response.json()
            team_mapping = radiant if response_json['radiant_win'] else dire
            game_mode = response_json['game_mode']
            lobby_type = response_json['lobby_type']
            players = response_json['players']
            print(response_json)
            break
            # TODO: parse response_json[players] for dataset entry
            # TODO: Create dataset entry and append into dataset_entries
        except Exception as e:
            print("Could not parse match.")
            print(e)
            break
    return dataset_entries


if __name__ == "__main__":
    # grab api key
    key = load_api_key('API_KEY')
    match_ids = get_match_ids(key)
    get_match_by_id(match_ids, key)
