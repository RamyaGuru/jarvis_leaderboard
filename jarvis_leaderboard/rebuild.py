import os
from jarvis.db.jsonutils import loadjson
from sklearn.metrics import mean_absolute_error, accuracy_score
import pandas as pd
import glob
import zipfile
import json
from collections import defaultdict
import collections
import numpy as np


print("Running modify.py script")
root_dir = os.path.dirname(os.path.abspath(__file__))

clean = True
errors = []


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
    results["method"] = method
    results["submod"] = submod
    results["dataset"] = dataset
    results["prop"] = prop
    results["data_split"] = data_split
    results["csv_path"] = csv_path
    results["metric"] = metric
    csv_data = pd.read_csv(csv_path, sep=",")
    meta_path = csv_path.split("/")
    meta_path[-1] = "metadata.json"
    meta_path = "/".join(meta_path)
    meta_data = loadjson(meta_path)
    results["model_name"] = meta_data["model_name"]
    results["team_name"] = meta_data["team_name"]
    results["date_submitted"] = meta_data["date_submitted"]
    results["project_url"] = meta_data["project_url"]

    # print("meta_path", meta_data)
    # meta_data=loadjson()
    # print("csv_data", csv_path)
    # dataset with actual values
    temp = dataset + "_" + prop + ".json"
    temp2 = temp + ".zip"
    fname = os.path.join("dataset", method, submod, temp2)
    fname2 = os.path.join(root_dir, fname)

    z = zipfile.ZipFile(fname2)
    json_data = json.loads(z.read(temp))

    # json_data = loadjson(os.path.join(root_dir, fname))
    actual_data_json = json_data[data_split]
    if "val" in json_data:  # sometimes just train-test
        data_size = (
            len(json_data["train"])
            + len(json_data["val"])
            + len(json_data["test"])
        )
    else:
        data_size = len(json_data["train"]) + len(json_data["test"])
    # print ('actual_data_json',actual_data_json)
    results["dataset_size"] = data_size
    ids = []
    targets = []
    for i, j in actual_data_json.items():
        ids.append(i)
        targets.append(j)
    mem = {"id": ids, "actual": targets}
    actual_df = pd.DataFrame(mem)
    # print ('actual_df',actual_df)
    # print('csv_data',csv_data)
    # actual_df.to_csv('actual_df.csv')
    # csv_data.to_csv('csv_data.csv')
    if len(csv_data) != len(actual_df):
        print("Error", csv_path, len(csv_data), len(actual_df))
        errors.append(csv_path)

    df = pd.merge(csv_data, actual_df, on="id")
    # print('csv',csv_path)
    # print ('df',df)
    # print('csv_data',csv_data)
    # print('actual_df',actual_df)
    results["res"] = "na"
    if metric == "mae":
        res = round(mean_absolute_error(df["actual"], df["prediction"]), 3)
        results["res"] = res
    if metric == "acc":
        # print("ACC")
        # print(df, len(df))
        res = round(accuracy_score(df["actual"], df["prediction"]), 3)
        # print("res", res)
        results["res"] = res
    if metric == "multimae":
        print("csv multimae", csv_path)
        maes = []
        for k, v in df.iterrows():
            real = np.array(v["target"].split(";"), dtype="float")
            pred = np.array(v["prediction"].split(";"), dtype="float")
            m = mean_absolute_error(real, pred)
            maes.append(m)
            # print('mm',m)
        results["res"] = round(np.array(maes).sum(), 3)
        # print ('df',df)
        # print('csv_data',csv_data)
        # print('actual_df',actual_df)
        # print('res',results['res'])

    return results


for i in glob.glob("jarvis_leaderboard/benchmarks/*/*.csv.zip"):
    # if 'Text' in i:
    # print(i)
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
    print(i)
    print()
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
homepage = [
    "SinglePropertyPrediction-test-formation_energy_peratom-dft_3d-AI-mae",
    "SinglePropertyPrediction-test-optb88vdw_bandgap-dft_3d-AI-mae",
    "SinglePropertyPrediction-test-optb88vdw_total_energy-dft_3d-AI-mae",
    "SinglePropertyPrediction-test-bulk_modulus_kv-dft_3d-AI-mae",
    "MLFF-test-energy-alignn_ff_db-AI-mae",
    "ImageClass-test-bravais_class-stem_2d_image-AI-acc",
    "TextClass-test-categories-arXiv-AI-acc",
    "SinglePropertyPrediction-test-bulk_modulus-dft_3d-ES-mae",
    "SinglePropertyPrediction-test-bandgap-dft_3d-ES-mae",
    "SinglePropertyPrediction-test-epsx-dft_3d-ES-mae",
    "SinglePropertyPrediction-test-Tc_supercon-dft_3d-ES-mae",
    "SinglePropertyPrediction-test-slme-dft_3d-ES-mae",
    "EigenSolver-test-electron_bands-dft_3d-QC-multimae",
]
# print("dat", dat)
print("errors", errors, len(errors))
selected = defaultdict()
for name in homepage:
    for i in dat:
        name2 = (
            i["result"]["submod"]
            + "-"
            + i["result"]["data_split"]
            + "-"
            + i["result"]["prop"]
            + "-"
            + i["result"]["dataset"]
            + "-"
            + i["result"]["method"]
            + "-"
            + i["result"]["metric"]
        )
        if name == name2:
            temp = float(i["result"]["res"])
            i["result"]["team"] = i["team"]
            if name not in selected:
                selected[name] = i["result"]
            elif (
                temp > selected[name]["res"] and i["result"]["metric"] == "acc"
            ):
                selected[name] = i["result"]
            elif (
                temp < selected[name]["res"] and i["result"]["metric"] == "mae"
            ):
                selected[name] = i["result"]


"""
for i in dat:
    temp = float(i["result"]["res"])

    name = (
        i["result"]["submod"]
        + "-"
        + i["result"]["data_split"]
        + "-"
        + i["result"]["prop"]
        + "-"
        + i["result"]["dataset"]
        + "-"
        + i["result"]["method"]
        + "-"
        + i["result"]["metric"]
    )
    i["result"]["team"] = i["team"]
    if name in homepage:
        # print (i['result'])
        if name not in selected:
            selected[name] = i["result"]
        elif temp > selected[name]["res"] and i["result"]["metric"] == "acc":
            selected[name] = i["result"]
        elif temp < selected[name]["res"] and i["result"]["metric"] == "mae":
            selected[name] = i["result"]

"""
# print("selected", selected)
temp = (
    '<!--table_content--><table style="width:100%" id="j_table">'
    + "<thead><tr>"
    + "<th>Method</th>"
    # +'<th><a href="./method' + '" target="_blank">' + 'Method' + "</a></th>"
    + "<th>Task</th>"
    + "<th>Property</th>"
    + "<th>Model name</th>"
    + "<th>Metric</th>"
    + "<th>Score</th>"
    + "<th>Team</th>"
    + "<th>Size</th>"
    + "</tr></thead>"
)
for i, j in selected.items():
    temp = (
        temp
        + "<tr>"
        + "<td>"
        + '<a href="./'
        + j["method"]
        + '" target="_blank">'
        + j["method"]
        + "</a>"
        # + j["method"]
        + "</td>"
        + "<td>"
        + '<a href="./'
        + j["method"]
        + "/"
        + j["submod"]
        + '" target="_blank">'
        + j["submod"]
        + "</a>"
        # + j["submod"]
        + "</td>"
        + "<td>"
        + '<a href="./'
        + j["method"]
        + "/"
        + j["submod"]
        + "/"
        + j["prop"]
        + '" target="_blank">'
        + j["prop"]
        + "</a>"
        # + j["prop"]
        + "</td>"
        + "<td>"
        + j["team"]
        + "</td>"
        + "<td>"
        + str(j["metric"].upper())
        + "</td>"
        + "<td>"
        + str(j["res"])
        + "</td>"
        + "<td>"
        + str(j["team_name"])
        + "</td>"
        + "<td>"
        + str(j["dataset_size"])
        + "</td>"
        # + "<td>"
        # + str(j["date_submitted"])
        # + "</td>"
        + "</tr>"
    )


md_path = "docs/index.md"


with open(md_path, "r") as file:
    filedata = file.read().splitlines()
content = []
for j in filedata:
    if "<!--table_content-->" in j:
        content.append("<!--table_content-->")
    elif "<!--number_of_benchmarks-->" in j:
        content.append("<!--number_of_benchmarks-->")
    else:
        content.append(j)
with open(md_path, "w") as file:
    file.write("\n".join(content))


with open(md_path, "r") as file:
    filedata = file.read().splitlines()
content = []
for j in filedata:
    if "<!--table_content-->" in j:
        temp = temp + j + "</table>"
        content.append(temp)
    elif "<!--number_of_benchmarks-->" in j:
        temp2 = (
            "<!--number_of_benchmarks--> - Number of benchmarks: "
            + str(len(dat))
            + "\n"
        )
        content.append(temp2)
    else:
        content.append(j)
# filedata = filedata.replace('<!--table_content-->', temp)

with open(md_path, "w") as file:
    file.write("\n".join(content))
    # + "<td>"
    # + method
    # + "</td>"
    # + "<td>"
    # + str(res['model_name'])
    # + "</td>"
# print(temp)
