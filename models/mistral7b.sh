#!/bin/bash
#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

# URL du fichier à télécharger
URL="https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q2_K.gguf?download=true"

# Nom du fichier de sortie
OUTPUT="mistral7B.gguf"

# Utiliser curl pour télécharger le fichier
curl -L -o $OUTPUT $URL

echo "Téléchargement terminé : $OUTPUT"