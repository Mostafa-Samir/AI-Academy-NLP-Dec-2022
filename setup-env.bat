@echo off

CALL conda.bat create -n ai-academy-env python=3.8
CALL conda.bat deactivate
CALL conda.bat activate ai-academy-env
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --display-name="AI-Academy"
python -m setup-nltk