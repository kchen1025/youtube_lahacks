import connect
import re
from collections import defaultdict


reg_ex = '(.*[0-9]{1,2}:[0-9][0-9].*)'


class algorithm:
    def __init__(self,timestamps: [str]):
        self.timestamps = timestamps

    def sort_timestamps(self):
        timestamps = self.timestamps.copy()
        for count,times in enumerate(timestamps,start=0):
            if len(times) == 4:
                timestamps[count] = '0' + times
        self.timestamps = sorted(timestamps)
        
    def algorithm(self):
        at_start_of_tup = True
        timestamps = self.timestamps
        value = timestamps[0]
        for count,times in enumerate(timestamps,start = 0):
            if(at_start_of_tup):
                tup = ()

    
#parses the current webpage for comments 
def parse_currpage(json_file: 'json')-> [str]:
    time_stamps = []
    #FIX THIS LATER ####################################
    ####################################################
    for comment in range(28):
        try:
            match = re.match(reg_ex, json_file['feed']['entry'][comment]['content']['$t'])
            if match:
                #printing regex match for the timestamp in youtube comments 
                time_stamps.append(re.search(r'([0-9]{1,2}:[0-9][0-9])',match.string).group(0))
        except IndexError:
            print("error move on")
    return time_stamps


if __name__ == '__main__':
    gurl = connect.TEST_URL
    glist = []
    
    #30 is just an arbitrary number until i figure out how to do this properly 
    for i in range(10):
        try:
            #api has strange format so i catch the error and pass it.
            #not good format
            json2 = connect.generate_json(gurl)
            for i in parse_currpage(json2):
                glist.append(i)
            gurl = connect.next_url(json2)
        except IndexError:
            print("error print output")
            
            
    a = algorithm(glist)
    a.sort_timestamps()
            
