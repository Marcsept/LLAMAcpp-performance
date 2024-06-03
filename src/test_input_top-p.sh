#!/bin/bash
#==============================================================================
# Script Name: test_input_top-p.sh
# Description: A simple function who try some value of top-p option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

top-p () {

  #Define variables
  local md=$1
  local option="top-p"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--top-p 0.1" "top_p_01"
  
  try_option $outputs_path $inputs_path $model "--top-p 0.5" "top_p_05"

  try_option $outputs_path $inputs_path $model "--top-p 0.99" "top_p_99"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
