#!/bin/bash

# Initialiser les variables globales pour la barre de chargement
progress=0
bar_length=50

# Définir la fonction de barre de chargement
update_loading_bar() {
  local total_steps=$1
  local current_step=$2
  local bar_fill=$((current_step * bar_length / total_steps))
  local empty_space=$((bar_length - bar_fill))
  local percentage=$((current_step * 100 / total_steps))
  
  # Construire la barre de chargement
  local bar=""
  local i=0
  while [ $i -lt $bar_fill ]; do
    bar="${bar}#"
    i=$((i + 1))
  done

  i=0
  while [ $i -lt $empty_space ]; do
    bar="${bar} "
    i=$((i + 1))
  done
  
  # Afficher la barre de chargement
  echo -ne "\r[${bar}] $percentage% "
}

# Exemple d'utilisation dans un script
#total_steps=100
#  update_loading_bar $total_steps $i


