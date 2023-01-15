import os
from jarvis.db.jsonutils import loadjson
from sklearn.metrics import mean_absolute_error
import pandas as pd
import glob

print("Running modify.py script")

root_dir = os.path.dirname(os.path.abspath(__file__))
clean = True

def get_metric_value(
    csv_path="", dataset="", prop="", data_split="", method="", metric=""
):
    results={}
    csv_data = pd.read_csv(csv_path)
    meta_path=csv_path.split('/')
    meta_path[-1]='metadata.json'
    meta_path='/'.join(meta_path)
    meta_data=loadjson(meta_path)
    results['model_name']=meta_data['model_name']
    results['team_name']=meta_data['team_name']
    results['date_submitted']=meta_data['date_submitted']
    
    print('meta_path',meta_data)
    #meta_data=loadjson()
    print ('csv_data',csv_path)
    temp = dataset + "_" + prop + ".json"
    fname = os.path.join("dataset", method, temp)
    json_data = loadjson(os.path.join(root_dir, fname))
    actual_data_json = json_data[data_split]
    data_size=len(json_data['train'])+len(json_data['val'])+len(json_data['test'])
    # print ('actual_data_json',actual_data_json)
    results['dataset_size']=data_size
    ids = []
    targets = []
    for i, j in actual_data_json.items():
        ids.append(i)
        targets.append(j)
    mem = {"id": ids, "actual": targets}
    actual_df = pd.DataFrame(mem)
    df = pd.merge(csv_data, actual_df, on="id")
    results['res']='na'
    if metric == "mae":
        res = round(mean_absolute_error(df["actual"], df["prediction"]),2)
        results['res']=res
    return results

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
    #print(
    #    fname,
    #    data_split,
    #    prop,
    #    dataset,
    #    method,
    #    metric,
    #    team,
    #    md_filename,
    #    md_path,
    #)
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
        + str(res['res'])
        + "</td>"
        + "<td>"
        + str(res['model_name'])
        + "</td>"
        + "<td>"
        + str(res['team_name'])
        + "</td>"
        + "<td>"
        + str(res['dataset_size'])
        + "</td>"
        + "<td>"
        + str(res['date_submitted'])
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