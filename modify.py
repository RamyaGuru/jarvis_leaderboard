import os
print ('Running modify.py script')
# Read in the file
docs_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"docs")
index_path = os.path.join(docs_dir,'index.md')

with open(index_path, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('MkDocs', 'JARVIS-Leaderboard')

# Write the file out again
with open(index_path, 'w') as file:
  file.write(filedata)

"""
f=open('docs/index.md','r')
lines=f.read().splitlines()
f.close()
for i in lines:
 print (i)
"""
