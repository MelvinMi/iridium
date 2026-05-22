#!/bin/bash

DIR_EXAMPLES="/home/ubuntu/Desktop/gr-iridium/examples"
PATH_PARSER="/home/ubuntu/Desktop/iridium-toolkit/iridium-parser.py"
DIR_OUTPUT="/home/ubuntu/Desktop/IridiumAcquisition"
#PATH_MY_EXTRACTOR="/home/ubuntu/Desktop/my_extractor.py"


cd "$DIR_EXAMPLES" || { echo "Dossier gr-iridium/examples introuvable."; exit 1; }

mkdir -p "$DIR_OUTPUT"

while true; do

    FILE_DATE=$(date +%d-%m-%Y_%H-%M-%S)

    echo "[$(date '+%H:%M:%S')] Allumage du BladeRF et traitement en continu: "

    iridium-extractor -D 4 bladerf-10msps.conf | \
    python3 "$PATH_PARSER" | \
    tee -a "$DIR_OUTPUT/pipeline_live_${FILE_DATE}.parsed" #| \
    #python3 "$PATH_MY_EXTRACTOR"

    echo "[$(date '+%H:%M:%S')]  Interruption détectée, Ctrl-c ou attendre 10s"
    sleep 10
done



#chmod +x demo_iridium.sh
#./demo_iridium.sh
