from dotenv import load_dotenv
import os
import requests
import sys


api_endpoint = "https://api.opendota.com/api/"


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

# Performs a GET request on a specified route of the Dota api.
# If no route is provided, the default is /publicMatches.
# Requires an open Dota API key.
# api_key -> a string representation of an api_key
# num_matches -> number of unique matches to return (optional).
# route -> string representation of an api route (optional).
# returns -> an array of unique match IDs.
# Please only provide num_matches or route, but not both.


def get_api_resource(api_key, num_matches=None, route=None):
    if num_matches and route:
        print("Please provide only num_matches or route.")
        return
    query_strings = f"api_key={api_key}"
    resource = route if route else "publicMatches"
    uri = f"{api_endpoint}{resource}?{query_strings}"
    default_matches = 100
    response_json = None
    match_ids = set()
    while len(match_ids) != (num_matches if num_matches else default_matches):
        try:
            response = requests.get(uri)
            response_json = response.json()
            if not response.status_code == 200:
                print(f"Status Code Error: {response.status_code}")
                print(f"{response_json}")
                break
            # grab match ids
            [match_ids.add(match['match_id']) for match in response_json]
        except Exception as e:
            print(f"Unable to fetch endpoint: {uri}")
            print(f"{e}")
            break
    return match_ids


if __name__ == "__main__":
    # grab api key
    key = load_api_key('API_KEY')
    match_ids = get_api_resource(key)
