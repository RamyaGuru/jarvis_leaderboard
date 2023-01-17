

[LICENSE]: https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst

# JARVIS Leaderboard
This project benchmarks performances of various methods for materials science applications using the datasets available in [JARVIS-Tools databases](https://jarvis-tools.readthedocs.io/en/master/databases.html).
In addition to prediction results, we attempt to capture the underlyig software and hardware frameworks in training models to enhance reproducibility.
Currently, there are  x number of benchmarks available.




## Getting Started

To get started, first fork this repository by clicking on the Fork button [`Fork`](https://github.com/knc6/jarvis_leaderboard/fork). 
On the new screen, give your repository a name and make sure to check `Include all branches`/ uncehck `Copy the master branch only`. 





## Adding model benchmarks to existing dataset
To add a new benchmark, 

1) Create a folder in the `jarvis_leaderboard/benchmarks` folder under respective submodule e.g. `xyz_model`. 

2) In the `xyz_model` folder, add comma-separated zip file(`.csv.zip`) file(s) corresponding to benchmark(s), 
e.g. `PP-test-exfoliation_energy-dft_2d-AI-mae.csv.zip` for `exfoliation_energy` in `dft_3d` dataset for `test` split using an `AI` (artificial intelligence method) with 
`mae` (mean absolute error) metric for `PP` (property prediction) task. Therefore, the filename should have these six components. 

Note the word: `PP`:task type, `test`, property: `exfoliation_energy`, dataset: `dft_3d`, method: `AI`, metric: `mae`
have been joined with '-' sign. This format should be used for consistency in webpage generation.
The test data splits are pre-determined, if the exact test IDs are not used, then the code might result in errors. 


3) Add at least two columns: `id` and `prediction` in the csv file using your model. The `jarvis_leaderboard/rebuild.py` script will parse the data in the csv.zip file, and
will calculate and analyze several metrics. The `id `should be identifier in the test split set and `prediction` is your model prediction.

We recommend to name this folder as your model name, e.g. `alignn_models`, `cfid_models`, `cgcnn_models` etc. 

3) Make a pull-request to the original repo.

## Adding model benchmarks to new dataset
To add a new dataset

1) Create a `json.zip` file in the `jarvis_leaderboard/dataset` folder under respective submodule e.g. `jarvis_leaderboard/dataset/AI/PP/dft_3d_exfoliation_energy.json.zip`.

2) In the `.json` file should have `train`, `val`, `test` keys with array of ids and their values. An example for creating such a file is provided in `jarvis_leaderboard/dataset/AI/PP/format_data.py` 

3) Add a `.md` file in `docs` folder with path to respective submodule e.g., `docs/AI/PP/exfoliation_energy.md` 
## License
This template is served under the NIST license.  
Read the [LICENSE] file for more info.
