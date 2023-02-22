[LICENSE]: https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst

# JARVIS Leaderboard 
Now moved to [https://pages.nist.gov/jarvis_leaderboard/](https://pages.nist.gov/jarvis_leaderboard/).

<!-- This project provides benchmark-performances of various methods for materials science applications using the datasets available in [JARVIS-Tools databases](https://jarvis-tools.readthedocs.io/en/master/databases.html). Some of the methods are: [Artificial Intelligence (AI)](./AI), [Electronic Structure (ES)](./ES) and [Qunatum Computation (QC](./QC)). There are a variety of properties included in the benchmark.
In addition to prediction results, we attempt to capture the underlyig software and hardware frameworks in training models to enhance reproducibility. This project is a part of the [NIST-JARVIS](https://jarvis.nist.gov) infrastructure. -->


<!--#_of_benchmarks--> 
<!-- - [Learn how to add benchmarks below](#add) -->
<!-- <p style="text-align:center;"><img align="middle" src="https://www.ctcms.nist.gov/~knc6/images/logo/jarvis-mission.png"  width="40%" height="20%"></p>-->


<!-- # Examples of benchmarks -->
<!--#_content-->
<!-- <a name="add"></a>
# Adding benchmarks and datasets

To get started, first fork this repository by clicking on the [`Fork`](https://github.com/knc6/jarvis_leaderboard/fork) button. 

Then, clone your forked repository and install the project. Note instead of knc6, use your own username,

```
git clone https://github.com/knc6/jarvis_leaderboard
cd jarvis_leaderboard
python setup.py develop
```

## A) Adding model benchmarks to existing dataset

     To add a new benchmark, 

     1) Populate the dataset for a particular exisiting benchmar e.g.:
     `python jarvis_leaderboard/populate_data.py --benchmark_file SinglePropertyPrediction-test-exfoliation_energy-dft_3d-AI-mae --output_path=Out`
      This will generate an `id_prop.csv` file in the `Out` directory and other pertinent files such as POSCAR files for atomistic properties.
      The code will also print number of training, val and test samples.
      For methods other than AI method, only test set is provided.
      The reference data for ES is from experiments only.

     2) Develop your model(s) using this dataset, e.g.:
     `pip install alignn`
     `train_folder.py --root_dir "Out" --config "alignn/examples/sample_data/config_example.json" --output_dir=temp`

     3) Create a folder in the `jarvis_leaderboard/benchmarks` folder under respective submodule e.g. `xyz_model`. 

     4) In the `xyz_model` folder, add comma-separated zip file (`.csv.zip`) file(s) corresponding to benchmark(s), 
     e.g. `SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv.zip` for `exfoliation_energy` in `dft_3d`
     dataset for `test` split using an `AI` (artificial intelligence method) with 
     `mae` (mean absolute error) metric for `SinglePropertyPrediction` (single property prediction) task. 
     Therefore, the filename should have these six components. 

     Note the word: `SinglePropertyPrediction`: task type, `test`, property: `exfoliation_energy`, dataset: `dft_3d`, 
     method: `AI`, metric: `mae` have been joined with '-' sign. 
     This format should be used for consistency in webpage generation.
     The test data splits are pre-determined, if the exact test IDs are not used, then the code might result in errors. 


     5) Add at least two columns: `id` and `prediction` in the csv file using your model. 
     The `jarvis_leaderboard/rebuild.py` script will parse the data in the csv.zip file, and
     will calculate and analyze several metrics. 
     The `id `should be identifier in the test split set and `prediction` is your model prediction.

     e.g.: for the above alignn example:
     `cp temp/prediction_results_test_set.csv SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv`
     Then zip the file:
     `zip SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv.zip SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv`

     We recommend to name this folder as your model name, e.g. `alignn_models`, `cfid_models`, `cgcnn_models` etc. 

     6) Add metadata info in the `metadata.json` file, an example is given in the 
     `jarvis_leaderboard/benchmarks/alignn_models/metadata.json`. 
     Also, add a `run.py` and `run.sh` scripts to reproduce the model predictions.
   
     The `project_url` in metadata.json should have link to a paper/GitHub URL.

     7) Make a pull-request to the original repo.

## B) Adding model benchmarks and a new dataset

     To add a new dataset

     1) Create a `json.zip` file in the `jarvis_leaderboard/dataset` folder under respective submodule 
     e.g. `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/dft_3d_exfoliation_energy.json.zip`.

     2) In the `.json` file should have `train`, `val`, `test` keys with array of ids and their values. 
     An example for creating such a file is provided in `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/format_data.py` 

     3) Add a `.md` file in `docs` folder with path to respective submodule e.g., 
     `docs/AI/SinglePropertyPrediction/exfoliation_energy.md` 

# License
   This template is served under the NIST license.  
   Read the [LICENSE] file for more info. -->