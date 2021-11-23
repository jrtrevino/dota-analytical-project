import parse_dota_api

def to_csv(file_name, match_ids):
    with open(file_name, 'a+') as f:
        f.write('matchid\n')
        f.writelines(match_ids)
    


def wrapper():
    key = parse_dota_api.load_api_key('API_KEY')
    desired_matches = 100000
    results = parse_dota_api.get_match_ids(key, desired_matches)
    results = [(str(matchid) + "\n") for matchid in results]
    results_per_file = 25000
    file_number = 0
    for _ in range(0, len(results), results_per_file):
        result_slice = results_per_file * file_number
        file_name = f"matchid-output/matchids-{file_number}.csv"
        to_csv(file_name, results[result_slice: result_slice + results_per_file])
        file_number += 1

wrapper()