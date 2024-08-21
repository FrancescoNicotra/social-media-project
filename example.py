from ffpyplayer.player import MediaPlayer
import cv2

def PlayVideo(video_path):
    # Funzione per gestire l'audio
    def get_audio_frame(player):
        audio_frame, val = player.get_frame()
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
        return val

    # Creare un lettore multimediale per il video
    player = MediaPlayer(video_path)

    # Aprire il video con OpenCV
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Visualizza il frame video
        cv2.imshow('Video', frame)

        # Riproduci l'audio
        get_audio_frame(player)

        # Premi 'q' per uscire dalla riproduzione
        if cv2.waitKey(28) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Percorso del video
video_path = './videos/Chris Evans The Puppy Interview.mp4'

# Riproduci il video
PlayVideo(video_path)
