###############################################################################
## 1. read the copyright text from file
def get_copyright_text(copyright_file):
    with open(copyright_file,"r") as fcopyright:
        content = fcopyright.readlines()
    copyright_text = ''.join(content) # convert to string
    # print(copyright_text)
    return copyright_text

###############################################################################
## 2. Listing All Files in a Directory
def get_list_of_files_in_directory(src_code_directory):
    from pathlib import Path
    basepath = Path(src_code_directory)
    entries = (entry for entry in basepath.iterdir() if entry.is_file())
    for entry in entries:
        print(entry.name)

def get_list_of_files_by_extension(src_code_directory,extn):
    from pathlib import Path
    basepath = Path(src_code_directory)
    list_of_files = basepath.glob('**/*.'+extn)
    extn_files = []
    for item in list_of_files:
        extn_files.append(str(item))
    return extn_files


###############################################################################

def prepend_copyright_text_single(src_code_file,copyright_file):
#     from tempfile import TemporaryFile
    copyright_text = get_copyright_text(copyright_file)
    with open(src_code_file,"r") as fsrc:
        src_code = fsrc.read()
        # print(src_code)
        full_content = copyright_text + "\n" + src_code
        # print(full_content)
        # ftemp = TemporaryFile('w+t') # This will create and open a file that can be used as a temporary storage area.
        # ftemp.write(full_content)
        # data = ftemp.read()
        # print(data)
        # ftemp.close()
    with open(src_code_file,"w+") as fsrc_new:
        fsrc_new.write(full_content)
###############################################################################
def prepend_copyright_text_all(copyright_file, src_code_directory,extn_list):
    list_of_files = get_list_of_files_by_extension(src_code_directory,'cpp') # hardcoded: ToDo: changes to extn
    # print(list_of_files)
    for src_code_file in list_of_files:
        prepend_copyright_text_single(src_code_file,copyright_file)

###############################################################################
# Find and replace copyright text
def replace_copyright_text_single(src_code_file,old_copyright_text,new_copyright_text):
#     from tempfile import TemporaryFile
    with open(src_code_file,"r") as fsrc:
        src_code = fsrc.read()
        # print(src_code)
        full_content = src_code.replace(old_copyright_text,new_copyright_text)
    with open(src_code_file,"w") as fsrc_new:
        print(src_code_file)
        fsrc_new.write(full_content)


def replace_copyright_text_all(old_copyright_file, new_copyright_file, src_code_directory, extn_list):
        with open(old_copyright_file,"r") as foldcopy, open(new_copyright_file,"r") as fnewcopy:
                old_copyright_text = foldcopy.read()
                new_copyright_text = fnewcopy.read()  
        list_of_files = get_list_of_files_by_extension(src_code_directory,extn_list)   
        for src_code_file in list_of_files:
                replace_copyright_text_single(src_code_file,old_copyright_text,new_copyright_text)                

###############################################################################

if __name__=="__main__":
    new_copyright_file = 'copyright.txt'
    old_copyright_file = './old_copyright_samples/old_copyright_2.txt'
    # src_code_file = 'test_1.cpp's
    # copyright_text = get_copyright_text(copyright_file)
    # print(copyright_text)
    # prepend_copyright_text(src_code_file,copyright_file)
    src_code_directory = 'my_directory'
    # get_list_of_files_to_update(src_code_directory)
#     extn = 'cpp'
#     list_of_files = get_list_of_files_by_extension(src_code_directory,extn)
    # print(list(list_of_files))
#     prepend_copyright_text_all(src_code_directory,copyright_file)
    replace_copyright_text_all(old_copyright_file,new_copyright_file,src_code_directory,'cpp')


