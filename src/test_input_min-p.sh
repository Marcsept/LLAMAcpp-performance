#!/bin/bash
#==============================================================================
# Script Name: test_input_min-p.sh
# Description: A simple function who try some value of min-p option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

min-p () {

  #Define variables
  local md=$1
  local option="min-p"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--min-p 0.01" "min_p_001"
  
  try_option $outputs_path $inputs_path $model "--min-p 0.1" "min_p_01"
  
  try_option $outputs_path $inputs_path $model "--min-p 0.3" "min_p_03"

  try_option $outputs_path $inputs_path $model "--min-p 0" "min_p_0"

  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
