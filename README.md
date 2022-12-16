# AI Academy 2022 - Natural Language Processing (NLP)

Welcome to Beyond Limits AI Academy 2022 - NLP track. This repositoiry holds the necessary instructions and code that you will need in your labs across the three days of the training. Please follow the instructions below carefually for each day.

## Day 1
### Environment Setup

The very first thing we need to do is to prepare your local environemnt to run the provided code. To do so, we need you to 
1. inatll `miniconda` on your machine.
    - If your machine runs a Windows OS:
        - Go to https://docs.conda.io/en/latest/miniconda.html#windows-installers.
        - Download the `Python 3.8` installer to your machine.
        - Run the downloaded installer and follow the installation steps.

    -  If your machine runs macOS:
        - Go to https://docs.conda.io/en/latest/miniconda.html#macos-installers.
        - Download the `Python 3.8` installer to your machine.
        - Run the downloaded installer.

    - If your machine runs a Linux-based OS (e.g. Ubuntu)
        - Go to https://docs.conda.io/en/latest/miniconda.html#linux-installers.
        - Download the bash script installer for `Python 3.8`.
        - Open your terminal in the downloaded file location and run `bash Miniconda3-py38_4.12.0-Linux-x86_64.sh`

2. Clone this repository to your machine.
3. Go to the cloned repositoiry location and:
    - For Windows machines: TBD
    - For macOS/Linux-based: Open your terminal and run `bash setup-env.py`.
    
    This step will create a conda environement in your machine called `ai-academy-env`, this environemnt has all the dependencies required to run the labs. Make sure that you have this environemnt activated in your terminal before running commands descitrbed next. To activate the environemnt, simply run `conda activate ai-academy-env`.

### Lab
To start working on your day-1 lab, start the Jupyter Notebook server and navigate to `Day-1-lab.ipynb` notebook. To start the server, simply run `jupyter notebook` in the terminal opened in cloned repository directory. Once you open the notebook, choose the `AI-Academy` kernel if not already chosen.