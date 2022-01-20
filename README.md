
# Overview

The **alib** (short for **a library**) provides a common **Python 3** basis for our **Virtual Network Embedding Problem (VNEP)** approximation framework. It is largely based on the original framework at **[github.com/vnep-approx-py3/alib](https://github.com/vnep-approx/alib)** and has been extended to account for **Latency Constraints**, as described in our Technical Report **[1]** and our shortened paper **[2]**, as published in IFIP Networking 2021 Poster Session.

This repository contains a common data model, a common scenario generation/execution framework and additional utilities. For a more thorough overview, test and docs of the library we recommend visiting the [Original Implementation](https://github.com/vnep-approx-py3) and consulting the corresponding papers.
### Structure

This GitHub Organization contains three repositories which contain the functionality for solving the VNEP with latency constraints and evaluating the results: 

- **[alib](https://github.com/vnep-approx-latency/alib)**: A library providing the basic data model and the Mixed-Integer Program for the classic multi-commodity formulation.
- **[vnep_approx](https://github.com/vnep-approx-latency/vnep-approx)**: Provides Linear Programming formulations, specifically the one based on the DynVMP algorithm, as well as Randomized Rounding algorithms to solve the VNEP.
- **[evaluation-ifip-networking-2021](https://github.com/vnep-approx-latency/evaluation-ifip-networking-2021)**: Provides functionality for evaluating experiment artifacts to create plots to compare runtime, profits and other algorithm parameters.

### Papers

**[1]** R. Münk, M. Rost, S. Schmid, and H. Räcke. It’s Good to Relax: Fast Profit Approximation for Virtual Networks with Latency Constraints. [Technical Report arXiv:2104.09249 [cs.NI]](https://arxiv.org/abs/2104.09249), April 2021.

**[2]** R. Münk, M. Rost, H. Räcke and S. Schmid, It's Good to Relax: Fast Profit Approximation for Virtual Networks with Latency Constraints, *2021 IFIP Networking Conference (IFIP Networking)*, 2021, pp. 1-3, doi: [10.23919/IFIPNetworking52078.2021.9472197](https://ieeexplore.ieee.org/document/9472197).

# Dependencies and Requirements

The **alib** library requires Python 3 and uses the following libraries: gurobipy, numpy, networkx (for parsing TopologyZoo instances), matplotlib and click. 

The [Gurobi Solver](https://www.gurobi.com/) must be installed and the .../gurobi64/lib directory added to the environment variable LD_LIBRARY_PATH.

# Installation

Install the **alib** package using the setup script we provide. Simply execute from within the packages root directory: 

```
pip install -e .
```

When choosing the `-e` option, sources are not copied during the installation but the local sources are used: changes to the sources are directly reflected in the installed package.

We generally recommend installing our libraries in a virtual environment.

# Usage

**For a detailed walk-through of how to use the algorithms and reproduce the results from the paper, please view the examples in the** [**evaluation-ifip-networking-2021**](https://github.com/vnep-approx-latency/evaluation-ifip-networking-2021) **repository.**

For generating and executing (etc.) experiments, the environment variable **ALIB_EXPERIMENT_HOME** should be set to a path, such that the subfolders input/ output/ and log/ exist. If this environment variable is not set, the current working directory is traversed upwards until a directory containing input/, output/, and log/ is found.

You may either use our code via our API by importing the library or via our command line interface:

```
python -m alib.cli  
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

# Contact

If you have any questions, either open up an issue on GitHub or write a mail to [robin.muenk@tum.de](mailto:robin.muenk@tum.de).
