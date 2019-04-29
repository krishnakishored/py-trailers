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
    from tempfile import TemporaryFile
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
def prepend_copyright_text_all(src_code_directory,copyright_file):
    list_of_files = get_list_of_files_by_extension(src_code_directory,'cpp') # hardcoded: ToDo: changes to extn
    # print(list_of_files)
    for src_code_file in list_of_files:
        prepend_copyright_text_single(src_code_file,copyright_file)

###############################################################################
#3. Create a temporary file
# from tempfile import TemporaryFile

# # save the tempfile contents in the src_file
# from shutil import copyfileobj

# # Create a temporary file and write some data to it
# ftemp = TemporaryFile('w+t') # This will create and open a file that can be used as a temporary storage area.

# full_content = copyright_text + "\n" + src_code
# ftemp.write(full_content)
# # Go back to the beginning and read data from file
# ftemp.seek(0)
# data = ftemp.read()
# # print(data)


# with open('test_1.cpp','w+') as fsrc:
#     # copyfileobj(ftemp,fsrc)
#     fsrc.write(data)
# # Close the file, after which it will be removed
# ftemp.close()

###############################################################################

if __name__=="__main__":
    copyright_file = 'copyright.txt'
    src_code_file = 'test_1.cpp'
    # copyright_text = get_copyright_text(copyright_file)
    # print(copyright_text)
    # prepend_copyright_text(src_code_file,copyright_file)
    src_code_directory = 'my_directory'
    # get_list_of_files_to_update(src_code_directory)
    extn = 'cpp'
    list_of_files = get_list_of_files_by_extension(src_code_directory,extn)
    # print(list(list_of_files))
    prepend_copyright_text_all(src_code_directory,copyright_file)

