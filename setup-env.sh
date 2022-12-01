conda create -n ai-academy-env python=3.8
conda deactivate && \
    conda activate ai-academy-env
    pip install --upgrade pip
    pip install -r requirements.txt