#==============================================================================
# Script Name: move_state.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================


import argparse
import sys
import pandas as pd 
import os
import shutil

def move_files(file_paths, destination_folder):
    """
    Déplace des fichiers vers un dossier de destination.

    :param file_paths: Liste des chemins des fichiers à déplacer.
    :param destination_folder: Chemin du dossier de destination.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_path in file_paths:
        if os.path.isfile(file_path):
            shutil.move(file_path, destination_folder)
        else:
            print(f"Le fichier {file_path} n'existe pas.")

def rename_folder(current_folder_path, new_folder_name):
    """
    Renomme un dossier.

    :param current_folder_path: Chemin du dossier actuel.
    :param new_folder_name: Nouveau nom du dossier.
    """
    if os.path.isdir(current_folder_path):
        parent_dir = os.path.dirname(current_folder_path)
        new_folder_path = os.path.join(parent_dir, new_folder_name)
        os.rename(current_folder_path, new_folder_path)
    else:
        print(f"Le dossier {current_folder_path} n'existe pas.")


def main(arg):
    
    
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description='Path of the file to aggregate')
    
    # Ajouter un argument
    parser.add_argument('Path', type=str, help='Path (ex : ../file1/file2/file_to_aggregate')
     # Ajouter un argument
    parser.add_argument('Input', type=str, help='input (ex : input1')
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Liste pour stocker les noms de fichiers .txt
    fichiers_txt = []
    
    Path_state = "../State/"
    # Parcourir le dossier donné
    for fichier in os.listdir(Path_state):
        if fichier.endswith('.bin'):
            fichiers_txt.append(fichier)
            
    print(fichiers_txt)
    for i in range(len(fichiers_txt)):
        rename_folder(Path_state+fichiers_txt[i], str(args.Input)[:-4]+".bin")
    move_files(Path_state,str(args.Path))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <argument>")
    else:
        main(sys.argv[1])