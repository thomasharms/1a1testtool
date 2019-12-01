# Python Testing Tool

This tool is build in order to test python applications in an easy off the shelf fashion. Each test will be exectuted in its own virtual environment in a concurrent threading fashion. Tests can be put in the Repository folder and will be executed automatically.

## Getting Started

You can set up the tool within a couple of easy steps. System requirements are described at the section Requirements. You can download the tool from github and install it by following the instruction at the section Installing. Run Tests by following the steps as described in section: Running the Tests.

### Requirements

The only known requirement would be having a proper installation of Python 3.6 or higher installed as well as up and running. The testing tool will run on Linux and Mac OSX while Windows support might follow soon.

### Installing

The files are available at [the projects git repository](https://github.com/thomasharms/1a1testtool.git). Feel free to fork or clone ahead. After downloading the files first install the environment and the database by running the init.py file. This can be easily achieved by navigating to the folder containing the files by using a shell. Just run in a shell: 
```
python3 init.py
```
In case no Exception has been risen some virtual environments have been installed along with the needed packages and dependencies as well as the database and tables needed had been built.
Now you should be good to go.

## Running the Tests

### Running Test Files

The most interesting folder in order to run tests is called Test_Repo. You can just put your test files or bash files in there and they will automatically be tested. For demonstration purposes there are a couple of pretailored tests already in there. Feel free to use them in order to explore how it works.
A test can be run by using the main.py script. You can do that by:

* navigating in your shell to the program folder and run:
```
python3 main.py
```
* run in your shell:
```
python3 /path/to/the/program/main.py
```

All the tests in the repository folder will be run parallel, or more precisely: concurrent. The results will be put out via stdout as well as saved in the database.

### Running Self Evaluating Tests

The tool is able to evaluate the functionality of its own behaviour. It is accomplishing that by using the tests defined in the script "test_selftest.py". In order to run a test on the tool itself, simply run shell:
* out of the main program folder:
```
python3 selftest.py
```
* run from shell:
```
python3 /path/to/the/program/selftest.py
```

## Show Test Results

There is a demonstration procedure running for now, showing you the last 10 test results. This could be improved in a more conveniened fashion in the future. In order to see these results by shell you do either of the following steps:
* navigating in your shell to the program folder and run:
```
python3 testresults.py
```
* run in your shell:
```
python3 /path/to/the/program/testresults.py
```

## Test Framework

The chosen framework is PyTest.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/thomasharms/1a1testtool/tags). 

## Authors

* **Thomas Harms** - *Initial work* - [Thomas Harms](https://github.com/thomasharms)


