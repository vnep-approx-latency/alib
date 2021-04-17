# Overview

The **alib** (short for **a library**) provides a common **Python 3.X** basis for our **Virtual Network Embedding Problem (VNEP)** approximation framework. It is based on the original **Python 2.7** framework that is also hosted on **[Github at https://github.com/vnep-approx/alib](https://github.com/vnep-approx/alib)**.

As such, it contains (among other things) 
- A common **[data model](alib/datamodel.py)** to capture the notions of **substrate graphs** (physical networks), **request graphs** (virtual networks), and **embeddings** of requests to a substrate, **scenarios**, i.e. bundling multiple requests to be embedded on a common substrate.
- A common **[scenario generation](alib/scenariogeneration.py)** framework to generate cartesian products of parameter spaces and to generate scenarios accordingly (at random).
- A common **[scenario execution](alib/run_experiment.py)** framework to execute experments in parallel and using arbitrarily many different parameter configurations.
- A common base for solving **[integer/linear programs](alib/modelcreator.py)** pertaining to the VNEP together with an implementation of the **[classic multi-commodity flow formulation](alib/mip.py)** for the VNEP.
- Additionally, **[utilities](alib.util.py)** are provided to facilitate pretty printing, logging, etc.

# Dependencies and Requirements

The alib library requires Python 3.X and uses the following libraries: gurobipy, numpy, networkx (for parsing TopologyZoo instances), matplotlib, and click. 

Gurobi must be installed and the .../gurobi64/lib directory added to the environment variable LD_LIBRARY_PATH.

For generating and executing (etc.) experiments, the environment variable **ALIB_EXPERIMENT_HOME** should be set to a path,
such that the subfolders input/ output/ and log/ exist. If this environment variable is not set, the current working directory is traversed upwards until a directory containing input/, output/, and log/ is found.

**Note**: Our source was tested on Linux (specifically Ubuntu 14 and Ubuntu 16) and Mac OS X 10.15.  

# Installation

To install **alib**, we provide a setup script. Simply execute from within alib's root directory: 

```
pip install .
```

Furthermore, if the code base will be edited by you, we propose to install it as editable:
```
pip install -e .
```
When choosing this option, sources are not copied during the installation but the local sources are used: changes to
the sources are directly reflected in the installed package.

We generally propose to install **alib** into a virtual environment.

# Usage

You may either use our code via our API by importing the library or via our command line interface:

```
python -m alib.cli                                                                                                                                                                                           ─╯
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  convert-topology-zoo-gml-to-yml
                                  converts original topology zoo graphs in the
                                  GML format to our yml representation

  generate-scenarios              generates scenarios according to a yaml file
  inspect-cactus-graphs           outputs charactistics of cactus graph
                                  generation given a yaml-specification

  merge-scenario-containers       merges two scenario container pickle files
  merge-sss                       merges two scenario solution storage (sss)
                                  objects

  pretty-print                    outputs a textual representation of the
                                  contents of a pickle file

  start-experiment                starts an experiment specified in a yaml
                                  file

  summarize-toopology-zoo-graphs  summarizes characteristics of topology
                                  graphs contained
```

# Tests

The test directory contains a large number of tests to check the correctness of our implementation and might also be useful
to understand the code. 

To execute the tests, simply execute pytest in the test directory.

```
pytest .
```

# API Documentation

We provide a basic template to create an API documentation using **[Sphinx](http://www.sphinx-doc.org)**. 

To create the documentation, simply execute the makefile in **[docs/](docs/)**. Specifically, run for example

```
make html
```

to create the HTML documentation.

Note that **alib** must lie on the PYTHONPATH. If you use a virtual environment, we propose to install sphinx within the
virtual environment (using **pip install spinx**) and executing the above from within the virtual environment. 

# Contact and Acknowledgement

If you have any questions, either open up an issue on GitHub or write a mail to mrost<AT>inet.tu-berlin<DOT>de.

Major parts of this code were developed under the support of the **German BMBF Software Campus grant 01IS1205** from 2016 to 2018.
