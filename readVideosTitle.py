import os

def leggi_titoli_video(directory='./videos') -> list[str]:
    # Verifica che la cartella esista
    if not os.path.exists(directory):
        raise FileNotFoundError(f"La cartella {directory} non esiste.")
    # Verifica che la cartella non sia vuota
    if not os.listdir(directory):
        raise FileNotFoundError(f"La cartella {directory} è vuota.")

    # Lista per contenere i titoli dei video
    titoli_video = []

    # Estensioni video comuni
    estensioni_video = ('.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.m4v')

    # Itera su tutti i file nella cartella
    for filename in os.listdir(directory):
        # Controlla se il file ha un'estensione video
        if filename.lower().endswith(estensioni_video):
            # Sostituisce gli spazi nel nome del file con '_'
            nuovo_nome = filename.replace(' ', '_')
            # Rinomina il file nella cartella
            os.rename(os.path.join(directory, filename), os.path.join(directory, nuovo_nome))
            # Aggiungi il nome del file senza estensione alla lista
            titolo, _ = os.path.splitext(nuovo_nome)
            titoli_video.append(titolo)

    return titoli_video
