import BatsmanChart
import BowlerChart
import time
import initial
import yaml
import glob
import result_pickle
import json

def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data=yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
    with open(filepath,"w") as file_Descriptor:
        yaml.dump(data,file_Descriptor)

def json_loader(filepath):
	with open(filepath,"r") as file_descriptor:
		data=json.load(file_descriptor)
	return data

def dumpJson(filepath,data):
	with open(filepath, 'w') as outfile:
		json.dump(data, outfile)

start_time=time.time()
tag="RCB"
rootpath='royal_challengers_bangalore\\'
i=0
for filepath in glob.glob(rootpath + "/*.yaml"):
    i+=1
    data=yaml_loader(filepath)
    yaml_dump("ReducedData" + tag +"\\"+str(i)+".yaml",data['info'])

initial.dumpFile(tag,rootpath)
batsman_list=json_loader(tag +"\\" +tag +"top_stats_batsman.txt")
bowlers_list=json_loader(tag +"\\" +tag +"top_stats_bowler.txt")
list_batsman=[]
list_bowler=[]
for i in xrange(10):
    temp_dict=BatsmanChart.getAnswer(batsman_list[i][0],rootpath)
    list_batsman.append(temp_dict)


dumpJson(tag +"\\" +tag +"top_bats_strike_analyze.txt",list_batsman)



bowlers_list=json_loader(tag +"\\" +tag +"top_stats_bowler.txt")
list_bowler=[]
for i in xrange(10):
    temp_dict=BowlerChart.getAnswer(bowlers_list[i][0],rootpath)
    list_bowler.append(temp_dict)

dumpJson(tag +"\\" +tag +"top_bowlers_strike_analyze.txt",list_bowler)

result_pickle.read(tag)
#start.Batstats("RCB")
#initial.dumpcPickle("RCB")
print("--- %s seconds ---" % (time.time() - start_time))