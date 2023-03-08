import os
import subprocess
# import tempfile
# with tempfile.TemporaryFile() as tempf:
#     proc = subprocess.Popen(cmd, stdout=tempf, cwd="ContactManager")
#     proc.wait()
#     tempf.seek(0)
#     print(tempf.read())
    


import subprocess

cmd = ['dotnet','build']
cwd = os.getcwd() + '/ContactManager/'
output = subprocess.Popen(cmd, stdout=subprocess.PIPE,cwd=cwd).communicate()[0]
content = str(output).replace('b\'','').replace('\'','').replace('\\n','\n') + "\n#################"
f = open("../result.txt", "a")
f.write(content)
print(content)


