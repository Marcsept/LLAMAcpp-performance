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
import gzip
import shutil

def compresser_csv_gzip(nom_fichier_csv, nom_fichier_gzip):
    with open(nom_fichier_csv, 'rb') as f_in:
        with gzip.open(nom_fichier_gzip, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(nom_fichier_csv)


def extract_data(fichier) :
    out = "name;operation;DimX;DimY;DimZ;mat\n"
    fichier_ = fichier.split("/")[-1][:-8]+".csv"
    
    try:
        with open("aggregations/NeuralNetwork/"+fichier_, "a") as f:
            f.write(out)
            with open(fichier, 'r', encoding='utf-8') as file:
                contenu = file.read()
                #print(contenu)    
                contenu_ligne = contenu.split("\n")
                nb_ligne_global = len(contenu_ligne)
                it_ligne = 0
                while (it_ligne < nb_ligne_global):
                    #print(str(it_ligne+1) + " / " + str(nb_ligne_global))
                    #print(contenu_ligne[it_ligne])
                    if("Log_data :" in contenu_ligne[it_ligne]):
                        ligne_split = contenu_ligne[it_ligne].split(":")
                        ligne = str(ligne_split[1])+";"+str(ligne_split[6])+";"+str(ligne_split[2])+";"+str(ligne_split[3])+";"+str(ligne_split[4])+";"
                        data = []
                        nb_block = int (ligne_split[4])
                        nb_ligne = int (ligne_split[3])
                        for _ in range(nb_block) :
                            data_block = []
                            for _ in range(int(nb_ligne)):
                                it_ligne += 1
                                data_ligne = []
                                ligne_split = contenu_ligne[it_ligne].split("|")
                                for i in ligne_split[1:-1]:
                                    data_ligne.append(float (i))
                                data_block.append(data_ligne)
                            data.append(data_block)
                        ligne += str(data) + "\n"
                        #with open("aggregations/NeuralNetwork/"+fichier_, "a") as f:
                        f.write(ligne)
                    else : 
                        it_ligne += 1    
            #
            # Active or not the compressions divis by 3 the size. 
            #
            #compresser_csv_gzip("aggregations/NeuralNetwork/"+fichier_, "aggregations/NeuralNetwork/"+fichier_+".gz" )           
            return 
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except IOError:
        print(f"Erreur lors de la lecture du fichier {fichier}.")
    
    return        
        
   
            
            
            
            
    



def main():
    out = ""

    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(description='Path of the file to aggregate')
    
    # Ajouter un argument
    parser.add_argument('Path', type=str, help='Path (ex : ../file1/file2/file_to_aggregate')
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Liste pour stocker les noms de fichiers .txt
    
    # Parcourir le dossier donné (Log run time)
    for fichier in os.listdir(str(args.Path)):
        if fichier.endswith('.txt'):
           extract_data(args.Path + "/" + fichier)

    
    
    

if __name__ == '__main__':
    main()
    