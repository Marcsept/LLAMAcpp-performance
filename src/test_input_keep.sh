#!/bin/bash
#==============================================================================
# Script Name: test_input_keep.sh
# Description: A simple function who try some value of keep option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

keep () {

  #Define variables
  local md=$1
  local option="keep"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--keep 0" "keep_0"

  try_option $outputs_path $inputs_path $model "--keep 20" "keep_20"
  
  try_option $outputs_path $inputs_path $model "--keep -1" "keep_all"



  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
