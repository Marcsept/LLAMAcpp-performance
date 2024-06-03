#!/bin/bash
#==============================================================================
# Script Name: test_input_repeat_penalty.sh
# Description: A simple function who try some value of repeat_penalty option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

repeat_penalty () {

  #Define variables
  local md=$1
  local option="repeat_penalty"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--repeat_penalty 1" "repeat_penalty_1"

  try_option $outputs_path $inputs_path $model "--repeat_penalty 1.5" "repeat_penalty_1.5"

  try_option $outputs_path $inputs_path $model "--repeat_penalty 20" "repeat_penalty_20"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
