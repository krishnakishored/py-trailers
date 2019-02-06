import pandas as pd # for extracting columns form csv
import xlrd  # for converting xlsx to csv 

import argparse  # for adding help & command-line options


# maps argument to column names in the base.csv
translation_map = {
    "english": "TEXT TO BE TRANSLATED",
    "portuguese": "pt-BR (Brazilian Portuguese)",
    "czech": "cz-CZ (Czech)",
    "polish": "pl-PL (Polish)",
    "swedish": "sv-SE (Swedish)",
    "norwegian": "no-NO (Norwegian)"
}


def dict_zip(*dicts, fillvalue=None):
    '''
     # Util Function
     returns a dict of the form {key: [va1,val2]}
     expects to have the same keys
    '''
    all_keys = {k for d in dicts for k in d.keys()}
    return {k: [d.get(k, fillvalue) for d in dicts] for k in all_keys}


def get_runtime_base_voice_dict(base_file, output_lang):
    '''
    1. Read the base xlsx & convert it csv 
    2. populate the base_voice_dict for runtime access
    '''
    # Convert the xlsx to csv 
    data_xls = pd.read_excel(base_file,'Sheet1')  # set to default 'Sheet1' 
    input_csv = base_file.replace('.xlsx','.csv')
    data_xls.to_csv(input_csv, encoding='utf-16', index=False) # index set to 'False' to avoid column numbers
    # Fixed: UnicodeError: UTF-16 stream does not start with BOM
    with open(input_csv, encoding='UTF-16') as f:
        raw_data = pd.read_csv(f)
    # dropping null value columns to avoid errors
    raw_data.dropna(inplace=True)
    # converting to dict
    csv_dict = raw_data.to_dict()
    target_column = raw_data[translation_map[output_lang]]
    # print(target_column)
    base_column = raw_data[translation_map['english']] # default 'english' as the base column
    # print(base_column)
    base_voice_list = []
    zipped = dict_zip(base_column, target_column)
    for val in zipped.values():
        base_voice_list.append(val)

    return dict(base_voice_list)


def find_next_word_after_match(input_string, search_word):
    list_of_words = input_string.split()
    next_word = None
    if search_word in list_of_words:
        next_word = list_of_words[list_of_words.index(search_word) + 1]
    print(next_word)
    return next_word


def get_text_inbetween(input_string, start, end):
    '''
        # Util Function
        return the text between first match of 'start' & last match of 'end' strings
    '''
    grabbed_text = input_string[input_string.find(start)+len(start):input_string.rfind(end)]
    return grabbed_text

def text_translator(base_file, input_file, output_lang):
    '''
    1. get_runtime_base_voice_dict()
    2. parse the input_file
    3. look for the StringID - 'name' value  & replace 'text' value with the base_voice
    4. create an outputfile
    '''
    subtext = translation_map[output_lang]
    subtext = subtext[:subtext.find(" ")]
    output_file = input_file.replace('cs-CS', subtext)

    reference_dict = get_runtime_base_voice_dict(base_file, output_lang)

    with open(input_file, 'r') as f_in:
        with open(output_file, 'w', encoding='utf16') as f_out:
            for line in f_in:
                query_text =  get_text_inbetween(line,'"','"')
                # print(query_text)
                if query_text is not None and query_text in reference_dict:
                    target_text = reference_dict[query_text]
                    # print(target_text)
                    text_to_replace = get_text_inbetween(line, '"', '"')
                    # print(text_to_replace)
                    line = line.replace(text_to_replace, target_text)
                    # print(line)                    
                f_out.write(line)



def run_text_translator_with_args(*args,**kwargs):
    parser = argparse.ArgumentParser(description='text_translator')
    parser.add_argument("-b","--base", help="full filename of base_file.xlsx", default="Base_voice_string_translations.xlsx")
    parser.add_argument("-i","--input", help="full filename of input_file.sexp", default="TTS_basicaudio-cs-CS.sexp")
    parser.add_argument("-l","--language", help="select:  portuguese, czech, polish, swedish, norwegian or all", default="swedish")
    args = parser.parse_args()
    if(args.language != 'all'):
        text_translator(args.base,args.input, args.language)
    else:
        # Update the 'translation_map'  dictionary to generate all files in one go
        for out_lang in translation_map.keys():
            text_translator(args.base,args.input,out_lang)


if __name__ == "__main__":
    run_text_translator_with_args()
   
    # base_file = 'Base_voice_string_translations.xlsx'
    # input_file = 'TTS_basicaudio-cs-CS.sexp'
    # output_lang = 'polish'
    # text_translator(base_file,input_file, output_lang)
        
    # dict_1 = get_runtime_base_voice_dict('Base_voice_string_translations.xlsx','polish')
    # print(dict_1)
    

    