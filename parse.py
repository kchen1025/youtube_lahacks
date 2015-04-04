import connect
import re

reg_ex = '(.*[0-9]{1,2}:[0-9][0-9].*)'

#parses the current webpage for comments 
def parse_currpage(json_file: 'json')-> None:
    count = 0
    
    #FIX THIS LATER ####################################
    ####################################################
    for comment in range(28):
        match = re.match(reg_ex, json_file['feed']['entry'][comment]['content']['$t'])
        if match:
            print(match.string)
        count+=1
        print(count)
            


if __name__ == '__main__':
#     test = 'blah blah 0:32 blah'
#     match = re.match(reg_ex,test)
#     print(match.string)

    gurl = connect.TEST_URL
     
    #30 is just an arbitrary number until i figure out how to do this properly 
    for i in range(100):
        json2 = connect.generate_json(gurl)
        parse_currpage(json2)
        gurl = connect.next_url(json2)