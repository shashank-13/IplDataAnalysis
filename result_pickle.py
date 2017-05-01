import json


def json_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = json.load(file_descriptor)
    return data


def read(path):
    summary_chart = json_loader(path + "\\" + path + "top_stats.txt")
    print summary_chart
    print "\n\n\n"

    batsman_list = json_loader(path + "\\" + path + "top_stats_batsman.txt")
    for i in xrange(10):
        print "Name {0}   Runs {1}  ".format(batsman_list[i][0], batsman_list[i][1])

    print "\n\n\n"

    bowlers_list = json_loader(path + "\\" + path + "top_stats_bowler.txt")
    for i in xrange(10):
        print "Name {0}   Wicket {1}  ".format(bowlers_list[i][0], bowlers_list[i][1])
    print "\n\n\n"

    fielders_list = json_loader(path + "\\" + path + "top_stats_fielders.txt")
    for i in xrange(10):
        print "Name {0} Run-outs {1}".format(fielders_list[i][0], fielders_list[i][1])
    print "\n\n\n"

    final_batsman = json_loader(path + "\\" + path + "top_bats_strike_analyze.txt")
    for x in final_batsman:
        print x
    print "\n\n\n"

    final_bowler = json_loader(path + "\\" + path + "top_bowlers_strike_analyze.txt")
    for x in final_bowler:
        print x
