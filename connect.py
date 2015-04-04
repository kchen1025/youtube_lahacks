import json
import urllib.request
import urllib.parse
from pprint import pprint


API_KEY = 'AIzaSyB2nClBJR9aP5clL6c15uIkPhJACccZmOM'
URL = 'https://www.googleapis.com/youtube/v3/videos?id='
TEST_URL = 'http://gdata.youtube.com/feeds/api/videos/9bZkp7q19f0/comments?orderby=published&alt=json&max-results=30&start-index=1'
#TEST_URL = 'http://gdata.youtube.com/feeds/api/videos/91lYBbBkftA/comments?orderby=published&alt=json&max-results=30&start-index=1'
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



    
    