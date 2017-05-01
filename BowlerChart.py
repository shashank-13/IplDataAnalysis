import yaml
import cPickle
import glob

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def getAnswer(team,rootPath):
    dict={team:[0,0,0,0,0]}
    string = "Royal Challengers Bangalore"
    for filepath in glob.glob(rootPath + "/*.yaml"):
        data = yaml_loader(filepath)
        list_data_bowler = []
        for key in data['innings']:
            for temp, temp1 in key.iteritems():
                if temp1.get('team') != string:
                    list_data_bowler = temp1.get('deliveries')
                    break

        counter = 0
        for key in list_data_bowler:
            bowler_key = key[key.keys()[0]].get('bowler')
            if (key[key.keys()[0]].get('runs').get('extras') == 0) or (
                    key[key.keys()[0]].get('runs').get('extras') != 0 and key[key.keys()[0]].get('runs').get(
                    'batsman') == 0):
                counter += 1
            if (bowler_key == team):
                if key[key.keys()[0]].has_key('wicket') and key[key.keys()[0]].get('wicket').get('kind') != 'run out':
                    index = counter / 24
                    if(index>4):
                        index-=1
                    dict[team][index] += 1


    print dict
    return dict