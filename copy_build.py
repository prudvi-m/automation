
import os, zipfile
import subprocess
import re


# dir_name = os.getcwd()
# extension = ".zip"

# os.chdir(dir_name) # change directory from working dir to dir with files

# for item in os.listdir(dir_name): # loop through items in dir
#     if item.endswith(extension): # check for ".zip" extension
#         file_name = os.path.abspath(item) # get full path of files
#         zip_ref = zipfile.ZipFile(file_name) # create zipfile object
#         zip_ref.extractall(dir_name) # extract file to dir
#         zip_ref.close() # close file
#         # os.remove(file_name) # delete zipped file




def check_build(folder):
    cmd = ['dotnet','build']
    cwd = os.getcwd() + f'/{folder}/'
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE,cwd=cwd).communicate()[0]
    content = str(output).replace('b\'','').replace('\'','').replace('\\n','\n')
    print(f"\n \n{folder}\n--------------------------------------------- \n \n")
    print(content)
    print("\n****************************************\n \n")
    return content


worked = []
ls_list = os.listdir()
for ls_name in ls_list:
    if not '.' in ls_name:
        content = check_build(ls_name)
        if re.search('Build succeeded.',content):
            worked.append(ls_name)

print("worked Projects: " ,worked)