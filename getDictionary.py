import yaml
import glob

def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data=yaml.load(file_descriptor)
    return data


def returnDictionary(rootPath):
    string = "Royal Challengers Bangalore"
    batsman_dict = {}
    bowlers_dict = {}
    fielders_dict = {}
    for filepath in glob.glob(rootPath + "/*.yaml"):
        data = yaml_loader(filepath)
        list_data_batsman = []
        list_data_bowler = []
        for key in data['innings']:
            for temp, temp1 in key.iteritems():
                if temp1.get('team') == string:
                    list_data_batsman = temp1.get('deliveries')
                else:
                    list_data_bowler = temp1.get('deliveries')

        for key in list_data_batsman:
            batsman_key = key[key.keys()[0]].get('batsman')
            if batsman_dict.has_key(batsman_key):
                batsman_dict[batsman_key] = batsman_dict[batsman_key] + key[key.keys()[0]].get('runs').get('batsman')
            else:
                batsman_dict[batsman_key] = key[key.keys()[0]].get('runs').get('batsman')

        for key in list_data_bowler:
            bowler_key = key[key.keys()[0]].get('bowler')
            if key[key.keys()[0]].has_key('wicket'):
                if key[key.keys()[0]].get('wicket').get('kind') == 'run out':
                    fielder = key[key.keys()[0]].get('wicket').get('fielders')
                    #print fielder
                    if isinstance(fielder,list):
                        for x in fielder:
                            if fielders_dict.has_key(x):
                                fielders_dict[x] += 1
                            else:
                                fielders_dict[x] = 1
                else:
                    if bowlers_dict.has_key(bowler_key):
                        bowlers_dict[bowler_key] += 1
                    else:
                        bowlers_dict[bowler_key] = 1


    return batsman_dict,bowlers_dict,fielders_dict