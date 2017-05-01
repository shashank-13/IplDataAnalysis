import yaml
import getStats
import getDictionary
import start
import json


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def dumpJson(filepath, data):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)


def json_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = json.load(file_descriptor)
    return data


def dumpFile(teamName, rootpath):
    top_stats = getStats.getStatistics("ReducedData" + teamName + "\\")
    batsman_dict, bowlers_dict, fielders_dict = getDictionary.returnDictionary(rootpath)

    dumpJson(teamName + "\\" + teamName + "top_stats.txt", top_stats)

    dumpJson(teamName + "\\" + teamName + "stats_batsman.txt", batsman_dict)

    dumpJson(teamName + "\\" + teamName + "stats_bowler.txt", bowlers_dict)

    dumpJson(teamName + "\\" + teamName + "stats_fielders.txt", fielders_dict)

    batsman_list_chart = start.Batstats(teamName)
    bowlers_list_chart = start.BowlStats(teamName)
    fielders_list_chart = start.FieldStats(teamName)

    dumpJson(teamName + "\\" + teamName + "top_stats_batsman.txt", batsman_list_chart)

    dumpJson(teamName + "\\" + teamName + "top_stats_bowler.txt", bowlers_list_chart)

    dumpJson(teamName + "\\" + teamName + "top_stats_fielders.txt", fielders_list_chart)




    # start.showStats()
