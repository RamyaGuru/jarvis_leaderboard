

[LICENSE]: https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst

# JARVIS Leaderboard
This project benchmarks performances of various methods for materials science applications using the datasets available in [JARVIS-Tools databases](https://jarvis-tools.readthedocs.io/en/master/databases.html).
In addition to prediction results, we attempt to capture the underlyig software and hardware frameworks in training models to enhance reproducibility.
Currently, there are  x number of benchmarks available.




## Getting Started

To get started, first fork this repository by clicking on the Fork button [`Fork`](https://github.com/knc6/jarvis_leaderboard/fork). 
On the new screen, give your repository a name and make sure to check `Include all branches`/ uncehck `Copy the master branch only`. 





## Adding new model benchmarks
To add a new benchmark, 

1) Create a folder in the `benchmarks` folder e.g. `my_benchmarks`. 

2) In the `my_benchmarks` folder, add comma-separated (`.csv`) file(s) corresponding to benchmark(s), 
e.g. `test-exfoliation_energy-dft_2d-ai-mae.csv` for `exfoliation_energy` in `dft_2d` dataset for `test` split using an `ai` (artificial intelligence method) with 
`mae` (mean absolute error) metric. Therefore, the filename should have these five components. 

Note the word: test, property: exfoliation_energy, dataset: dft_2d, method: ai, metric: ai
have been joined with '-' sign. This format should be used for consistency in webpage generation.
The test data splits are pre-determined, if the exact test IDs are not used, then the code will result in errors. 


3) Add at least two columns: `id` and `prediction` in the csv file using your model. The `rebuild_page.py` script will parse the data in the csv file, and
will calculate and analyze several metrics. The `id `should be identifier in the test split set and `prediction` is your model prediction.

An example, `my_benchmarks_test` is added in the GitHub repo for demo purpose only. 
We recommend to name this folder as your model name, e.g. `alignn_models`, `cfid_models`, `cgcnn_models` etc. 

3) Make a pull-request to the original repo.

## License
This template is served under the NIST license.  
Read the [LICENSE] file for more info.
