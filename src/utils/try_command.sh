#!/bin/bash

#==============================================================================
# Script Name: try_command.sh
# Description: A simple function who call man.exe from llama.
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================


# Define the function
try_option() {

  local outputs_path=""$1 
  local inputs_path=""$2 
  local model=""$3 
  local command=$4
  local file_name=$5
  local path_weight=$6



  for input_file in "$inputs_path"/*; do
  
  local filename=$(basename -- "$input_file")
  local filename="${filename%.*}"


  # define outputs files
  local output_res_file="$outputs_path/outputs_res/${filename}_${file_name}_res.txt"
  local output_log_file="$outputs_path/outputs_log/${filename}_${file_name}_log.txt"

  #echo "../llama.cpp/main.exe -m "$model" -s 987654321 "$command" --file "$input_file" -n 100 > "$output_res_file" 2> "$output_log_file""
  # Command (main for googlecolab and main.exe for windows)
  ../llama.cpp/main -m "$model" -s 987654321 ${command} --file "$input_file" -n 10 > "$output_res_file" 2> "$output_log_file"

  echo "start copy NN weigths"
  ls ../llama.cpp/weights.csv
  ls ${path_weight}
  cp "../llama.cpp/weights.csv" ${path_weight}
  echo "remove"
  rm "../llama.cpp/weights.csv" 


done

}



