from openai import OpenAI
import argparse
import os
import logging
from prompts import *
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
    no_sound_valid_data = []
    
    i = 0

    for file_name in os.listdir(args.input_path):

        if file_name.endswith(".jsonl"):
            eval_data = jsonlines_load(args.input_path + '/' + file_name)
            system_prompt = MUTANT_SYSTEM_PROMPT_DOC_CODE_2
            function_name = eval_data[0]['function_name']
            
            output_path = f'{args.output_dir}/{function_name}.jsonl'
            all_properties = eval_data[0]['properties']
            all_pbts = eval_data[0]['pbt']
            assert len(all_properties) == len(all_pbts), f'Error: properties and pbt mismatch for {function_name}'

            if len(all_properties) == 0:
                logging.warning(f'No properties found for {function_name}')
                no_sound_valid_data.append(function_name)
                continue
            
            for idx, prop in enumerate(all_properties):
                
                prop = prop[3:].strip()
                pbt = all_pbts[idx].strip()
                function_name = eval_data[0]['function_name']
                # replace . with _ in function name
                function_name_2 = function_name.replace('.', '_')
                
                # === bug in sound_valid files, api_doc should be api_code ===
                # question = MUTANTS_TEST_FUNCTION_PROMPT_CODE.format(function_name=function_name, function_name_2=function_name_2,
                #                                             api_code=eval_data[0]['api_doc'], prop=prop, pbt=pbt)

                question = MUTANTS_TEST_FUNCTION_PROMPT_DOC_CODE_2.format(function_name=function_name, function_name_2=function_name_2, 
                                                                        prop=prop, pbt=pbt)

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

                if i == 0 or args.verbose:
                    print('messages:\n', messages)
                    print('\n\nresponse:\n', response)
                    print('model name: ', response.model)
                    print('\nquestion:\n', question)
                    print('\ncontent:\n', response_text)
                    print('\nOne response example: \n', response_text[0])

                to_save_data = {
                'function_name': eval_data[0]['function_name'],
                'mutants': response_text,
                'property': prop,
                'pbt': pbt,
                'properties': eval_data[0]['properties'],
                }
                jsonlines_dump(output_path, to_save_data)

                if args.debug:
                    break

                i += 1
        
        full_model_name = response.model
        system_fingerprint = response.system_fingerprint
        full_file_name =  os.path.join(os.path.dirname(__file__), output_path)
        save_parameters = {
            'model_name': full_model_name,
            'file_name': full_file_name,
            'no_sound_valid_data': no_sound_valid_data,
            'system_prompt': system_prompt,
            'temperature': args.temperature,
            'seed': args.seed,
            'num_samples': args.num_samples,
            'system_fingerprint': system_fingerprint,
            'input_path': args.input_path,
            'demo_message': messages,
        }
        jsonlines_dump(f'{args.output_dir}/parameters.json', save_parameters)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='../doc_and_code/sound_valid')
    parser.add_argument('--output_dir', type=str, default='../doc_and_code/output_jsonl/mutants_2')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--model', type=str, default='gpt-4o-mini')
    parser.add_argument('--temperature', type=float, default=0.5)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--num_samples', type=int, default=1)
    parser.add_argument('--key', type=str, default='None', help='OpenAI API key, sk-proj-XXXX')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    main(args)
