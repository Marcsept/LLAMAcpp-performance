#!/bin/bash
#==============================================================================
# Script Name: test_input_typical.sh
# Description: A simple function who try some value of typical option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

typical () {

  #Define variables
  local md=$1
  local option="typical"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--typical 0" "typical_0"

  try_option $outputs_path $inputs_path $model "--typical 0.5" "typical_5"

  try_option $outputs_path $inputs_path $model "--typical 0.9" "typical_9"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
