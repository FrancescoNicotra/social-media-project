import argparse
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Load environment variables
load_dotenv('.env')
DEVELOPER_KEY = os.getenv('API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options = None):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
		q=options.q,
		part='id,snippet',
		maxResults=options.max_results
	).execute()

	videos = []

	# Add each result to the appropriate list, and then display the lists of
	# matching videos, channels, and playlists.
	for search_result in search_response.get('items', []):
		if search_result['id']['kind'] == 'youtube#video':
			videos.append('%s' % search_result['id']['videoId'])
	return videos


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--q', help='Search term', default='Google')
	parser.add_argument('--max-results', help='Max results', default=25)
	args = parser.parse_args()

	try:
		youtube_search(args)
	except HttpError as e:
		print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))