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
    return "_001_" in string
def ten(string):
    return "_01_" in string
def thirty(string):
    return "_03_" in string


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

def _1_(string):
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

def _0_(string):
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
    print(mean_total_time_token_per_seconde)
    print(step3_mean_total_time_token_per_seconde)
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

def main(arg):
    model = "aggregations/"+arg
    
    #Preparation output
    colums= ["Option","mean_load_time","mean_sample_token_per_seconde","mean_prompt_eval_time_token_per_seconde","mean_eval_time_token_per_seconde","mean_total_time_token_per_seconde"]
    if os.path.exists(model+"_summerize.csv"):
        os.remove(model+"_summerize.csv")
    stock(model, colums)

    preparation_data(model,pd.read_csv(model+"_test_input_only_aggregation.csv", sep=';', encoding='latin1'), "without option")

    #option type f32 in cache for K and V
    df = pd.read_csv(model+"_test_input_ctv_ctk_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_ctv_ctk_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(f32)]
    name_option = "KV_f32"
    preparation_data(model,df,name_option)

    #option type f16 in cache for K and V
    df = pd.read_csv(model+"_test_input_ctv_ctk_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_ctv_ctk_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(f16)]
    name_option = "KV_f16"
    preparation_data(model,df,name_option)

    #option group attention factor 2 (default 1)
    df = pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(n)]
    name_option = "grp_att_factor_2"
    preparation_data(model,df,name_option)

    #option groupe attention width 256 (default 256)
    df = pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(w)]
    name_option = "grp_att_width_256"
    preparation_data(model,df,name_option)

    #option group attention factore 2 and groupe attention width 256
    df = pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_grp_att_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(nw)]
    name_option = "grp_att_factor_width"
    preparation_data(model,df,name_option)

    #option number of tokens to keep from the initial prompt 0 (default : 0)
    df = pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(zero)]
    name_option = "keep_0"
    preparation_data(model,df,name_option)

    #option number of tokens to keep from the initial prompt 20 (default : 0)
    df = pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(twenty)]
    name_option = "keep_20"
    preparation_data(model,df,name_option)

    #option number of tokens to keep from the initial prompt -1 (all) (default : 0)
    df = pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_keep_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(all_)]
    name_option = "keep_all"
    preparation_data(model,df,name_option)

    #option min probability sampling 0.01 (default : 0.1)
    df = pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(one)]
    name_option = "min-p 0.01"
    preparation_data(model,df,name_option)

    #option min probability sampling 0.1 (default : 0.1)
    df = pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(ten)]
    name_option = "min-p 0.1"
    preparation_data(model,df,name_option)

    #option min probability sampling 0.3 (default : 0.1)
    df = pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')[pd.read_csv(model+"_test_input_min-p_aggregation.csv", sep=';', encoding='latin1')['name_'].apply(thirty)]
    name_option = "min-p 0.3"
    preparation_data(model,df,name_option)

        
    csv = model+"_test_input_mirostat_aggregation.csv"
    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br002_ent15)]
    name_option = "mirostat 1 / mirostat-lr 0.02 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br002_ent2)]
    name_option = "mirostat 1 / mirostat-lr 0.02 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br002_ent5)]
    name_option = "mirostat 1 / mirostat-lr 0.02 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br002_ent8)]
    name_option = "mirostat 1 / mirostat-lr 0.02 / mirostat-ent 8"
    preparation_data(model,df,name_option)


    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br02_ent15)]
    name_option = "mirostat 1 / mirostat-lr 0.2 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br02_ent2)]
    name_option = "mirostat 1 / mirostat-lr 0.2 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br02_ent5)]
    name_option = "mirostat 1 / mirostat-lr 0.2 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br02_ent8)]
    name_option = "mirostat 1 / mirostat-lr 0.2 / mirostat-ent 8"
    preparation_data(model,df,name_option)


    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br05_ent15)]
    name_option = "mirostat 1 / mirostat-lr 0.5 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br05_ent2)]
    name_option = "mirostat 1 / mirostat-lr 0.5 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br05_ent5)]
    name_option = "mirostat 1 / mirostat-lr 0.5 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V1 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat1_br05_ent8)]
    name_option = "mirostat 1 / mirostat-lr 0.5 / mirostat-ent 8"
    preparation_data(model,df,name_option)



    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br002_ent15)]
    name_option = "mirostat 2 / mirostat-lr 0.02 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br002_ent2)]
    name_option = "mirostat 2 / mirostat-lr 0.02 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br002_ent5)]    
    name_option = "mirostat 2 / mirostat-lr 0.02 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.02 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br002_ent8)]
    name_option = "mirostat 2 / mirostat-lr 0.02 / mirostat-ent 8"
    preparation_data(model,df,name_option)


    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br02_ent15)]
    name_option = "mirostat 2 / mirostat-lr 0.2 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br02_ent2)]
    name_option = "mirostat 2 / mirostat-lr 0.2 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br02_ent5)]
    name_option = "mirostat 2 / mirostat-lr 0.2 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.2 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br02_ent8)]
    name_option = "mirostat 2 / mirostat-lr 0.2 / mirostat-ent 8"
    preparation_data(model,df,name_option)


    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 15 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br05_ent15)]
    name_option = "mirostat 2 / mirostat-lr 0.5 / mirostat-ent 15"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 2 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br05_ent2)]
    name_option = "mirostat 2 / mirostat-lr 0.5 / mirostat-ent 2"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 5 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br05_ent5)]
    name_option = "mirostat 2 / mirostat-lr 0.5 / mirostat-ent 5"
    preparation_data(model,df,name_option)

    #option mirostat : V2 (default : not use) 
    #option mirostat learning rate : 0.5 (default : 0.1)
    #option mirostat entropy : 8 (default : 5)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_mirostat2_br05_ent8)]
    name_option = "mirostat 2 / mirostat-lr 0.5 / mirostat-ent 8"
    preparation_data(model,df,name_option)

    csv=model+"_test_input_nkvo_aggregation.csv"
    #option disable KV offload
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(nkvo)]
    name_option = "disable KV offload"
    preparation_data(model,df,name_option)

    #without option
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(not_nkvo)]
    name_option = "Normal"
    preparation_data(model,df,name_option)

    csv=model+"_test_input_repeat_last_n_aggregation.csv"
    #option last n tokens to consider for penalize : 0 (default : 64)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_0)]
    name_option = "repeat last n : 0"
    preparation_data(model,df,name_option)

    #option last n tokens to consider for penalize : 32 (default : 64)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_32)]
    name_option = "repeat last n : 32"
    preparation_data(model,df,name_option)

    #option last n tokens to consider for penalize : 128 (default : 64)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_128)]
    name_option = "repeat last n : 128"
    preparation_data(model,df,name_option)

    #option last n tokens to consider for penalize : context file (default : 64)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_all)]
    name_option = "repeat last n : context file"
    preparation_data(model,df,name_option)

    csv=model+"_test_input_repeat_penalty_aggregation.csv"
    #option penalize repeat sequence of tokens : 1 (default : 1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_1_)]
    name_option = "repeat penalty : 1"
    preparation_data(model,df,name_option)

    #option penalize repeat sequence of tokens : 1.5 (default : 1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_1_5)]
    name_option = "repeat penalty : 1.5"
    preparation_data(model,df,name_option)

    #option penalize repeat sequence of tokens : 20 (default : 1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_20)]
    name_option = "repeat penalty n : 20"
    preparation_data(model,df,name_option)

    csv=model+"_test_input_split_aggregation.csv"
    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns10_ps10_)]
    name_option = "_np01_ns10_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns10_ps1_)]
    name_option = "_np01_ns10_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns10_ps2_)]
    name_option = "_np01_ns10_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns1_ps10)]
    name_option = "_np01_ns1_ps10"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns1_ps1_)]
    name_option = "_np01_ns1_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns1_ps2_)]
    name_option = "_np01_ns1_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns2_ps10_)]
    name_option = "_np01_ns2_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns2_ps1_)]
    name_option = "_np01_ns2_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np01_ns2_ps2_)]
    name_option = "_np01_ns2_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns10_ps10_)]
    name_option = "_np05_ns10_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns10_ps1_)]
    name_option = "_np05_ns10_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns10_ps2_)]
    name_option = "_np05_ns10_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns1_ps10_)]
    name_option = "_np05_ns1_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns1_ps1_)]
    name_option = "_np05_ns1_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns1_ps2_)]
    name_option = "_np05_ns1_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns2_ps10_)]
    name_option = "_np05_ns2_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns2_ps1_)]
    name_option = "_np05_ns2_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np05_ns2_ps2_)]
    name_option = "_np05_ns2_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns10_ps10)]
    name_option = "_np09_ns10_ps10"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns10_ps1_)]
    name_option = "_np09_ns10_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns10_ps2_)]
    name_option = "_np09_ns10_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns1_ps10_)]
    name_option = "_np09_ns1_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns1_ps1_)]
    name_option = "_np09_ns1_ps1_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns1_ps2_)]
    name_option = "_np09_ns1_ps2_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns2_ps10_)]
    name_option = "_np09_ns2_ps10_"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns2_ps1)]
    name_option = "_np09_ns2_ps1"
    preparation_data(model,df,name_option)

    #option   -np N, --parallel N   number of parallel sequences to decode (default: 1)
    #option   -ns N, --sequences N  number of sequences to decode (default: 1)
    #option   -ps N, --p-split N    speculative decoding split probability (default: 0.1)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_np09_ns2_ps2)]
    name_option = "_np09_ns2_ps2"
    preparation_data(model,df,name_option)

    csv=model+"_test_input_temp_aggregation.csv"
    #option temp : 0 (default : 0.8)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_0_)]
    name_option = "temp : 0"
    preparation_data(model,df,name_option)

    #option temp : 0.5 (default : 0.8)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_0_5)]
    name_option = "temp : 0.5"
    preparation_data(model,df,name_option)

    #option temp : 5 (default : 0.8)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_5_)]
    name_option = "temp : 5"
    preparation_data(model,df,name_option)    

        
    csv=model+"_test_input_tfs_aggregation.csv"
    #option tail free sampling : 0.9 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_90)]
    name_option = "tfs : 0.9"
    preparation_data(model,df,name_option)

    #option tail free sampling : 0.95 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_95)]
    name_option = "tfs : 0.95"
    preparation_data(model,df,name_option)

    #option tail free sampling : & (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_100)]
    name_option = "tfs : 1 disabled"
    preparation_data(model,df,name_option)

    csv = model+"_test_input_threads_aggregation.csv"

    #option Threads : 1 (default : 4)
    #option Threads : 1 (default : same Threads)
    #option Threads : 1 (default : same Threads)
    #option Threads : 1 (default : same Threads)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_1)]
    name_option = "Threads 1"
    preparation_data(model,df,name_option)

    #option Threads : 2 (default : 4)
    #option Threads : 2 (default : same Threads)
    #option Threads : 2 (default : same Threads)
    #option Threads : 2 (default : same Threads)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_2)]
    name_option = "Threads 2"
    preparation_data(model,df,name_option)

    #option Threads : 4 (default : 4)
    #option Threads : 4 (default : same Threads)
    #option Threads : 4 (default : same Threads)
    #option Threads : 4 (default : same Threads)
    df = pd.read_csv(csv, sep=';', encoding='latin4')[pd.read_csv(csv, sep=';', encoding='latin4')['name_'].apply(_4)]
    name_option = "Threads 4"
    preparation_data(model,df,name_option)

    #option Threads : 8 (default : 4)
    #option Threads : 8 (default : same Threads)
    #option Threads : 8 (default : same Threads)
    #option Threads : 8 (default : same Threads)
    #df = pd.read_csv(csv, sep=';', encoding='latin8')[pd.read_csv(csv, sep=';', encoding='latin8')['name_'].apply(_8)]
    name_option = "Threads 8"
    #preparation_data(model,df,name_option)

    csv=model+"_test_input_top-k_aggregation.csv"
    #option top-k sampling : 5 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_5)]
    name_option = "top-k : 5 "
    preparation_data(model,df,name_option)

    #option top-k sampling : 20 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_20)]
    name_option = "top-k : 20 "
    preparation_data(model,df,name_option)

    #option top-k sampling : 100 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_100)]
    name_option = "top-k : 100 "
    preparation_data(model,df,name_option)

    csv=model+"_test_input_top-p_aggregation.csv"
    #option top-k sampling : 0.1 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_01)]
    name_option = "top-p : 5 "
    preparation_data(model,df,name_option)

    #option top-k sampling : 0.5 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_05)]
    name_option = "top-p : 20 "
    preparation_data(model,df,name_option)

    #option top-k sampling : 0.99 (default : 40)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_99)]
    name_option = "top-k : 100 "
    preparation_data(model,df,name_option)

    csv=model+"_test_input_typical_aggregation.csv"
    #option locally typical sampling: 0 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_0)]
    name_option = "typicaly : 0 "
    preparation_data(model,df,name_option)

    #option locally typical sampling: 5 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_5)]
    name_option = "typicaly : 5 "
    preparation_data(model,df,name_option)

    #option locally typical sampling: 9 (default : 1 disabled)
    df = pd.read_csv(csv, sep=';', encoding='latin1')[pd.read_csv(csv, sep=';', encoding='latin1')['name_'].apply(_9)]
    name_option = "typicaly : 9 "
    preparation_data(model,df,name_option)  

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <argument>")
    else:
        main(sys.argv[1])