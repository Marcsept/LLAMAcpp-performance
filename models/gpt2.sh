#!/bin/bash
#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

# URL du fichier à télécharger
URL="https://huggingface.co/RichardErkhov/openai-community_-_gpt2-medium-gguf/resolve/main/gpt2-medium.IQ4_NL.gguf?download=true"

# Nom du fichier de sortie
OUTPUT="gpt2.gguf"

# Utiliser curl pour télécharger le fichier
curl -L -o $OUTPUT $URL

echo "Téléchargement terminé : $OUTPUT"