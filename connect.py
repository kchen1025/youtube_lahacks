import json
import urllib.request
import urllib.parse
from pprint import pprint


API_KEY = 'AIzaSyB2nClBJR9aP5clL6c15uIkPhJACccZmOM'
URL = 'https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id='
TEST_URL = 'http://gdata.youtube.com/feeds/api/videos/'
COMMENT_REQUEST = '/comments?orderby=published&alt=json&max-results=30&start-index=1'
#TEST_URL = 'http://gdata.youtube.com/feeds/api/videos/91lYBbBkftA/comments?orderby=published&alt=json&max-results=30&start-index=1'
VIDEO_ID = 'WczKOeAqkf8' 


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

def pull_video_time(json_file:'json')->int:
    temp = json_file['items'][0]['contentDetails']['duration'][2:]
    
    counter = 0
    duration = 0
    for cur_char in temp[::-1]:
        if(counter % 3 == 0):
            counter += 1
            continue
        duration += pow(60,int(counter / 3))*( 10 if ((counter+1) % 3) == 0 else 1 )* int(cur_char)
        counter += 1

    return duration


    
    
