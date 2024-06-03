#!/bin/bash
#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

# URL du fichier à télécharger
URL="https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q3_K_S.gguf?download=true"

# Nom du fichier de sortie
OUTPUT="llama2.gguf"

# Utiliser curl pour télécharger le fichier
curl -L -o $OUTPUT $URL

echo "Téléchargement terminé : $OUTPUT"