import pandas as pd

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
    1. reading base csv file from url
    2. populate the base_voice_dict for runtime access
    '''
    with open(base_file, encoding='UTF-16') as f:
        raw_data = pd.read_csv(f)
    # # dropping null value columns to avoid errors
    raw_data.dropna(inplace=True)

    # converting to dict
    csv_dict = raw_data.to_dict()
    target_column = raw_data[translation_map[output_lang]]
    # base_column = raw_data[translation_map['TEXT TO BE TRANSLATED']]
    base_column = raw_data[translation_map['english']]
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
    return next_word


def get_text_inbetween(input_string, start, end):
    '''
        return the text between first match of 'start' & last match of 'end' strings
    '''
    text_inbetween = input_string[input_string.find(start)+len(start):input_string.rfind(end)]
    return text_inbetween

def translate(base_file, input_file, output_lang):
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
                # ToDo: string manipulation
                query_text = find_next_word_after_match(line, '(name')
                if query_text is not None and query_text in reference_dict:
                    # print(query_text)
                    target_text = reference_dict[query_text]
                    print(target_text)
                    text_to_replace = get_text_inbetween(line, '"', '"')
                    line = line.replace(text_to_replace, target_text)
                    # print(line)                    
                f_out.write(line)


# maps argument to column names in the BaseVoiceString.csv
translation_map = {
    "english": "TEXT TO BE TRANSLATED",
    "portuguese": "pt-BR (Brazilian Portuguese)",
    "czech": "cz-CZ (Czech)",
    "polish": "pl-PL (Polish)",
    "swedish": "sv-SE (Swedish)",
    "norwegian": "no-NO (Norwegian)"
}

if __name__ == "__main__":
    # translate('./base/BaseVoiceString.csv', 'TTS_basicaudio-cs-CS.sexp', 'polish')
    # translate('./base/BaseVoiceString.csv', 'TTS_basicaudio-cs-CS.sexp', 'czech')
    # translate('./base/BaseVoiceString.csv', 'TTS_basicaudio-cs-CS.sexp', 'swedish')
    # translate('./base/BaseVoiceString.csv', 'TTS_basicaudio-cs-CS.sexp', 'swedish')
    for language in translation_map.keys():
        translate('./base/BaseVoiceString.csv', 'TTS_basicaudio-cs-CS.sexp', language)