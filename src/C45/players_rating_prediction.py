import pandas as pd
from collections import defaultdict

if __name__ == '__main__':


    df_match = pd.read_csv('match.csv')
    # df_match_outcome = pd.read_csv('match_outcomes.csv')
    df_players = pd.read_csv('players.csv')
    df_players_rating = pd.read_csv('player_ratings.csv')

    match_id = df_match['match_id'].values
    radiant_win = df_match['radiant_win'].values

    player_rating = {}
    for index, row in df_players_rating.iterrows():
        rate = row['trueskill_mu']
        id = row['account_id']
        player_rating[id] = rate


    match_radiant_win = {}
    heroes = {}
    for index, match in enumerate(match_id):
        match_radiant_win[match] = radiant_win[index]



    current_match_id = 0
    distinct_heroes = defaultdict(set)

    # import pdb; pdb.set_trace()



    current_team_rating = 0
    count = 0
    predicted_radiant_win = []
    for index, row in df_players.iterrows():
        m_id = row['match_id']
        outcome = radiant_win[m_id]
        account_id = row['account_id']
        if account_id != 0 and account_id in player_rating:

            count += 1
            current_team_rating += player_rating[account_id]

        if (index + 1) % 10 == 0: #time to compare result of the mmr of players on both team:
            if count != 0:
                dyre_team = current_team_rating / count
            current_team_rating = 0
            count = 0
            if dyre_team > radiant_team:
                predicted_radiant_win.append(False)
            else:
                predicted_radiant_win.append(True)


        elif (index + 1) % 5 == 0: #time to write result since it's five heroes already
            if count != 0:
                radiant_team = current_team_rating / count
            current_team_rating = 0
            count = 0
            # if current_match_id % 2 == 1:  # this is dyre team
            #     outcome = not outcome

        current_match_id += 1
    correct_classified = 0
    i = 0
    while i < len(predicted_radiant_win):
        if predicted_radiant_win[i] == radiant_win[i]:
            correct_classified += 1
        i += 1

    y_actu = pd.Series(radiant_win, name='Actual')
    y_pred = pd.Series(predicted_radiant_win, name='Predicted')
    df_confusion = pd.crosstab(y_actu, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)

    print(df_confusion)

    print('Total Number Of Records Classified: ', len(predicted_radiant_win))
    print('Total Number Of Records Correctly Classified: ', correct_classified)
    print('Total number of records Incorrectly Classified: ', len(predicted_radiant_win) - correct_classified)
    print('Overall accuracy and error rate of the classifier: ', correct_classified/len(predicted_radiant_win) * 100, '%')
