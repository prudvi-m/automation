
import os
import subprocess
import re
import psutil
import tempfile

def check_run():

    # dotnet run --urls "http://127.0.0.1:0"
    cmd = ['dotnet','run']
    cwd = os.getcwd() + f'/ContactManager/'

    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd,stdout=tempf, cwd=cwd,shell=True)
        print('ok')
        print(proc.returncode)
        tempf.seek(0)
        print(tempf.read())

if __name__ == '__main__':
    check_run()







# output = subprocess.Popen(cmd, stdout=subprocess.PIPE,cwd=cwd)
# output_result =  output.communicate()[0]
# content = str(output).replace('b\'','').replace('\'','').replace('\\n','\n')
# print(f"\n \nContactManager\n--------------------------------------------- \n \n")
# print(content)
# print()
# print("****************************************")
# print("\n \n")

