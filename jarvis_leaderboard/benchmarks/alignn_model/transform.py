import glob, os
import zipfile, json
from jarvis.db.jsonutils import dumpjson
from format_data import preapre_json_file
import pandas as pd
from io import StringIO

jl_path = ""
pp = list(
    set(
        [
            "avg_elec_mass",
            "avg_hole_mass",
            "bulk_modulus_kv",
            "dfpt_piezo_max_dielectric",
            "dfpt_piezo_max_dij",
            "dfpt_piezo_max_eij",
            "ehull",
            "encut",
            "epsx",
            "epsy",
            "epsz",
            "exfoliation_energy",
            "formation_energy_peratom",
            "kpoint_length_unit",
            "magmom_oszicar",
            "magmom_oszicar",
            "max_efg",
            "mbj_bandgap",
            "mbj_bandgap",
            "mepsx",
            "mepsy",
            "mepsz",
            "n-powerfact",
            "n-powerfact",
            "n-Seebeck",
            "optb88vdw_bandgap",
            "optb88vdw_bandgap",
            "optb88vdw_total_energy",
            "shear_modulus_gv",
            "slme",
            "spillage",
        ]
    )
)
# pp=['slme','spillage','shear_modulus_gv']
x = []
for i in glob.glob(
    "/mnt/c/Users/knc6/OneDrive - NIST/KamalLaptop/JARVIS-ALIGNN/Models/17005681/*.zip"
):
    if "supercon" not in i:
        p = (
            i.split("/")[-1]
            .split(".zip")[0]
            .split("jv_")[1]
            .split("_alignn")[0]
        )
        if p in pp:
            model_zipfile = (
                "/mnt/c/Users/knc6/OneDrive - NIST/KamalLaptop/JARVIS-ALIGNN/Models/17005681/jv_"
                + p
                + "_alignn.zip"
            )
            model_zip = zipfile.ZipFile(model_zipfile)
            print("model_zipfile", model_zipfile, model_zip.namelist())
            temp = "jv_" + p + "_alignn/ids_train_val_test.json"
            train_val_test = json.loads(model_zip.read(temp))

            #dumpjson(filename='ids_train_val_test.json',data=train_val_test)
            #preapre_json_file(prop=p)
            #cmd='rm ids_train_val_test.json'
            #os.system(cmd)

            fname=p.replace('n-','n_')+'.md'
            f=open(fname,'w')
            line='# Model for '+p+'\n\n'
            f.write(line)
            line='<h2>Model benchmarks</h2>\n\n<table style="width:100%" id="j_table">\n <thead>\n  <tr>\n    <th>Model name</th>\n   <!-- <th>Method</th>-->\n    <th>MAE</th>\n    <th>Team name</th>\n    <th>Dataset size</th>\n    <th>Date submitted</th>\n    <th>Notes</th>\n  </tr>\n </thead>\n<!--table_content-->\n</table>\n'
            f.write(line)
            f.close()
            temp = "jv_" + p + "_alignn/prediction_results_test_set.csv"
            p = p.replace('n-','n_') #For n-seebeck etc
            fname = "SinglePropertyPrediction-test-" + p + "-dft_3d-AI-mae.csv"
            f = open(fname, "wb")
            f.write(model_zip.read(temp))
            f.close()
            # df=pd.read_csv(StringIO(model_zip.read(temp)))
            # print (df)
            # print(i,len(train_val_test))
            x.append(p)
print(x)

import os,glob
for i in glob.glob('*csv'):
  cmd='zip '+i+'.zip '+i
  os.system(cmd)
