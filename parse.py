import connect
import re
from collections import defaultdict, OrderedDict
import time_convert as tc

reg_ex = '(.*[0-9]{1,2}:[0-9][0-9].*)'
video_duration = 0 

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
        d = defaultdict(int)
        at_start_of_tup = True
        t = tc.time(self.timestamps)
        timestamps = t.to_seconds()
        
        for time in timestamps:
            if at_start_of_tup:
                tup = (time,time+3)
                d[tup] += 1
                at_start_of_tup = False
            elif time in range(tup[0],tup[1]+4):
                d[tup] += 1
            else:
                at_start_of_tup = True
                
        o =  OrderedDict(sorted(d.items(),key = lambda t:t[1],reverse = True))
        #o = OrderedDict(sorted(d.items(),key = lambda t:t[0]))
        num_highlights = int(video_duration/60)
        highlights_list = []

        for key in o:
            highlights_list.append(key)
            if len(highlights_list) == num_highlights:
                break
            

        new_list = [i for i in sorted(highlights_list, key=lambda highlights:highlights[0])]
        
        return new_list
    
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
    gurl = connect.TEST_URL + connect.VIDEO_ID + connect.COMMENT_REQUEST
    glist = []

    url = connect.URL
    json2 = connect.generate_json(url + connect.VIDEO_ID + "&key=" + connect.API_KEY)
    video_duration = connect.pull_video_time(json2)
    
    #30 is just an arbitrary number until I figure out how to do this properly 
    for i in range(10):
        try:
            #api has strange format so I catch the error and pass it.
            json2 = connect.generate_json(gurl)
            for i in parse_currpage(json2):
                glist.append(i)
            gurl = connect.next_url(json2)
        except IndexError:
            print("error print output")
            
            
    a = algorithm(glist)
    a.sort_timestamps()
    print(a.algorithm())
    
    
            
