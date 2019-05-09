#### How to run copyrighter app
1. Create a folder - say 'Copyrighter'

2. Copy the following files to the folder : 
    - `copyrighter.py`
    - `crux.py`
    - `defaults.json` 
    - `ReadMe.md`(this file)
    - `requirements.txt`    

3. Create a python3 virtual environment = `$ python3 -m venv venv` in the folder 

4. Activate the environment - `$ source venv/bin/activate`

5. Install the dependencies - `(venv) $  pip install -r requirements.txt` 
    upgrade pip if it prompts - `pip install --upgrade pip`

6. Update the values in default.json
   * Add the new and old copyright content to the corresponding files
   * The following fields are required:  
        - `old_copyright_dir` -  complete path to a directory containing old_copyright files
        - `new_copyright_file` - complete path to a single new_copyright_file
        - `file_extension_list` - list of file extensions to be considered
        - `src_code_dir` - complete path to the soruce directory
        


   sample:
    ~~~js
    {
    "new_copyright_file":   "./new_copyright_file.txt",
    "file_extension_list" : ["cpp","h","qml"],
    "src_code_dir" : "my_directory",
    "old_copyright_dir": "old_copyright_dir",
    "ignore_directories_list": ["build"]
    }    
    ~~~


7. Run the copyrighter.py 
    - `$ python copyrighter` # takes the args from defaults.json
    - `$ python copyrighter.py -h `  for help options & command line args

