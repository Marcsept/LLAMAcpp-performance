# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:54:41 2024

@author: User
"""

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
                if (("llm_load_print_meta:" in line_split) or ("llm_load_tensors:" in line_split) or ("llama_new_context_with_model:" in line_split) or ("llama_kv_cache_init:" in line_split)):
                    egale = False
                    value_at_add = ""
                    #print(line_split)
                    for i in line_split :
                        if(egale):
                            value_at_add += i
                        else :
                            egale = i == '='
                    if (not("UNK token" in line)):
                        out.append(value_at_add)

                elif("system_info:" in line_split):
                    line_split = line[12:].split("|")[:-1]
                    for j in line_split:
                        egale = False
                        value_at_add = ""
                        for i in j :
                            if(egale):
                                value_at_add += i
                            else :
                                egale = i == '='
                        out.append(value_at_add)

                elif(("repeat_last_n =" in line) or ("top_k =" in line) or ("mirostat =" in line)):
                    line_split = line.split(',')
                    egale = False
                    #print(line_split)
                    for j in line_split:
                        egale = False
                        value_at_add = ""
                        for i in j :
                            if(egale):
                                value_at_add += i
                            else :
                                egale = i == '='
                        out.append(value_at_add)

                elif("generate:" in line_split):
                    line_split = line[9:].split(",")
                    #print(line_split)
                    for j in line_split:
                        egale = False
                        value_at_add = ""
                        for i in j :
                            if(egale):
                                value_at_add += i
                            else :
                                egale = i == '='
                        out.append(value_at_add)

                elif("llama_print_timings:" in line_split):
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
    'format',
    'arch',
    'vocab_type',
    'n_vocab',
    'n_merges',
    'n_ctx_train',
    'n_embd',
    'n_head',
    'n_head_kv',
    'n_layer',
    'n_rot',
    'n_embd_head_k',
    'n_embd_head_v',
    'n_gqa',
    'n_embd_k_gqa',
    'n_embd_v_gqa',
    'f_norm_eps',
    'f_norm_rms_eps',
    'f_clamp_kqv',
    'f_max_alibi_bias',
    'f_logit_scale',
    'n_ff',
    'n_expert',
    'n_expert_used',
    'causal_attn',
    'pooling_type',
    'rope_type',
    'rope_scaling',
    'freq_base_train',
    'freq_scale_train',
    'n_yarn_orig_ctx',
    'rope_finetuned',
    'ssm_d_conv',
    'ssm_d_inner',
    'ssm_d_state',
    'ssm_dt_rank',
    'model_type',
    'model_ftype',
    'model_params',
    'model_size',
    'general.name',
    'BOS_token',
    'EOS_token',
    'LF_token',
    'ggme_ctx_size',
    'CPU_buffer_size',
    'n_ctx',
    'n_batch',
    'n_ubatch',
    'flash_attn',
    'freq_base',
    'freq_scal',
    'CPU_KV_buffer_size',
    'KV_self_size',
    'CPU_output_buffer_size',
    'CPU_compute_buffer_size',
    'graph_nodes',
    'graph_splits',
    'n_threads',
    'AVX',
    'AVX_VNNI',
    'AVX2',
    'AVX512',
    'AVX512_VBMI',
    'AVX512_VNNI',
    'FMA',
    'NEON',
    'ARM_FMA',
    'F16C',
    'FP16_VA',
    'WASM_SIMD',
    'BLAS',
    'SSE3',
    'SSSE3',
    'VSX',
    'MATMUL_INT8',
    'LLAMAFILE',
    'repeat_last_n',
    'repeat_penalty',
    'frequency_panalty',
    'presence_penatly',
    'top_k',
    'tfs_z',
    'top_p',
    'min_p',
    'typical_p',
    'temp',
    'mirostat',
    'mirostat_lr',
    'mirostat_ent',
    'generate_n_ctx',
    'generate_n_batch',
    'generate_n_predict',
    'generate_n_keep',
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
    