import argparse
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load environment variables
load_dotenv('.env')
API_KEY = os.getenv('API_KEY')
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CSV_FILENAME = 'trending_videos.csv'
COUNTRIES = ['IT']  # List of countries to analyze

# authenticate to the API
def get_authenticated_service():
    return build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY, cache_discovery=False)



# This function searches for videos that are associated with a particular Freebase
# topic, logging their video IDs and titles to the Apps Script log. This example uses
# the topic ID for Google Apps Script.
# Note that this sample limits the results to 25. To return more results, pass
# additional parameters as documented here:
# https://developers.google.com/youtube/v3/docs/search/list
def searchByArguments():
	mid = '/m/0gjf126'
	results = YouTube.Search.list('id,snippet', {topicId: mid, maxResults: 25})
	for i in results.items:
		item = results.items[i]
		Logger.log('[%s] Title: %s', item.id.videoId, item.snippet.title)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    youtube = get_authenticated_service()
    try:
        searchByArguments(youtube)
    except HttpError as e:
        print('Si è verificato un errore HTTP %d:\n%s' %
            (e.resp.status, e.content))