import connect
import re
from collections import defaultdict

reg_ex = '(.*[0-9]{1,2}:[0-9][0-9].*)'

class algorithm:
    def __init__(self,timestamps: [str]):
        self.timestamps = timestamps

    


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
    for i in range(30):
        try:
            #api has strange format so i catch the error and pass it.
            #not good format
            json2 = connect.generate_json(gurl)
            for i in parse_currpage(json2):
                print(i)
                glist.append(i)
            gurl = connect.next_url(json2)
        except IndexError:
            print("error print output")
            
    print(glist)
    print(len(glist))
    