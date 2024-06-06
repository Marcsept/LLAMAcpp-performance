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

def f32(string):
    return "_f32_" in string
def f16(string):
    return "_f16_" in string

def n(string):
    return "att_n_" in string
def w(string):
    return "att_w_" in string
def nw(string):
    return "att_w_n" in string

def zero(string):
    return "_0_" in string
def twenty(string):
    return "_20_" in string
def all_(string):
    return "_all_" in string

def one(string):
    return "_01_" in string
def ten(string):
    return "_05_" in string
def thirty(string):
    return "_99_" in string


def _mirostat1_br002_ent15(string):
    return "_mirostat1_br002_ent15" in string
def _mirostat1_br002_ent2(string):
    return "_mirostat1_br002_ent2" in string
def _mirostat1_br002_ent5(string):
    return "_mirostat1_br002_ent5" in string
def _mirostat1_br002_ent8(string):
    return "_mirostat1_br002_ent8" in string

def _mirostat1_br02_ent15(string):
    return "_mirostat1_br02_ent15" in string
def _mirostat1_br02_ent2(string):
    return "_mirostat1_br02_ent2" in string
def _mirostat1_br02_ent5(string):
    return "_mirostat1_br02_ent5" in string
def _mirostat1_br02_ent8(string):
    return "_mirostat1_br02_ent8" in string

def _mirostat1_br05_ent15(string):
    return "_mirostat1_br05_ent15" in string
def _mirostat1_br05_ent2(string):
    return "_mirostat1_br05_ent2" in string
def _mirostat1_br05_ent5(string):
    return "_mirostat1_br05_ent5" in string
def _mirostat1_br05_ent8(string):
    return "_mirostat1_br05_ent8" in string


def _mirostat2_br002_ent15(string):
    return "_mirostat2_br002_ent15" in string
def _mirostat2_br002_ent2(string):
    return "_mirostat2_br002_ent2" in string
def _mirostat2_br002_ent5(string):
    return "_mirostat2_br002_ent5" in string
def _mirostat2_br002_ent8(string):
    return "_mirostat2_br002_ent8" in string

def _mirostat2_br02_ent15(string):
    return "_mirostat2_br02_ent15" in string
def _mirostat2_br02_ent2(string):
    return "_mirostat2_br02_ent2" in string
def _mirostat2_br02_ent5(string):
    return "_mirostat2_br02_ent5" in string
def _mirostat2_br02_ent8(string):
    return "_mirostat2_br02_ent8" in string

def _mirostat2_br05_ent15(string):
    return "_mirostat2_br05_ent15" in string
def _mirostat2_br05_ent2(string):
    return "_mirostat2_br05_ent2" in string
def _mirostat2_br05_ent5(string):
    return "_mirostat2_br05_ent5" in string
def _mirostat2_br05_ent8(string):
    return "_mirostat2_br05_ent8" in string

def nkvo(string):
    return "nkvo" in string
def not_nkvo(string):
    return not nkvo(string)

def _0(string):
    return "_0_" in string
def _32(string):
    return "_32_" in string
def _128(string):
    return "_128_" in string
def _all(string):
    return "_all_" in string

def _1(string):
    return "_1_" in string
def _1_5(string):
    return "_1.5_" in string
def _20(string):
    return "_20_" in string

def _np01_ns10_ps10_(string):
    return "_np01_ns10_ps10_" in string
def _np01_ns10_ps1_(string):
    return "_np01_ns10_ps1_" in string
def _np01_ns10_ps2_(string):
    return "_np01_ns10_ps2_" in string
def _np01_ns1_ps10(string):
    return "_np01_ns1_ps10_" in string
def _np01_ns1_ps1_(string):
    return "_np01_ns1_ps1_" in string
def _np01_ns1_ps2_(string):
    return "_np01_ns1_ps2_" in string
def _np01_ns2_ps10_(string):
    return "_np01_ns2_ps10_" in string
def _np01_ns2_ps1_(string):
    return "_np01_ns2_ps1_" in string
def _np01_ns2_ps2_(string):
    return "_np01_ns2_ps2_" in string
def _np05_ns10_ps10_(string):
    return "_np05_ns10_ps10_" in string
def _np05_ns10_ps1_(string):
    return "_np05_ns10_ps1_" in string
def _np05_ns10_ps2_(string):
    return "_np05_ns10_ps2_" in string
def _np05_ns1_ps10_(string):
    return "_np05_ns1_ps10_" in string
def _np05_ns1_ps1_(string):
    return "_np05_ns1_ps1_" in string
def _np05_ns1_ps2_(string):
    return "_np05_ns1_ps2_" in string
def _np05_ns2_ps10_(string):
    return "_np05_ns2_ps10_" in string
def _np05_ns2_ps1_(string):
    return "_np05_ns2_ps1_" in string
def _np05_ns2_ps2_(string):
    return "_np05_ns2_ps2_" in string
def _np09_ns10_ps10(string):
    return "_np09_ns10_ps10" in string
def _np09_ns10_ps1_(string):
    return "_np09_ns10_ps1_" in string
def _np09_ns10_ps2_(string):
    return "_np09_ns10_ps2_" in string
def _np09_ns1_ps10_(string):
    return "_np09_ns1_ps10_" in string
def _np09_ns1_ps1_(string):
    return "_np09_ns1_ps1_" in string
def _np09_ns1_ps2_(string):
    return "_np09_ns1_ps2_" in string
def _np09_ns2_ps10_(string):
    return "_np09_ns2_ps10_" in string
def _np09_ns2_ps1(string):
    return "_np09_ns2_ps1" in string
def _np09_ns2_ps2(string):
    return "_np09_ns2_ps2" in string

def _0(string):
    return "0_" in string
def _0_5(string):
    return "05_" in string
def _5_(string):
    return "5_" in string

def _10(string):
    return "_10_" in string
def _60(string):
    return "_60_" in string
def _80(string):
    return "_80_" in string
def _90(string):
    return "_90_" in string
def _95(string):
    return "_95_" in string
def _100(string):
    return "_100_" in string

def _1(string):
    return "_thread1_" in string
def _2(string):
    return "_thread2_" in string
def _4(string):
    return "_thread4_" in string
def _8(string):
    return "_thread8_" in string

def _5(string):
    return "_5_" in string
def _20(string):
    return "_20_" in string
def _100(string):
    return "_100_" in string

def _01(string):
    return "_01_" in string
def _05(string):
    return "_05_" in string
def _99(string):
    return "_99_" in string

def _0(string):
    return "_0_" in string
def _5(string):
    return "_5_" in string
def _9(string):
    return "_9_" in string

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
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_0)]
    name_option = option_name
    preparation_data(model,df,name_option)
 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <argument>")
    else:
        main(sys.argv[1], sys.argv[2])