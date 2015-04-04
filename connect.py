import json
import urllib.request
import urllib.parse
from pprint import pprint


API_KEY = 'AIzaSyB2nClBJR9aP5clL6c15uIkPhJACccZmOM'
URL = 'https://www.googleapis.com/youtube/v3/videos?id='
TEST_URL = 'http://gdata.youtube.com/feeds/api/videos/91lYBbBkftA/comments?orderby=published&alt=json&max-results=30&start-index=1'
VIDEO_ID = '91lYBbBkftA' 


def get_result(url: str)-> 'json':
    '''takes the url from build_url and generates json from it'''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def next_url(json_file:'json')->str:
    return json_file['feed']['link'][3]['href']


def generate_json(url:str)-> 'json':
    '''take in the url and return the json file that it retrieves'''  
    result = get_result(url)
    return result


#parses the current webpage for comments 
def parse_currpage(json_file: 'json')-> None:
    count = 0
    
    #FIX THIS LATER ####################################
    ####################################################
    for comment in range(29):
        print(json_file['feed']['entry'][comment]['content']['$t'])
        count += 1
        print(count)



if __name__ == '__main__':
    gurl = TEST_URL
    for i in range(30):
        json2 = generate_json(gurl)
        parse_currpage(json2)
        gurl = next_url(json2)
    
    