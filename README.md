
# Geospatial visualization 

This repository contains several notebooks demonstrating geospatial visualziation using [leafmap](https://leafmap.org)  a Python package for geospatial analysis and interactive mapping in a Jupyter environment.

## Data 

The main data source is [GeoHub](https://geohub.data.undp.org/data).

## Installation

We recommend using a virtual environment  because **leafmap**  feature a large number of dependencies.

### using pipenv
 Detailed instruction on how to install *pipenv* are available at [https://pipenv.pypa.io/en/latest/installation.html](https://pipenv.pypa.io/en/latest/installation.html)

1. clone the repository and change into the cretae folder

```shell
git clone https://github.com/UNDP-Data/geo-visualization.git
cd  geo-visualization
```

2. create a virtual env
```shell
pipenv --python 3
```
3. install dependencies
```shell
pipenv run pip install -r requirements.txt
```
4. install jupyter lab
```shell
pipenv run pip install jupyterlab
```

5. start a session

```shell
piepnv run jupyter lab
```

