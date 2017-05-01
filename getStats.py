import yaml
import glob


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data




def getStatistics(destpath):
    string = "Royal Challengers Bangalore"
    city = "Bangalore"

    matches_won = 0
    matches_lost = 0
    toss_won = 0
    total_played = 0
    decision_field_won = 0
    decision_bat_won = 0
    toss_match_won = 0
    away_win = 0
    home_win = 0
    counter = 0

    for filepath in glob.glob(destpath + "/*.yaml"):
        counter += 1
        data = yaml_loader(filepath)
        if data['outcome'].get('winner') == string:
            matches_won += 1
            if data.get('city') == city:
                home_win += 1
            else:
                away_win += 1
            if data['toss'].get('winner') == string:
                toss_match_won += 1
                toss_won += 1
                if data['toss'].get('decision') == 'field':
                    decision_field_won += 1
                else:
                    decision_bat_won += 1
            else:
                if data['toss'].get('decision') == 'field':
                    decision_bat_won += 1

                else:
                    decision_field_won += 1

        else:
            matches_lost += 1
            if data['toss'].get('winner') == string:
                toss_won += 1

        total_played += 1
    data_list={}
    data_list['Matches played :']=total_played
    data_list['Matches Won :']= matches_won
    data_list['Matches Lost :']=matches_lost
    data_list['Toss Win :']=toss_won
    data_list['Toss win Conversion :']=toss_match_won
    data_list['Home Win :']=home_win
    data_list['Away Win :']=away_win
    return data_list


'''print " Matches played : {0} Matches Won : {1} Matches Lost : {2}  \n".format(total_played,matches_won,matches_lost)
print " Toss Win : {0} Toss win Conversion : {1} \n".format(toss_won,toss_match_won)
print " Home Win : {0} Away Win {1} \n".format(home_win,away_win)'''


