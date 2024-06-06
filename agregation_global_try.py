#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================



import sys
import pandas as pd 
import os

    return "try" in string

def datanalyse(df, name_option):
    #Calcule mean_load_time
    mean_load_time = df['load_time'].str.replace("ms", "").astype(float).mean()
    #Calcule mean_sample_token_per_seconde
    mean_sample_token_per_seconde = df['token_per_sec'].astype(float).mean()
    #Calcule mean_prompt_eval_time_token_per_seconde
    mean_prompt_eval_time_token_per_seconde = df['token_per_sec.1'].astype(float).mean()
    #Calcule mean_eval_time_token_per_seconde
    mean_eval_time_token_per_seconde = df['token_per_sec.2'].astype(float).mean()
    #Calcule mean_total_time_token_per_seconde
    mean_total_time_token_per_seconde=0
    step1_mean_total_time_token_per_seconde= df['total_time'].str.replace("ms", "").str.replace("tokens","")
    step2_mean_total_time_token_per_seconde = [x.split("/") for x in step1_mean_total_time_token_per_seconde]
    step3_mean_total_time_token_per_seconde = [ 1000 / (float(x[0]) / float(x[1])) for x in step2_mean_total_time_token_per_seconde]
    for x in step3_mean_total_time_token_per_seconde :
        mean_total_time_token_per_seconde += x
    if( mean_total_time_token_per_seconde == 0 ):
        mean_total_time_token_per_seconde = 0
    else :
        mean_total_time_token_per_seconde = mean_total_time_token_per_seconde / len(step3_mean_total_time_token_per_seconde)
    
    
    return [name_option,
            round(mean_load_time,3),
            round(mean_sample_token_per_seconde,3),
            round(mean_prompt_eval_time_token_per_seconde,3),
            round(mean_eval_time_token_per_seconde,3),
            round(mean_total_time_token_per_seconde,3)]

def stock(model,tab):
    to_write = ""
    for i in tab:
        to_write+= str(i) + ";"
    to_write = to_write[:-1]+"\n"
    with open(model+'_summerize.csv', 'a') as fichier:
        fichier.write(to_write)
        
def preparation_data(model,dataFrame, name_option):
    stock(model, datanalyse(dataFrame, name_option))

def main(arg1, arg2):
    model = "aggregations/"+arg1
    option_name = arg2
    
    csv=model+"_test_input_"+option_name+"_aggregation.csv"
    #option locally typical sampling: 0 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(trys)]
    name_option = option_name
    preparation_data(model,df,name_option)
 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <argument>")
    else:
        main(sys.argv[1], sys.argv[2])