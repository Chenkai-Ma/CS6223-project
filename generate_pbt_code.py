from openai import OpenAI
import argparse
import os
import logging
from prompts import *
from tqdm import tqdm
from datetime import datetime
from tools import *

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

    dt_string = datetime.now().strftime("%m-%d-%H-%M")

    # read the input file
    all_data = jsonlines_load(args.input_path)

    if args.end == -1:
        end_index = len(all_data)
    else:
        end_index = args.end

    eval_data = all_data[args.start:end_index]

    progress_bar = tqdm(range(len(eval_data)))

    if args.mode == 'properties':
        output_path = f'{args.output_dir}/property/property_{args.start}_{end_index}_{dt_string}.jsonl'
    elif args.mode == 'pbt':
        output_path = f'{args.output_dir}/pbt/pbt_{args.start}_{end_index}_{dt_string}.jsonl'
    else:
        logging.error('Invalid mode. Please choose from properties or pbt.')
        return 0

    for i in progress_bar:

        system_prompt = SYSTEM_PROMPT
        
        if args.mode == 'properties':
            question = PROPERTIES_PROMPT_CODE.format(function_name=eval_data[i]['function_name'], api_code=eval_data[i]['api_code'])
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question} 
            ]
        elif args.mode == 'pbt':
            function_name_2 = eval_data[i]['function_name'].replace('.', '_')
            question_prev = PROPERTIES_PROMPT_CODE.format(function_name=eval_data[i]['function_name'], api_code=eval_data[i]['api_code'])
            assistant_props = eval_data[i]['properties'][0]
            question = PBT_PROPERTIES_PROMPT_CODE.format(function_name_2=function_name_2)

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question_prev},
                {"role": "assistant", "content": assistant_props},
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

        if args.mode == 'properties':
            to_save_data = {
                'function_name': eval_data[i]['function_name'],
                'properties': response_text,
                'api_doc': eval_data[i]['api_doc'],
                'api_code': eval_data[i]['api_code'],
            }
        elif args.mode == 'pbt':
            to_save_data = {
                'function_name': eval_data[i]['function_name'],
                'pbt': response_text,
                'properties': eval_data[i]['properties'],
                'api_doc': eval_data[i]['api_doc'],
                'api_code': eval_data[i]['api_code'],
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
    jsonlines_dump(f'{args.output_dir}/parameters.json', save_parameters)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='code_only/output_jsonl/property/property_0_30_11-07-19-32.jsonl')
    parser.add_argument('--output_dir', type=str, default='code_only/output_jsonl')
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=30)
    parser.add_argument('--mode', type=str, default='properties', help='properties or pbt')
    parser.add_argument('--model', type=str, default='gpt-4o-mini')
    parser.add_argument('--temperature', type=float, default=0.7, help='0.5 for properties, 0.7 for pbt')
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--num_samples', type=int, default=5, help='5 for pbt')
    parser.add_argument('--key', type=str, default='None', help='OpenAI API key, sk-proj-XXXX')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    main(args)
