import argparse  # for adding help & command-line options

from crux import  update_copyright_text_all

'''
Read the default values for the args from the config file.
But the args passed via the command-line overwrites the defaults

'''

def read_config(config_file='defaults.json'):
    import json
    config = json.loads(open('defaults.json','r').read())
    # print(config)
    return config


def run_copyrighter_with_args(*args, **kwargs):
    
    default_config = read_config()
    # parser.add_argument("-c", "--cfg", help="config file", default='./defaults.json')
    # default_config = read_config(args.cfg)
    parser = argparse.ArgumentParser(description='copyrighter')
    parser.add_argument("-o", "--old", help="full filename of old_copyright_file.txt", default=default_config["old_copyright_file"])
    parser.add_argument("-n", "--new", help="full filename of new_copyright_file.txt", default=default_config["new_copyright_file"])
    parser.add_argument("-e", "--ext", help="list of file extenstions", default=default_config["file_extension_list"])
    parser.add_argument("-s", "--src", help="source directory", default=default_config["src_code_dir"])
    parser.add_argument("-i", "--ign", help="list of directories to ignore", default=default_config["ignore_directories_list"])
    parser.add_argument("-d", "--ocd", help="dir containing all old_copyright texts ", default=default_config["old_copyright_dir"])
    
    
    # parser.add_argument("-n", "--new", help="full filename of new_copyright_file.txt", default="new_copyright_file.txt")
    # parser.add_argument("-o", "--old", help="full filename of old_copyright_file.txt", default="old_copyright_file.txt")
    # parser.add_argument("-e", "--ext", help="list of file extenstions", default="cpp,h")
    # parser.add_argument("-s", "--src", help="source directory", default="my_directory")
    args = parser.parse_args()

    update_copyright_text_all(args.old,args.new,args.src,args.ext)
    # if(args.language != 'all'):
    #     text_translator(args.base, args.input, args.language)
    # else:
    #     # Update the 'translation_map'  dict to generate all files in one go
    #     for out_lang in translation_map.keys():
    #         text_translator(args.base, args.input, out_lang)





    
if __name__ == "__main__":
    run_copyrighter_with_args()