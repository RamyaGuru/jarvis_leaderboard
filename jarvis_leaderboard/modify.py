import os

print("Running modify.py script")
import pandas as pd
import glob

root_dir = os.path.dirname(os.path.abspath(__file__))
for i in glob.glob("jarvis_leaderboard/benchmarks/*/*.csv"):
    fname = i.split("/")[-1].split(".csv")[0]
    temp = fname.split("-")
    data_split = temp[0]
    prop = temp[1]
    dataset = temp[2]
    method = temp[3]
    metric = temp[4]
    team = i.split("/")[-2]
    md_filename = "../docs/" + method + "/" + prop + ".md"
    md_path = os.path.join(root_dir, md_filename)
    print(
        fname,
        data_split,
        prop,
        dataset,
        method,
        metric,
        team,
        md_filename,
        md_path,
    )
    with open(md_path, "r") as file:
        filedata = file.read()
    res = 5
    temp = (
        "<!--table_content-->\n"
        + "<td>"
        + team
        + "</td>"
        + "<td>"
        + method
        + "</td>"
        + "<td>"
        + str(res)
        + "</td>"
        + "<td>"
        + str(res)
        + "</td>"
        + "<td>"
        + str(res)
        + "</td>\n"
    )
    filedata = filedata.replace("<!--table_content-->", temp)
    with open(md_path, "w") as file:
        file.write(filedata)
"""
# Read in the file
docs_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"../docs")
index_path = os.path.join(docs_dir,'index.md')

with open(index_path, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('MkDocs', 'JARVIS-Leaderboard')

# Write the file out again
with open(index_path, 'w') as file:
  file.write(filedata)
"""
