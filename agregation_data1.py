# -*- coding: utf-8 -*-
#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================



import argparse
import os
import pandas as pd


def extract_data(fichier) :
    out = []

    try:
        with open(fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
            #print(contenu)
            
            contenu_ligne = contenu.split("\n")
            for line in contenu_ligne: 
                line_split = line.split()
                if("llama_print_timings:" in line_split):
                    if(len(line_split) > 11): 
                        line_split = line.split('(')
                        #print(line_split)
                        egale = False
                        value_at_add = ""
                        #print(line_split)
                        for i in line_split[0].split() :
                            if(egale):
                                value_at_add += i
                            else :
                                egale = i == '='
                        out.append(value_at_add)
                        out.append(line_split[1].split()[0])
                        out.append(line_split[1].split()[4])
                    else : 
                        egale = False
                        value_at_add = ""
                        #print(line_split)
                        for i in line_split :
                            if(egale):
                                value_at_add += i
                            else :
                                egale = i == '='
                        out.append(value_at_add)

            return out
            
            
            
            
            
            
            
            
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except IOError:
        print(f"Erreur lors de la lecture du fichier {fichier}.")
    
    return 1



def main():
    colone = [
    'load_time',
    'sample_time', 'ms_per_token','token_per_sec',
    'prompt_eval_time','ms_per_token','token_per_sec',
    'eval_time', 'ms_per_token','token_per_sec',
    'total_time',
    'name_'
]
    out = ""
    for i in range(len(colone)-1):
        out += colone[i] + ";"
    out+= colone[-1] +"\n"

    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description='Path of the file to aggregate')
    
    # Ajouter un argument
    parser.add_argument('Path', type=str, help='Path (ex : ../file1/file2/file_to_aggregate')
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Liste pour stocker les noms de fichiers .txt
    fichiers_txt = []
    
    # Parcourir le dossier donné
    for fichier in os.listdir(str(args.Path)):
        if fichier.endswith('.txt'):
            fichiers_txt.append(fichier)
            tab_data = extract_data(args.Path + "/" + fichier)
            for i in range(len(tab_data)-1):
                out += tab_data[i] + ";"
            out+= tab_data[-1] +";"
            out+= fichier + "\n"
    with open("aggregations/"+args.Path.split("/")[1]+ "_aggregation.csv", "w") as f:
        f.write(out)
    

if __name__ == '__main__':
    main()
    