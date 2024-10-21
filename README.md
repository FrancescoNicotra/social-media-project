# Jupyter Notebook Project with Docker

This repository contains a project developed using Jupyter Notebook. The environment is set up with all necessary dependencies using Docker and a `requirements.txt` file. Follow the steps below to get the project up and running.

## Prerequisites

Before running the project, make sure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)
- A valid YouTube API Key. You can obtain one by following [this guide](https://developers.google.com/youtube/v3/getting-started).
- A valid Groq API Key. You can sign up and get access via the [Groq API website](https://groq.com/).

## Getting Started

### 1. Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/FrancescoNicotra/social-media-project.git
```
### Navigate into the project directory:
To run the project locally without Docker, install the required Python packages:
```bash
cd social-media-project
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
Alternatively, you can create a virtual environment for your project:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running with Jupyter Notebook
To run the Jupyter Notebook locally:
  Ensure Jupyter Notebook is installed. If not, install it with the following command:
  ```bash
    pip install jupyter
  ```
Launch Jupyter Notebook:
```bash
jupyter notebook
```
In your browser, navigate to the Jupyter interface and open Project.ipynb
