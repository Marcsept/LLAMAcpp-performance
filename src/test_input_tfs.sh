#!/bin/bash
#==============================================================================
# Script Name: test_input_tfs.sh
# Description: A simple function who try some value of tfs option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

tfs () {

  #Define variables
  local md=$1
  local option="tfs"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--tfs 1" "tfs_100"

  try_option $outputs_path $inputs_path $model "--tfs 0.95" "tfs_95"

  try_option $outputs_path $inputs_path $model "--tfs 0.90" "tfs_90"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
