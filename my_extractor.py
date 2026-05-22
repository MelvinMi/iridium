import sys
import json
from datetime import datetime
import time

def process_line(line):

    # On vérifie si c'est une ligne de données Iridium valide

    if not line.startswith("RAW:"):
        return

    # On extrait les infos (ici on fait simple)

    parts = line.split()

    if len(parts) > 5:
        timestamp_sdr = parts[2]
        frequence = parts[3]
        confiance = parts[4]

        # Double horodatage (comme demandé dans le package)

        utc_now = datetime.utcnow().isoformat()
        monotonic_now = time.monotonic()

        # On crée l'objet observation

        observation = {
            "utc_time": utc_now,
            "monotonic_time": monotonic_now,
            "sdr_timestamp": timestamp_sdr,
            "frequency": frequence,
            "confidence": confiance
        }

        #  On écrit dans le fichier log JSON
        # (L'option 'a' veut dire 'append' : on ajoute à la fin du fichier)
        with open("logs/parsed/live_observations.json", "a") as f:
            f.write(json.dumps(observation) + "\n")


if __name__ == "__main__":

    for line in sys.stdin:
        process_line(line.strip())
