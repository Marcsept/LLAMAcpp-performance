#!/bin/bash
#==============================================================================
# Script Name: test_input_split.sh
# Description: A simple function who try some value of split option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

split () {

  #Define variables
  local md=$1
  local option="split"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 1 -ps 1" "np01_ns1_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 1 -ps 1" "np05_ns1_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 1 -ps 1" "np09_ns1_ps1"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 2 -ps 1" "np01_ns2_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 2 -ps 1" "np05_ns2_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 2 -ps 1" "np09_ns2_ps1"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 10 -ps 1" "np01_ns10_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 10 -ps 1" "np05_ns10_ps1"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 10 -ps 1" "np09_ns10_ps1"



  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 1 -ps 2" "np01_ns1_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 1 -ps 2" "np05_ns1_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 1 -ps 2" "np09_ns1_ps2"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 2 -ps 2" "np01_ns2_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 2 -ps 2" "np05_ns2_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 2 -ps 2" "np09_ns2_ps2"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 10 -ps 2" "np01_ns10_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 10 -ps 2" "np05_ns10_ps2"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 10 -ps 2" "np09_ns10_ps2"



  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 1 -ps 10" "np01_ns1_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 1 -ps 10" "np05_ns1_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 1 -ps 10" "np09_ns1_ps10"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 2 -ps 10" "np01_ns2_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 2 -ps 10" "np05_ns2_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 2 -ps 10" "np09_ns2_ps10"

  try_option $outputs_path $inputs_path $model "-np 0.1 -ns 10 -ps 10" "np01_ns10_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.5 -ns 10 -ps 10" "np05_ns10_ps10"
  try_option $outputs_path $inputs_path $model "-np 0.9 -ns 10 -ps 10" "np09_ns10_ps10"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
