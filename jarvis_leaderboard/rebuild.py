import os
from jarvis.db.jsonutils import loadjson
from sklearn.metrics import mean_absolute_error
import pandas as pd
import glob
import zipfile
import json

print("Running modify.py script")

root_dir = os.path.dirname(os.path.abspath(__file__))
clean = True


def get_metric_value(
    submod="",
    csv_path="",
    dataset="",
    prop="",
    data_split="",
    method="",
    metric="",
):
    results = {}
    csv_data = pd.read_csv(csv_path)
    meta_path = csv_path.split("/")
    meta_path[-1] = "metadata.json"
    meta_path = "/".join(meta_path)
    meta_data = loadjson(meta_path)
    results["model_name"] = meta_data["model_name"]
    results["team_name"] = meta_data["team_name"]
    results["date_submitted"] = meta_data["date_submitted"]
    results["project_url"] = meta_data["project_url"]

    print("meta_path", meta_data)
    # meta_data=loadjson()
    print("csv_data", csv_path)
    # dataset with actual values
    temp = dataset + "_" + prop + ".json"
    temp2 = temp + ".zip"
    fname = os.path.join("dataset", method, submod, temp2)
    fname2 = os.path.join(root_dir, fname)

    z = zipfile.ZipFile(fname2)
    json_data = json.loads(z.read(temp))

    # json_data = loadjson(os.path.join(root_dir, fname))
    actual_data_json = json_data[data_split]
    data_size = (
        len(json_data["train"])
        + len(json_data["val"])
        + len(json_data["test"])
    )
    # print ('actual_data_json',actual_data_json)
    results["dataset_size"] = data_size
    ids = []
    targets = []
    for i, j in actual_data_json.items():
        ids.append(i)
        targets.append(j)
    mem = {"id": ids, "actual": targets}
    actual_df = pd.DataFrame(mem)
    df = pd.merge(csv_data, actual_df, on="id")
    results["res"] = "na"
    if metric == "mae":
        res = round(mean_absolute_error(df["actual"], df["prediction"]), 3)
        results["res"] = res
    return results


for i in glob.glob("jarvis_leaderboard/benchmarks/*/*.csv.zip"):
    print(i)
    fname = i.split("/")[-1].split(".csv.zip")[0]
    temp = fname.split("-")
    submod = temp[0]
    data_split = temp[1]
    prop = temp[2]
    dataset = temp[3]
    method = temp[4]
    metric = temp[5]
    team = i.split("/")[-2]
    # md_filename = os.path.join("../docs",method,submod,prop) #"../docs/" + method + "/" +submod+"/"+ prop + ".md"
    md_filename = "../docs/" + method + "/" + submod + "/" + prop + ".md"
    md_path = os.path.join(root_dir, md_filename)
    # print(
    #    fname,
    #    data_split,
    #    prop,
    #    dataset,
    #    method,
    #    metric,
    #    team,
    #    md_filename,
    #    md_path,
    # )
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
dat = []
for i in glob.glob("jarvis_leaderboard/benchmarks/*/*.csv.zip"):
    fname = i.split("/")[-1].split(".csv.zip")[0]
    temp = fname.split("-")
    submod = temp[0]
    data_split = temp[1]
    prop = temp[2]
    dataset = temp[3]
    method = temp[4]
    metric = temp[5]
    team = i.split("/")[-2]
    md_filename = "../docs/" + method + "/" + submod + "/" + prop + ".md"
    md_path = os.path.join(root_dir, md_filename)
    notes = ""
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
        submod=submod,
        csv_path=i,
        dataset=dataset,
        prop=prop,
        data_split=data_split,
        method=method,
        metric=metric,
    )
    # res = 5
    # if clean:
    team = (
        '<a href="' + res["project_url"] + '" target="_blank">' + team + "</a>"
    )
    # team='['+team+']'+'('+res['project_url']+')'
    info = {}
    temp = (
        "<!--table_content-->"
        + "<tr>"
        + "<td>"
        + team
        + "</td>"
        # + "<td>"
        # + method
        # + "</td>"
        + "<td>"
        + str(res["res"])
        + "</td>"
        # + "<td>"
        # + str(res['model_name'])
        # + "</td>"
        + "<td>"
        + str(res["team_name"])
        + "</td>"
        + "<td>"
        + str(res["dataset_size"])
        + "</td>"
        + "<td>"
        + str(res["date_submitted"])
        + "</td>"
        + "<td>"
        + str(notes)
        + "</td>"
        + "</tr>"
    )
    info["team"] = team
    info["result"] = res
    dat.append(info)
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

print("dat", dat)
