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
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    ).execute()

    # Lista per contenere i commenti del video corrente
    video_comments = []

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]

        # Aggiungi il commento alla lista dei commenti
        video_comments.append({
            "author": author,
            "text": text
        })

    # Ritorna un dizionario con l'ID del video e i suoi commenti
    return {
        "video_id": video_id,
        "comments": video_comments
    }

comments_json = []