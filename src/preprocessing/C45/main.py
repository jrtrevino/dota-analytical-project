import pandas as pd
from collections import defaultdict

if __name__ == '__main__':


    df_match = pd.read_csv('match.csv')
    # df_match_outcome = pd.read_csv('match_outcomes.csv')
    df_players = pd.read_csv('players.csv')
    import pdb; pdb.set_trace()
    df_heroes = pd.read_csv('hero_names.csv')

    match_id = df_match['match_id'].values
    radiant_win = df_match['radiant_win'].values

    heros_picked = defaultdict(int)
    for index, row in df_players.iterrows():
        hero = row['hero_id']
        heros_picked[hero] += 1 / len(df_match)

    low_percentage_heros = dict(filter(lambda x: x[1] < .06, heros_picked.items())) #filter out the heros that have a low percentage pick rate, in this case we consider 6 % to be low)

    heros_id = df_heroes['hero_id'].values
    heros_name = df_heroes['localized_name']
    import pdb; pdb.set_trace()

    match_radiant_win = {}
    heroes = {}
    for index, match in enumerate(match_id):
        match_radiant_win[match] = radiant_win[index]
    for index, hero in enumerate(heros_id):
        heroes[hero] = heros_name[index]



    current_match_id = 0
    distinct_heroes = defaultdict(set)

    # import pdb; pdb.set_trace()

    filtered_heros_id = list(filter(lambda x: x not in low_percentage_heros, heros_id))


    with open('hero_pick_outcomes2.csv', 'w') as file:
        file.write('match_id,')
        for i in filtered_heros_id:
            file.write('hero{0},'.format(i))
        file.write('hero_low,')
        file.write('outcome\n')
        file.write('-1,')
        for i in range(len(filtered_heros_id)):
            file.write('2,')
        file.write('5,') #attribute amount for low percentage
        file.write('2\n')
        file.write('outcome\n')
        hero_pick = []
        for index, row in df_players.iterrows():
            m_id = row['match_id']
            hero = row['hero_id']
            hero_pick.append(hero)
            outcome = radiant_win[m_id]
            distinct_heroes[(index + 1) % 5].add(hero)

            if (index + 1) % 5 == 0: #time to write result since it's five heroes already
                # import pdb; pdb.set_trace()
                if current_match_id % 2 == 1:  # this is dyre team
                    outcome = not outcome
                # hero_pick = map(str, hero_pick)
                # str_out = str(current_match_id) + ',' + ','.join(hero_pick) + ',' + str(outcome)
                file.write(str(current_match_id) + ',')
                # import pdb; pdb.set_trace()
                for value in filtered_heros_id:
                    # import pdb; pdb.set_trace()
                    if value in hero_pick:
                        # import pdb; pdb.set_trace()
                        file.write('1,')
                        hero_pick.remove(value)
                    else:
                        file.write('0,')
                file.write('{0},'.format(len(hero_pick))) #if hero_pick has anything left in it, that's the number of low picked heros
                file.write(str(outcome))
                file.write('\n')
                hero_pick = []
                current_match_id += 1

    import pdb; pdb.set_trace()

    #change the 2nd line to match
    with open('hero_pick_outcomes.csv', 'r') as file:
        data = file.readlines()
    # with open('hero_pick_outcomes.csv' , 'w') as file:
    #     line2 =
    import pdb; pdb.set_trace()
    print('hello')