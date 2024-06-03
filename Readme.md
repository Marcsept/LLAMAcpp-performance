# Test benchmark LLAMA

By : Valère BILLAUD

## How use it ? 

The command ``main_test.sh NAME_MODEL`` permet to run all tests present in src file. 

- NAME_MODEL : "gpt2", "llama2" and "mistral7B", you can add model in ``models file``

## List of tests 

- only : without more options that potions use to create a similaire environement of run for every test, (the model, the prompt file, the seed and a number of generated tokens)


- ctv ctk : KV cache data type for V and K
    - Values to test : f16 and f32
    - Default : f16

- grp_att : Groupe attentionfactor and width
    - Values to test : factor 2, witdh 256 and (factor 2 + witdh 256)
    - Default : factor 1, witdh 512

- keep : number of tokens to keep from the initial prompt 
    - Values to test : 0, 20, all
    - Default : 0 

- min-p : min-p sampling 
    - Values to test : 0, 0.01, 0.1 and 0.3
    - Default : 0.1 

- mirostat : mirostat sampling with the learning rate and entrhopy (mirostat, mirostat-lr, mirostat-ent)
    - Values to test : (1, 0.2, 2), (1, 0.2, 5), (1, 0.2, 8), (1, 0.2, 15), (1, 0.5, 2), (1, 0.5, 5), (1, 0.5, 8), (1, 0.5, 15), (1, 0.02, 2), (1, 0.02, 5), (1, 0.02, 8), (1, 0.02, 15) (2, 0.2, 2), (2, 0.2, 5), (2, 0.2, 8), (, 0.2, 15), (2, 0.5, 2), (2, 0.5, 5), (2, 0.5, 8), (2, 0.5, 15), (2, 0.02, 2), (2, 0.02, 5), (2, 0.02, 8), (2, 0.02, 15)
    - Default : (0 (disabeal), 0.1, 5.0)

- nkvo : disable KV offload 

- Repeat last n : last n tokens to consider for penalize
    - Values to test : 0, 32, 128, -1 (All)
    - Default : 64 (0 disabled)

- Repeat penalty : penalize repeat sequence of tokens
    - Values to test : 1, 1.5, 20
    - Default : 1 disabled

- Split : (np : number of parallele sequence, ns : number sequence to decode, sp : speculative decoding split probability)
    - Values to tests : (0.1, 1, 1), (0.5, 1, 1), (0.9, 1, 1), (0.1, 2, 1), (0.5, 2, 1), (0.9, 2, 1), (0.1, 10, 1), (0.5, 10, 1), (0.9, 10, 1), (0.1, 1, 2), (0.5, 1, 2), (0.9, 1, 2), (0.1, 2, 2), (0.5, 2, 2), (0.9, 2, 2), (0.1, 10, 2), (0.5, 10, 2), (0.9, 10, 2), (0.1, 1, 10), (0.5, 1, 10), (0.9, 1, 10), (0.1, 2, 10), (0.5, 2, 10), (0.9, 2, 10), (0.1, 10, 10), (0.5, 10, 10), (0.9, 10, 10),
    - Default : (1, 1, 0.1)

- Temp : temperature 
    - Values to tets : 0, 0.5, 5
    - Default : 0.8

- Tfs : tail free sampling, parameter z 
    - Values to tests : 1, 0.95, 0.90
    - Default : 1 (disabled)

- Threads : Number of threads to use during generation
    - Values to tests : 1, 2, 4, 8, 16
    - Default : 4

- Top-k : top-k sampling
    - Values to tests : 5, 20, 100
    - Default : 40 (0 disabled)

- Top-p : top-p sambling
    - Values to tests : 0.1, 0.5, 0.99
    - Default : 0.9 (1 disabled)

- Typical : locally typical sampling, parameter p
    - Values to tests : 0, 0.5, 0.9 
    - Default : 1 (disabled)

## Input / output  

You can add inputs in the file ``inputs``. 

For all tests a file wase create in outputs to stock the result and the log of the test. At the end a python script retrieve date from log and merge it in a csv per option in file aggregation.

To manipulete and visualise this data you have a notebook (in aggregation) with some comparaison and graph. 


