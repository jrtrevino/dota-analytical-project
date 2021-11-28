import argparse
import pandas as pd
import parse_dota_api as dota
import sys
import time


def run(match_id_list, api_key):
    game_array = []
    player_array = []
    error_array = []
    for match_id in match_id_list:
        # grab data from api
        responses = dota.get_match_by_id([match_id], api_key)
        if len(responses) > 0:
            print("Grabbed match data from game: {}".format(match_id))
            # our response dataframe 'master'
            df = pd.json_normalize(responses[0])
            try:
                df.drop('players', inplace=True, axis=1)
                df.drop('picks_bans', inplace=True, axis=1)
            except KeyError as e:
                continue
            # normalize players column
            players = pd.json_normalize(responses[0], record_path=["players"], record_prefix="players.")
            game_array.append(df)
            player_array.append(players)
        else:
            print("Could not parse data from game: {}".format(match_id))
            error_array.append(match_id)
        time.sleep(1) # for api throttle limit
    if len(game_array) > 0:
        game_to_csv = pd.concat(game_array)
        players_to_csv = pd.concat(player_array)
        return game_to_csv, players_to_csv, error_array
    return 


def df_to_csv(output_name, df_game, df_players, error_array):
    try:
        df_game.to_csv("{}-game.csv".format(output_name[:-4]), mode="w+")
        df_players.to_csv("{}-players.csv".format(output_name[:-4]), mode="w+")
        if len(error_array) > 0:
            with open(output_name[:-3] + "-error.csv", "w+") as f:
                for match_id in error_array:
                    f.write(match_id)
    except Exception as e:
        print(e)
        print("Error making csv. Attempting to write to ./temp")
        df_game.to_csv('./{}-temp-game-csv'.format(output_name[:-4]), 'w+')
        df_players.to_csv('./{}-temp-players.csv'.format(output_name[:-4]), 'w+')


def load_file(filename):
    try:
        with open(filename, 'r') as f:
            match_ids = f.readlines() 
    except:
        print("Could not open file. Try again.")
        sys.exit(-1)
    return [stripped.rstrip() for stripped in match_ids[1:]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate CSV files from OpenDota match ids.')
    parser.add_argument('input', type=str, help="Input file path.")
    parser.add_argument('output', type=str, help="Output file path.")
    parser.add_argument('key', type=str, help="Your dota API key")
    args = parser.parse_args()
    if not args.key:
        api_key = dota.load_api_key('API_KEY')
    match_ids = load_file(args.input)
    df_game, df_players, errors = run(match_ids[:3], args.key if args.key else api_key)
    df_to_csv(args.output ,df_game, df_players, errors)
