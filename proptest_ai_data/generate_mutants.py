from openai import OpenAI
import argparse
import os
import logging
import json
from typing import Union
from prompts import *
from tqdm import tqdm
from datetime import datetime

def jsonlines_dump(fname: str, data: Union[dict, list]):
    try:
        with open(fname, 'a+') as f:
            if isinstance(data, dict):
                f.write(json.dumps(data)+'\n')
            elif isinstance(data, list):
                for d in data:
                    f.write(json.dumps(d)+'\n')

    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error: {e}')
        print(f'Could not write to {fname}')

def jsonlines_load(fname: str):
    with open(fname, 'r') as f:
        return [json.loads(line) for line in f]

def main(args):
    if args.key == 'None':
        # check if there is file called openai_key.txt
        if os.path.exists('../openai_key.txt'):
            with open('../openai_key.txt', 'r') as f:
                key = f.read()
        else:
            logging.error('Please provide OpenAI API key.')
            return 0
    else:
        key = args.key

    client = OpenAI(api_key=key)
    dt_string = datetime.now().strftime("%m-%d-%H:%M")

    # read the input file
    all_data = jsonlines_load(args.input_path)

    if args.end == -1:
        end_index = len(all_data)
    else:
        end_index = args.end

    eval_data = all_data[args.start:end_index]

    progress_bar = tqdm(range(len(eval_data)))

    for i in progress_bar:

        system_prompt = MUTANT_SYSTEM_PROMPT
        function_name = eval_data[i]['function_name']
        output_path = f'{args.output_dir}/{function_name}.jsonl'

        all_properties = eval_data[i]['properties'][0].split('\n\n')
        all_pbts = eval_data[i]['pbt'][0].strip().split('\n\n')
        assert len(all_properties) == len(all_pbts)-1, f'Error: properties and pbt mismatch for {function_name}'
        
        for idx, prop in enumerate(all_properties):
            
            prop = prop[3:].strip()
            pbt = all_pbts[idx+1].strip()

            question = MUTANTS_TEST_FUNCTION_PROMPT.format(function_name=eval_data[i]['function_name'], api_documentation=eval_data[i]['api_doc'], prop=prop, pbt=pbt)

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question} 
            ]

            response = client.chat.completions.create(
                model=args.model,
                messages=messages,
                temperature=args.temperature,
                n = args.num_samples,
                seed  = args.seed
            )
            response_text = []
            for choice in response.choices:
                response_text.append(choice.message.content)

            if args.verbose:
                print('messages:\n', messages)
                print('\n\nresponse:\n', response)
                print('model name: ', response.model)
                print('\nquestion:\n', question)
                print('\ncontent:\n', response_text)
                print('\nOne response example: \n', response_text[0])

            to_save_data = {
            'function_name': eval_data[i]['function_name'],
            'mutants': response_text,
            'property': prop,
            'pbt': pbt,
            'properties': eval_data[i]['properties'],
            }
            jsonlines_dump(output_path, to_save_data)
    
    full_model_name = response.model
    system_fingerprint = response.system_fingerprint
    full_file_name =  os.path.join(os.path.dirname(__file__), output_path)
    save_parameters = {
        'model_name': full_model_name,
        'file_name': full_file_name,
        'system_prompt': system_prompt,
        'temperature': args.temperature,
        'seed': args.seed,
        'num_samples': args.num_samples,
        'system_fingerprint': system_fingerprint,
        'input_path': args.input_path,
        'demo_message': messages
    }
    jsonlines_dump(f'{args.output_dir}/parameters.jsonl', save_parameters)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='../our_proptest_data/output_jsonl/pbt/pbt_0_1.jsonl')
    parser.add_argument('--output_dir', type=str, default='../our_proptest_data/output_jsonl/mutants')
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=40)
    parser.add_argument('--mode', type=str, default='properties', help='properties, pbt or mutants')
    parser.add_argument('--model', type=str, default='gpt-4o-mini')
    parser.add_argument('--temperature', type=float, default=0.7)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--num_samples', type=int, default=5)
    parser.add_argument('--key', type=str, default='None', help='OpenAI API key, sk-proj-XXXX')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    main(args)
