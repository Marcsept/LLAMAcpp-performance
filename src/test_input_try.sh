#!/bin/bash
#==============================================================================
# Script Name: test_input_try.sh
# Description: A simple function who try some composed command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

try () {

  #Define variables
  local md=$1
  local param=$2
  local option=$3
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"


  #echo '"  try_option "$outputs_path" "$inputs_path"  "$model"  "$param" "$option"'
  try_option "$outputs_path" "$inputs_path"  "$model"  "$param" "$option"
  #try_option $outputs_path $inputs_path $model "-t 2 --typical 0.9 -np 0.5 -ns 2 -ps 1 -gaw 256 --top-p 5 -ctk f16 -ctv f16 --top-k 100 --repeat_last_n 32" "try1"

  #try_option $outputs_path $inputs_path $model "-t 2 --typical 0.9 -np 0.5 -ns 2 -ps 1 -gaw 256 --top-p 5 -ctk f16 -ctv f16 --top-k 100" "try2"

  #try_option $outputs_path $inputs_path $model "-t 2 --typical 0.9 --repeat_last_n 32 " "try3"




  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"
  python agregation_global_try.py $md $option


}
