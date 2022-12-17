#!/bin/bash

conda create -n ai-academy-env python=3.8

source $(conda info --base)/etc/profile.d/conda.sh && \
    conda deactivate && \
    conda activate ai-academy-env && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m ipykernel install --user --display-name="AI-Academy" && \
    python -m setup-nltk