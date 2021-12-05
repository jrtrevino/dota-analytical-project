import pandas as pd
from collections import defaultdict

if __name__ == '__main__':


    df_match = pd.read_csv('match.csv')
    # df_match_outcome = pd.read_csv('match_outcomes.csv')
    df_players = pd.read_csv('players.csv')

    match_id = df_match['match_id'].values
    radiant_win = df_match['radiant_win'].values
    match_radiant_win = {}
    for index, match in enumerate(match_id):
        match_radiant_win[match] = radiant_win[index]


    current_match_id = 0
    distinct_heroes = defaultdict(set)

    import pdb; pdb.set_trace()
    with open('hero_pick_outcomes.csv', 'w') as file:
        file.write('match_id,hero1,hero2,hero3,hero4,hero5,outcome\n')
        file.write('-1,0,0,0,0,0,2\n')
        file.write('outcome\n')
        hero_pick = []
        for index, row in df_players.iterrows():
            m_id = row['match_id']
            hero = row['hero_id']
            hero_pick.append(hero)
            outcome = radiant_win[m_id]
            distinct_heroes[(index + 1) % 5].add(hero)

            if (index + 1) % 5 == 0: #time to write result since it's five heroes already
                if current_match_id % 2 == 1:  # this is dyre team
                    outcome = not outcome
                hero_pick = map(str, hero_pick)
                str_out = str(current_match_id) + ',' + ','.join(hero_pick) + ',' + str(outcome)
                file.write(str_out)
                file.write('\n')
                hero_pick = []
                current_match_id += 1



    #change the 2nd line to match
    with open('hero_pick_outcomes.csv', 'r') as file:
        data = file.readlines()
    # with open('hero_pick_outcomes.csv' , 'w') as file:
    #     line2 =
    import pdb; pdb.set_trace()
    print('hello')