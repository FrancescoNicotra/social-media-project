import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
from googleExample import youtube_search
import os
from extract_audio import extract_audio
from readVideosTitle import leggi_titoli_video
from trans import transcribe_audio

# Dove salvare
SAVE_PATH = os.path.expanduser("~/Desktop/Facial-Emotion-Recognition\ base")

def create_link(videoIds):
	links = []
	for videoId in videoIds:
		print(f"Processing video ID: {videoId}")
		link = f"https://www.youtube.com/watch?v={videoId}"
		links.append(link)
	return links

def download_youtube_video(url, save_path='.'):
	try:
		print(f"Attempting to download video from URL: {url}")
		yt = YouTube(url, on_progress_callback = on_progress)

		ys = yt.streams.get_highest_resolution()
		ys.download(output_path='./videos')

	except Exception as e:
		print(f"Errore durante il download: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--q', help='Search term', default='Google')
	parser.add_argument('--max-results', help='Max results', default=5)
	args = parser.parse_args()

	videoIds = youtube_search(args)
	print(f"Video IDs: {videoIds}")

	# Links dei video da scaricare
	links = create_link(videoIds)
	print(f"Links: {links}")

	# Scarica i video dalla lista
	for link in links:
		download_youtube_video(link, SAVE_PATH)
	video_titles = leggi_titoli_video()

	for video_title in video_titles:
		extract_audio('./videos/' + video_title.replace(' ', '_') + '.mp4', './audio/' + video_title + '.wav')
	for video_title in video_titles:
		transcribe_audio('./audio/' + video_title + '.wav', './transcriptions/' + video_title + '.csv')