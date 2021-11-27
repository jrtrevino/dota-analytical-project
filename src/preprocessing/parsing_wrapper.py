import argparse
import pandas as pd
import parse_dota_api as dota
import time



def run(match_id_list, api_key):
    df_array = []
    error_array = []
    for match_id in match_id_list:
        # grab data from api
        responses = dota.get_match_by_id([match_id], api_key)
        if responses:
            print("Grabbed match data from game: {}".format(match_id))
            df_array.append(pd.json_normalize(responses))
        else:
            print("Could not parse data from game: {}".format(match_id))
            error_array.append(match_id)
        time.sleep(1) # for api throttle limit
    df_to_csv = pd.concat(df_array)
    return df_to_csv, error_array


def df_to_csv(output_name, df, error_array):
    try:
        df.to_csv(output_name, mode="w+")
        if len(error_array) > 0:
            with open(output_name[:-3] + "-error.csv", "w+") as f:
                for match_id in error_array:
                    f.write(match_id)
    except Exception as e:
        print(e)
        print("Error making csv. Attempting to write to ./temp")
        df.to_csv('./temp.csv', 'w+')
    


if __name__ == "__main__":
    api_key = dota.load_api_key('API_KEY')
    df, errors = run([6288572418,
         6288572419,
         6289096708,
         6289096709,
         6289096711,
         6289096714], api_key)
    df_to_csv('testrun.csv',df, errors)
