<div align="center">
  <a href="https://www.pokt.network">
    <img src="https://user-images.githubusercontent.com/16605170/74199287-94f17680-4c18-11ea-9de2-b094fab91431.png" alt="Pocket Network logo" width="340"/>
  </a>
</div>

# Pocket Economic Research

A repository for collaboration on Pocket Network modelling. Based on the open-source Python library [radCAD](https://github.com/CADLabs/radCAD), an extension to [cadCAD](https://cadcad.org). Also, inspired by the [Ethereum Economic Model](https://github.com/CADLabs/ethereum-economic-model/) for repo structuring and documentation.

We will aim to migrate to cadCAD1.0 in the future once it becomes readily used by the community.

## Table of Contents

* [Introduction](#Introduction)
  * [Model Features](#Model-Features)
  * [Directory Structure](#Directory-Structure)
  * [Model Architecture](#Model-Architecture)
  * [Model Assumptions](#Model-Assumptions)
* [Getting Started](#Getting-Started)
* [Simluation Experiments](#Simlulation-Experiments)
* [Web App](#Web-App)
* [Contributions](#Contributions)
* [Contacts](#Support-and-Contact)
* [License](#License)

---

## Introduction

We are creating an open source model to describe the Pocket Network ecosystem. The model is a work in progress but aims to capture App session behavior, which translates to node rewards and network state.

### Model Features

* Modular structure for experimentation. Different users of the model can experiment with their agent type.
* Interactive Web Application for user access.

### Directory structure

* [data/](data/): Datasets used in the creation of the models.
* [docs/](docs/): Various documentation to support the usage of the model from systems level understanding to code level documentation.
* [experiments/](experiments/): Analysis and experiment creation.
* [model/](model/): Base models of the repository
* [app/](app/): interactive web apps for ease of use

### Model Architecture

The [Model](model/) contains the cadCAD modules for agent styles descriptions and configuration files for the simulations.

| Module | Description |
| --- | --- |
| WIP | WIP |

### Model Assumptions

We aim to create relevant models for the real world network but any assumption made for implementation will be described in the [Assumptions](ASSUMPTIONS.md) markdown.

## Getting Started

For now we will be using local environments using Python3 and Visual Studio Code (with Jupyter extension).

**First**, set up a Python 3 [virtualenv](https://docs.python.org/3/library/venv.html) development environment using of Pythons [Virtual Environments Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

```bash
mkvirtualenv radCAD
workon radCAD
```

**Once you have _activated_ the virtual environment**, install the Python 3 dependencies using [Pip](https://packaging.python.org/tutorials/installing-packages/), from the [requirements.txt](requirements.txt) file in the root directory, within your new virtual environment:

```bash
# Install Python 3 dependencies inside virtual environment
pip install -r requirements.txt
```

In your [Visual Studio Code](https://code.visualstudio.com/) window you can interact with Jupyter Notebooks through the `.ipynb` file extensions after you have installed Jupyter extension (should prompt automatically). There you can choose your virtual environment (cadCAD) that was created earlier.

## Simulations Experiments

The [experiments/](experiments/) directory will be populated with example analyses and instructions for setting up news experiments. The new experiments can be modifications of the current state or possibly a new one. But we aim to provide simple parameter modifications as a web app.

## Web App

Starting with [Streamlit](https://www.streamlit.io) we provide simple simulations that can take varying inputs. In the future, we may migrate to [Dash Plotly](https://plotly.com/dash/) for more advanced applications if needed.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/pokt-network/repo-template/blob/master/CONTRIBUTING.md) for details on contributions and the process of submitting pull requests.

## Support and Contact

<div>
  <a  href="https://twitter.com/poktnetwork" ><img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"></a>
  <a href="https://t.me/POKTnetwork"><img src="https://img.shields.io/badge/Telegram-blue.svg"></a>
  <a href="https://www.facebook.com/POKTnetwork" ><img src="https://img.shields.io/badge/Facebook-red.svg"></a>
  <a href="https://research.pokt.network"><img src="https://img.shields.io/discourse/https/research.pokt.network/posts.svg"></a>
</div>

## License

This project is licensed under the MIT License; see the [LICENSE.md](LICENSE.md) file for details.
