import subprocess
a=[]
git = ['git config user.name',
       'git config user.email',
       'git rev-parse HEAD']
for i in range(3):
    command_line = git[i]
    s = subprocess.run(command_line, stdout=subprocess.PIPE, shell=True)
    a.append(s)
    print(a[i].stdout)