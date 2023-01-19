#!/usr/bin/env python

"""Module to train for a folder with formatted dataset."""
import csv
import os
import sys
import time
import json
import zipfile
from jarvis.core.atoms import Atoms
from jarvis.db.jsonutils import loadjson
import argparse
from jarvis.db.figshare import data

parser = argparse.ArgumentParser(description="JARVIS-Leaderboard")
parser.add_argument(
    "--dataset",
    default="dft_3d",
    help="JARVIS-Tools based dataset to use.",
)
parser.add_argument(
    "--output_path",
    default="DataPath",
    help="Path for storing the training data.",
)

parser.add_argument(
    "--prop",
    default="exfoliation_energy",
    help="Property/key in the dataset to select.",
)

parser.add_argument("--method", default="AI", help="Select method AI etc...")

parser.add_argument(
    "--task", default="PP", help="Select task: propert-prediction (PP) etc...."
)
parser.add_argument(
    "--id_tag",
    default="jid",
    help="Item itentfier tag in the dataset.",
)


def get_val(df=None, id_tag="jid", prop="", jv_id="JVASP-14441"):
    """Get data from dataframe."""
    return df[df[id_tag] == jv_id][prop].values[0]


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    dataset = args.dataset
    output_path = args.output_path
    prop = args.prop
    method = args.method
    task = args.task
    id_tag = args.id_tag
    temp = dataset + "_" + prop + ".json.zip"
    temp2 = dataset + "_" + prop + ".json"
    fname = os.path.join("jarvis_leaderboard", "dataset", method, task, temp)
    print(fname)
    if dataset in ["dft_3d", "dft_2d"]:
        dat = data(dataset)
        info = {}
        for i in dat:
            info[i[id_tag]] = Atoms.from_dict(i["atoms"])

        zp = zipfile.ZipFile(fname)
        train_val_test = json.loads(zp.read(temp2))
        # print(train_val_test)
        train = train_val_test["train"]
        val = train_val_test["val"]
        test = train_val_test["test"]
        cwd = os.getcwd()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # os.chdir(output_path)
        id_prop = os.path.join(output_path, "id_prop.csv")
        f = open(id_prop, "w")
        for i, j in train.items():
            line = str(i) + ".vasp" + "," + str(j) + "\n"
            f.write(line)
            pos_name = os.path.join(output_path, str(i) + ".vasp")
            info[i].write_poscar(pos_name)
        for i, j in val.items():
            line = str(i) + ".vasp" + "," + str(j) + "\n"
            f.write(line)
            pos_name = os.path.join(output_path, str(i) + ".vasp")
            info[i].write_poscar(pos_name)

        for i, j in test.items():
            line = str(i) + ".vasp" + "," + str(j) + "\n"
            f.write(line)
            pos_name = os.path.join(output_path, str(i) + ".vasp")
            info[i].write_poscar(pos_name)
        f.close()
        # os.chdir(cwd)
# jarvis_leaderboard/dataset/AI/PP/dft_3d_exfoliation_energy.json.zip
