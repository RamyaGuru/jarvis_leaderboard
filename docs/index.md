

[LICENSE]: https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst

# JARVIS Leaderboard [WIP]

This project provides benchmark-performances of various methods for materials science applications using the datasets available in [JARVIS-Tools databases](https://jarvis-tools.readthedocs.io/en/master/databases.html).
In addition to prediction results, we attempt to capture the underlyig software and hardware frameworks in training models to enhance reproducibility. This project is a part of the [NIST-JARVIS](https://jarvis.nist.gov) infrastructure.


<!--number_of_benchmarks-->Number of benchmarks: 49



<!-- <p style="text-align:center;"><img align="middle" src="https://www.ctcms.nist.gov/~knc6/images/logo/jarvis-mission.png"  width="40%" height="20%"></p>-->


# Examples of benchmarks
<!--table_content--><table style="width:100%" id="j_table"><thead><tr><th>Method</th><th>Task</th><th>Property</th><th>Model name</th><th>Metric</th><th>Score</th><th>Team</th><th>Size</th></tr></thead><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/formation_energy_peratom" target="_blank">formation_energy_peratom</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">alignn_model</a></td><td>MAE</td><td>0.033</td><td>JARVIS</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/optb88vdw_bandgap" target="_blank">optb88vdw_bandgap</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">alignn_model</a></td><td>MAE</td><td>0.142</td><td>JARVIS</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/MLFF" target="_blank">MLFF</a></td><td><a href="./AI/MLFF/energy" target="_blank">energy</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">alignnff_model</a></td><td>MAE</td><td>0.097</td><td>JARVIS</td><td>307111</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/ImageClass" target="_blank">ImageClass</a></td><td><a href="./AI/ImageClass/bravais_class" target="_blank">bravais_class</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">densenet_model</a></td><td>ACC</td><td>0.83</td><td>JARVIS</td><td>9150</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/TextClass" target="_blank">TextClass</a></td><td><a href="./AI/TextClass/categories" target="_blank">categories</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">logisticreg_model</a></td><td>ACC</td><td>0.86</td><td>JARVIS</td><td>100994</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/bulk_modulus" target="_blank">bulk_modulus</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">vasp_optb88vdw</a></td><td>MAE</td><td>5.732</td><td>JARVIS</td><td>21</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/bandgap" target="_blank">bandgap</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">vasp_tbmbj</a></td><td>MAE</td><td>0.498</td><td>JARVIS</td><td>54</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/epsx" target="_blank">epsx</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">vasp_optb88vdw_linopt</a></td><td>MAE</td><td>1.464</td><td>JARVIS</td><td>16</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/Tc_supercon" target="_blank">Tc_supercon</a></td><td><a href="https://github.com/usnistgov/alignn" target="_blank">qe_pbesol_gbrv</a></td><td>MAE</td><td>3.378</td><td>JARVIS</td><td>14</td></tr><!--table_content--></table>

# Adding benchmarks and datasets

To get started, first fork this repository by clicking on the Fork button [`Fork`](https://github.com/knc6/jarvis_leaderboard/fork). 


## A) Adding model benchmarks to existing dataset

     To add a new benchmark, 

     1) Populate the dataset for a particular task+method+dataset using script such as `python jarvis_leaderboard/populate_data.py`. 

     2) Develop your model(s) using this dataset,

     3) Create a folder in the `jarvis_leaderboard/benchmarks` folder under respective submodule e.g. `xyz_model`. 

     4) In the `xyz_model` folder, add comma-separated zip file (`.csv.zip`) file(s) corresponding to benchmark(s), 
     e.g. `SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv.zip` for `exfoliation_energy` in `dft_3d` dataset for `test` split using an `AI` (artificial intelligence method) with 
    `mae` (mean absolute error) metric for `SinglePropertyPrediction` (single property prediction) task. Therefore, the filename should have these six components. 

    Note the word: `SinglePropertyPrediction`: task type, `test`, property: `exfoliation_energy`, dataset: `dft_3d`, method: `AI`, metric: `mae`
    have been joined with '-' sign. This format should be used for consistency in webpage generation.
    The test data splits are pre-determined, if the exact test IDs are not used, then the code might result in errors. 


    5) Add at least two columns: `id` and `prediction` in the csv file using your model. The `jarvis_leaderboard/rebuild.py` script will parse the data in the csv.zip file, and
    will calculate and analyze several metrics. The `id `should be identifier in the test split set and `prediction` is your model prediction.

    We recommend to name this folder as your model name, e.g. `alignn_models`, `cfid_models`, `cgcnn_models` etc. 

    6) Add metadata info in the `metadata.json` file, an example is given in the `jarvis_leaderboard/benchmarks/alignn_models/metadata.json`. Also, add a `run.py` and `run.sh` scripts to reproduce the model predictions.

    7) Make a pull-request to the original repo.

## B) Adding model benchmarks and a new dataset

    To add a new dataset

    1) Create a `json.zip` file in the `jarvis_leaderboard/dataset` folder under respective submodule e.g. `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/dft_3d_exfoliation_energy.json.zip`.

    2) In the `.json` file should have `train`, `val`, `test` keys with array of ids and their values. An example for creating such a file is provided in `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/format_data.py` 

    3) Add a `.md` file in `docs` folder with path to respective submodule e.g., `docs/AI/SinglePropertyPrediction/exfoliation_energy.md` 

# License
   This template is served under the NIST license.  
   Read the [LICENSE] file for more info.