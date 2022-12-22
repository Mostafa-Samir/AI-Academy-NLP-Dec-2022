import os

import streamlit as st
from streamlit_server_state import server_state, server_state_lock

from model import Model, SklearnModel, TransformerModel


model_type = os.environ.get("MODEL_TYPE", None)
checkpoint_path = os.environ.get("CHECKPOINT_PATH", None)

assert model_type is not None, "MODEL_TYPE environemnt variable is missing"
assert checkpoint_path is not None, "CHECKPOINT_PATH environment variable is missing"
assert model_type in {"sklearn", "transformers"}, "Model type is unrecognized"

with server_state_lock.model:
    if "model" not in server_state:
        server_state.model: Model = SklearnModel(checkpoint_path) if model_type == "sklearn" else TransformerModel(checkpoint_path)


st.set_page_config(layout="wide")
st.write("# Sentiment Analyzer")

text = st.text_area("Write a text to predict its sentiment")

predict_btn = st.button("Predict")

if predict_btn and text != '':
    prediction, *_ = server_state.model.predict([text])
    st.write(f"Sentiment is {prediction}")