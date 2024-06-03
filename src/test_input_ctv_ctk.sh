#!/bin/bash
#==============================================================================
# Script Name: test_input_ctv_ctk.sh
# Description: A simple function who try some value of ctv and ctk option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

ctv_ctk () {

  #Define variables
  local md=$1
  local option="ctv_ctk"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model " -ctk f16 -ctv f16 " "ctk_f16_ctv_f16"

  try_option $outputs_path $inputs_path $model " -ctk f32 -ctv f32 " "ctk_f32_ctv_f32"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
