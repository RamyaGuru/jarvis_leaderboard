import os
from jarvis.db.jsonutils import loadjson
from sklearn.metrics import mean_absolute_error
import pandas as pd
import glob

print("Running modify.py script")

root_dir = os.path.dirname(os.path.abspath(__file__))
clean = True

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
        filedata = file.read().splitlines()
    content = []
    for j in filedata:
        if "<!--table_content-->" in j:
            content.append("<!--table_content-->")
        else:
            content.append(j)
    with open(md_path, "w") as file:
        file.write("\n".join(content))
# jarvis_leaderboard/dataset/AI/dft_3d_exfoliation_energy.json
def get_metric_value(
    csv_path="", dataset="", prop="", data_split="", method="", metric=""
):

    csv_data = pd.read_csv(csv_path)
    # print ('csv_data',csv_data)
    temp = dataset + "_" + prop + ".json"
    fname = os.path.join("dataset", method, temp)
    actual_data_json = loadjson(os.path.join(root_dir, fname))[data_split]
    # print ('actual_data_json',actual_data_json)
    ids = []
    targets = []
    for i, j in actual_data_json.items():
        ids.append(i)
        targets.append(j)
    mem = {"id": ids, "actual": targets}
    actual_df = pd.DataFrame(mem)
    df = pd.merge(csv_data, actual_df, on="id")
    if metric == "mae":
        res = mean_absolute_error(df["actual"], df["prediction"])
    return res


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
        filedata = file.read().splitlines()

    res = get_metric_value(
        csv_path=i,
        dataset=dataset,
        prop=prop,
        data_split=data_split,
        method=method,
        metric=metric,
    )
    # res = 5
    # if clean:

    temp = (
        "<!--table_content-->"
        + "<tr>"
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
        + "</td>"
        + "</tr>"
    )
    # temp='<!--table_content-->\n'+'<td>'+team+'</td>'+'<td>'+method+'</td>'+'<td>'+str(res)+'</td>'+'<td>'+str(res)+'</td>'+'<td>'+str(res)+'</td>\n'
    content = []
    for j in filedata:
        if "<!--table_content-->" in j:
            temp = temp + j
            content.append(temp)
        else:
            content.append(j)
    # filedata = filedata.replace('<!--table_content-->', temp)

    with open(md_path, "w") as file:
        file.write("\n".join(content))
