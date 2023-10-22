## aad64_Pandas-Script


# Week 2 Mini-Project ![example workflow](https://github.com/nogibjj/aad64_Pandas-Script/actions/workflows/actions.yml/badge.svg)

This assignment is designed to introduce us to pandas descriptive scripts. For the same, the main edit made was to add pandas==2.1.0 to my requirements.txt file.

Here, I have created a project which has functions dedicated to doing the following on a given dataset and returning the output: 
* Calculating the `mean`,
* Calculating the `median`,
* Calculating the `standard deviation`,
* Displaying the overall `summmary statistics` of a dataset.
<p align = "center"><img width="580" alt="Screenshot 2023-09-11 at 11 47 40 AM" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/b0795143-b33d-461f-8459-3859896b7978"></p>

* `Visualizing` data in the form of a _scatterplot_ (below is the function run on a small, example dataset created in the [test_main.py](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/test_main.py) file).

<p align = "center"><img src = "https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/440f1749-e4bf-49e2-80cf-c4f55efae6af" width = 500px></p>

I have also created a test file to ensure that the mean, median, and standard deviation functions are correctly functioning (using asserts).

The contents of this project are: 
* `.devcontainer` (with a [devcontainer.json](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/.devcontainer/devcontainer.json) and a [Dockerfile](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/.devcontainer/Dockerfile)), 
* [Github Actions](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/.github/workflows/actions.yml), 
* `.gitignore file`, 
* [Makefile](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/Makefile), 
* [requirements.txt](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/requirements.txt), 
* [main.py](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/main.py), 
* [test_main.py](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/test_main.py), and 
* [iris.csv](https://github.com/nogibjj/aad64_Pandas-Script/edit/main/iris.csv).

As visible below, my project is passing all formatting, linting, and tests:

### Linting
<p align = "center"><img width="417" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/d1ba1d1e-b29d-401c-a3fc-2d00b1569df3"></p>

### Formatting
<p align = "center"><img width="407" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/00680819-8369-44f1-b55f-6e30ce41da3f"></p>

### Testing
<p align = "center"><img width="1277" alt="Screenshot 2023-09-11 at 11 53 40 AM" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/6e4f0fce-c5b7-440b-9278-4ab91c1655bf"></p>






