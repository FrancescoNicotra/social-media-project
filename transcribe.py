import whisper
import pandas as pd



def transcribe_audio(audio_title: str) -> None:
	model = whisper.load_model("base")
	complete_path = './audio/' + audio_title + '.wav'
	csv_path = './transcriptions/' + audio_title + '.csv'
# Carica l'audio completo
	audio = whisper.load_audio(complete_path)

	# Imposta una finestra di 30 secondi (circa 30 * 16000 campioni)
	segment_length = 30 * whisper.audio.SAMPLE_RATE

	transcription = []
	# Cicla su segmenti di 30 secondi
	for i in range(0, len(audio), segment_length):
		segment = whisper.pad_or_trim(audio[i:i + segment_length])

		# Crea lo spettrogramma e decodifica il segmento
		mel = whisper.log_mel_spectrogram(segment).to(model.device)
		_, probs = model.detect_language(mel)
		print(f"Detected language in segment {i//segment_length}: {max(probs, key=probs.get)}")

		options = whisper.DecodingOptions(fp16 = False)
		result = whisper.decode(model, mel, options)

		# Aggiungi il testo alla trascrizione completa
		transcription.append(result.text)
		# Unisci tutti i segmenti in un'unica stringa
	full_transcription = " ".join(transcription)
	# Crea un DataFrame con una sola riga
	df = pd.DataFrame({'testo': [full_transcription]})

	# Salva il DataFrame nel file CSV
	df.to_csv(csv_path, index=False, encoding='utf-8')
