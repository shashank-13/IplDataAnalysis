import yaml
import glob


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def getAnswer(team,rootPath):
    dict={team:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    strike = {team:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    string = "Royal Challengers Bangalore"
    for filepath in glob.glob(rootPath + "/*.yaml"):
        data = yaml_loader(filepath)
        list_data_batsman = []
        for key in data['innings']:
            for temp, temp1 in key.iteritems():
                if temp1.get('team') == string:
                    list_data_batsman = temp1.get('deliveries')
                    break

        counter=0
        for key in list_data_batsman:
            batsman_key = key[key.keys()[0]].get('batsman')
            if (batsman_key==team):
                if (key[key.keys()[0]].has_key('wicket') and key[key.keys()[0]].get('wicket').get('kind') != 'run out') or (key[key.keys()[0]].has_key('wicket') and key[key.keys()[0]].get('wicket').get('kind') == 'run out' and key[key.keys()[0]].get('wicket').get('player_out') == team):
                    break
                else:
                    if (key[key.keys()[0]].get('runs').get('extras') == 0) or (key[key.keys()[0]].get('runs').get('extras') != 0 and key[key.keys()[0]].get('runs').get('batsman') == 0):
                        counter+=1
                    runs=key[key.keys()[0]].get('runs').get('batsman')
                    index=counter/6
                    dict[team][index]+=runs
                    strike[team][index]+=1






    dict[team]=remove_values_from_list(dict[team],0)
    strike[team]=remove_values_from_list(strike[team],0)
    temp_list=[]
    for i in xrange(len(dict[team])):
        x=(dict[team][i]*100.0)/(strike[team][i]*1.0)
        temp_list.append(round(x,2))
    dict[team+"_strike"]=temp_list

    print dict
    return dict
