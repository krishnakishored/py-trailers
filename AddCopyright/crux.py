###############################################################################
## 1. read the copyright text from file
def get_copyright_text(copyright_file):
    with open(copyright_file,"r") as fcopyright:
        content = fcopyright.readlines()
    copyright_text = ''.join(content) # convert to string
    # print(copyright_text)
    return copyright_text

###############################################################################
def get_filtered_list(list_of_elements, values):            
        filtered_list = list_of_elements
        for val in values:
               filtered_list = [x for x in filtered_list if x.find(val) == -1]
        #        print(filtered_list)
        return filtered_list       

## 2. Listing All Files in a Directory
def get_list_of_files_in_directory(src_code_directory,ignore_dirs=[]):
    from pathlib import Path
    basepath = Path(src_code_directory)
    entries = (entry for entry in basepath.iterdir() if entry.is_file())
    list_of_files = []
    for entry in entries:
        # print(entry.name)
        list_of_files.append(entry)
     # filter out the ignore_directories    
    list_of_files = get_filtered_list(list_of_files,ignore_dirs)    

    return list_of_files

def get_list_of_files_by_extension(src_code_directory,extn,ignore_dirs):
    from pathlib import Path
    basepath = Path(src_code_directory)
    list_of_files = basepath.glob('**/*.' + str(extn))
    extn_files = []
    for item in list_of_files:
        extn_files.append(str(item))    
    # filter out the ignore_directories    
    extn_files = get_filtered_list(extn_files,ignore_dirs)

    return extn_files

###############################################################################

def prepend_copyright_text_single(src_code_file,copyright_text):
        import sys
#     from tempfile import TemporaryFile
#     copyright_text = get_copyright_text(copyright_file)
        try:
                with open(src_code_file,"r") as fsrc:
                        src_code = fsrc.read()
                        # print(src_code)
                        full_content = copyright_text + "\n" + src_code
                        # print(full_content)
     
        except ValueError as ve:
                print(ve)
                print("error reading: " + src_code_file)
                
        try:
                with open(src_code_file,"w+") as fsrc_new:
                        fsrc_new.write(full_content)
        except Exception as e:
                print(e)
                print("error writing: " + src_code_file)


###############################################################################
def prepend_copyright_text_all(copyright_file, src_code_directory,extn_list):
    list_of_files=[]
    for ext in extn_list:
        list_of_files.extend(get_list_of_files_by_extension(src_code_directory,ext))
        # list_of_files=get_list_of_files_by_extension(src_code_directory,ext) # hardcoded: ToDo: changes to extn
     
    # print(list_of_files)
    for src_code_file in list_of_files:
        prepend_copyright_text_single(src_code_file,copyright_file)

###############################################################################
# Find and replace copyright text
def replace_copyright_text_single(src_code_file,old_copyright_text,new_copyright_text):
#     from tempfile import TemporaryFile
        try:
                with open(src_code_file,"r") as fsrc:
                        src_code = fsrc.read()
                        full_content = src_code.replace(old_copyright_text,new_copyright_text)                
        except Exception as e:
                print(e)
                print("error writing: " + src_code_file)
    
        try:
                with open(src_code_file,"w") as fsrc_new:
                # print(src_code_file)
                        fsrc_new.write(full_content)
                
        except Exception as e:
                print(e)
                print("error writing: " + src_code_file)



def replace_copyright_text_all(old_copyright_file, new_copyright_file, src_code_directory, extn_list):
        with open(old_copyright_file,"r") as foldcopy, open(new_copyright_file,"r") as fnewcopy:
                old_copyright_text = foldcopy.read()
                new_copyright_text = fnewcopy.read()  
        
        list_of_files=[]
        for ext in extn_list:
                list_of_files.extend(get_list_of_files_by_extension(src_code_directory,ext))        
        
        for src_code_file in list_of_files:
                replace_copyright_text_single(src_code_file,old_copyright_text,new_copyright_text)   

###############################################################################
'''
Looks  for the old copyright text. 
If it's not found, prepend the new copyright_text. Else, Replace the old with new 
'''

def get_all_old_copyright_text(old_copyright_directory):
        import os
        all_old_copyright_text = []
        if os.path.isdir(old_copyright_directory):
                list_of_files_in_dir = get_list_of_files_in_directory(old_copyright_directory)
                
                for old_copyright_file  in list_of_files_in_dir:
                        with open(old_copyright_file,"r") as foldcopy:
                                all_old_copyright_text.append(foldcopy.read())
        elif os.path.isfile(old_copyright_directory):
                all_old_copyright_text = old_copyright_directory
        
        return all_old_copyright_text


def update_copyright_text_all(new_copyright_file, src_code_directory, extn_list,old_copyright_directory,ignore_dirs=['build','bin']):
        import mmap
        import os
        # read the old & neew copyright text
        try:
               # get the list of old copyright texts & the new copyright text
                list_of_old_copyright_texts = get_all_old_copyright_text(old_copyright_directory)               
                with open(new_copyright_file,"r") as fnewcopy:
                        new_copyright_text = fnewcopy.read()  
                
                # get the list of src files to update
                list_of_files=[]
                for ext in extn_list:
                        list_of_files.extend(get_list_of_files_by_extension(src_code_directory,ext,ignore_dirs))
       
                for src_code_file in list_of_files:
                        # print(os.stat(src_code_file).st_size)                        
                        if (os.stat(src_code_file).st_size==0): # to handle the empty file
                                with open(src_code_file,"w") as fsrc:
                                        fsrc.write(new_copyright_text)
                        else:
                                with open(src_code_file,"r") as fsrc:
                                        with mmap.mmap(fsrc.fileno(), 0, access=mmap.ACCESS_READ) as m:
                                                # read the first 5000 bytes to compare. Don't need to parse the entire file for copyright
                                                content = m.read(5000)

                                        doPrepend = True
                                        #loop the list_of_old_copyright_texts & check if the src_code_file contains any of them
                                        for old_copyright_text in list_of_old_copyright_texts:                                                
                                                if(-1 != content.find(old_copyright_text[:].encode())):
                                                        replace_copyright_text_single(src_code_file,old_copyright_text,new_copyright_text)
                                                        doPrepend = False                                                        
                                                        break
                                        
                                        # avoid if the new copyright already exists        
                                        if doPrepend and (-1 == content.find(new_copyright_text[:].encode())):
                                                prepend_copyright_text_single(src_code_file,new_copyright_text)
                        
        except Exception as e:
               print(e)
       
###############################################################################

if __name__=="__main__":
    new_copyright_file = 'copyright.txt'
    old_copyright_file = './old_copyright_samples/old_copyright_2.txt'
    # src_code_file = 'test_1.cpp's
    # copyright_text = get_copyright_text(copyright_file)
    # print(copyright_text)
    # prepend_copyright_text(src_code_file,copyright_file)
###############################################################################    
    # get_list_of_files_to_update(src_code_directory)
#     extn = 'cpp'
#     list_of_files = get_list_of_files_by_extension(src_code_directory,extn)
    # print(list(list_of_files))
#     prepend_copyright_text_all(src_code_directory,copyright_file)
#     replace_copyright_text_all(old_copyright_file,new_copyright_file,src_code_directory,'cpp')

###############################################################################
#       src_code_directory = 'my_directory' 
#       ignore_dir = ['build'] 
#       extn = ['cpp','h']
#       get_list_of_files_by_extension(src_code_directory,extn,ignore_dir)

###############################################################################
    list_of_elements = ['~/coding/python-coding/1','~/coding/python-coding/2','~/trailers-py-2/AddCopyright/3']
    values = ['/1' ,'/2']
    get_filtered_list(list_of_elements,values)
###############################################################################
# #     old_copyright_directory = 'old_copyright_dir/old_copyright_2.txt'
#     old_copyright_directory = 'old_copyright_dir'
#     print(get_all_old_copyright_text(old_copyright_directory))