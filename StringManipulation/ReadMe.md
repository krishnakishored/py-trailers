#### How to run this app
1. Create a folder - say 'voice_conversion'
2. Copy the following files to the folder : 
    - `text_translator.py`
    - `requirements.txt` 
    - `ReadMe.md`(this file) 
    -  `Base_voice_string_translations.xlsx` (base_file)
    - `TTS_basicaudio-cs-CS.sexp` (input_file)
3. Create a python3 virtual environment = `$ python3 -m venv venv` in the folder 
4. Activate the environment - `$ source venv/bin/activate`
5. Install the dependencies - `(venv) $  pip install -r requirements.txt` 
    upgrade pip if it prompts - `pip install --upgrade pip`
6. Run the text_translator.py 
    - `$ python text_translator.py -h `  for help options & command line args
    -  `$ python text_translator.py` -  (default output_language set to 'swedish')
        `TTS_basicaudio-sv-SE.sexp ` gets created as the required output file. 
        Also *Base_voice_string_translations.csv* from *Base_voice_string_translations.xlsx*  is created as part of translation. 