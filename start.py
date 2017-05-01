import json

def json_loader(filepath):
	with open(filepath,"r") as file_descriptor:
		data=json.load(file_descriptor)
	return data

def Batstats(teamname):
    batsman_dict = json_loader(teamname + "\\" +teamname +"stats_batsman.txt")
    batsman_list = []
    for key, value in batsman_dict.iteritems():
        temp_list = [key, value]
        batsman_list.append(temp_list)

    batsman_list = sorted(batsman_list, key=lambda x: x[1], reverse=True)

    '''for i in xrange(10):
        print "Name {0}   Runs {1}  ".format(batsman_list[i][0], batsman_list[i][1])'''
    return batsman_list


def BowlStats(teamname):
    bowlers_dict = json_loader(teamname + "\\" +teamname +"stats_bowler.txt")
    bowlers_list = []
    for key, value in bowlers_dict.iteritems():
        temp_list = [key, value]
        bowlers_list.append(temp_list)

    bowlers_list = sorted(bowlers_list, key=lambda x: x[1], reverse=True)

    '''for i in xrange(10):
        print "Name {0}   Wicket {1}  ".format(bowlers_list[i][0], bowlers_list[i][1])'''
    return bowlers_list


def FieldStats(teamname):


    fielders_dict=json_loader(teamname + "\\" +teamname +"stats_fielders.txt")
    fielders_list=[]

    for key,value in fielders_dict.iteritems():
        temp_list=[key,value]
        fielders_list.append(temp_list)

    fielders_list=sorted(fielders_list,key= lambda  x:x[1],reverse=True)

    '''for i in xrange(10):
        print "Name {0} Run-outs {1}".format(fielders_list[i][0],fielders_list[i][1])'''
    return fielders_list
