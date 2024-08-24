import json
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

def extract_comments(video_id):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
	developerKey=DEVELOPER_KEY)
	comment_item = {}
	try:
		request = youtube.commentThreads().list(
			part="snippet",
			videoId=video_id,
			maxResults=100
		)
		response = request.execute()
		for comment_thread in response.get('items', []):
			comment = comment_thread['snippet']['topLevelComment']['snippet']
			comment_item = {
				'videoId': video_id,
				'created_at': comment['publishedAt'],
				'comment': comment['textDisplay']
			}
	except HttpError as e:
		error_message = json.loads(e.content)['error']['message']
		if 'disabled comments' in error_message:
			print(
				f"I commenti sono disabilitati per il video con ID '{video_id}'.")
		else:
			print(
				f"Errore durante il recupero dei commenti per il video con ID '{video_id}':", error_message)
	return comment_item