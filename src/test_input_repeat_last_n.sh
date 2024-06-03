#!/bin/bash
#==============================================================================
# Script Name: test_input_repeat_last_n.sh
# Description: A simple function who try some value of repeat_last_n option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

repeat_last_n () {

  #Define variables
  local md=$1
  local option="repeat_last_n"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--repeat_last_n 0" "repeat_last_0"

  try_option $outputs_path $inputs_path $model "--repeat_last_n 32" "repeat_last_32"

  try_option $outputs_path $inputs_path $model "--repeat_last_n 128" "repeat_last_128"

  try_option $outputs_path $inputs_path $model "--repeat_last_n -1" "repeat_last_all"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
