import argparse

from fastapi import FastAPI
import uvicorn

from model import Model, SklearnModel, TransformerModel

model: Model = None

def initialize_app(model_type: str, checkpoint_path: str) -> FastAPI:

    app = FastAPI()

    @app.on_event("startup")
    def initialize_model():
        global model
        model = SklearnModel(checkpoint_path) if model_type == "sklearn" else TransformerModel(checkpoint_path)

    @app.post("/predict")
    async def predict_sentiment(text: str):
        prediction, *_ = model.predict([text])
        return {
            "text": text,
            "sentiment": prediction
        }

    return app

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--model-type", help="The type of the model, either sklearn or transformers", type=str)
    parser.add_argument("--checkpoint-path", help="The path to the saved checkpoint", type=str)

    args = parser.parse_args()

    assert args.model_type in {"sklearn", "transformers"}, "Model type is unrecognized"

    app = initialize_app(args.model_type, args.checkpoint_path)

    uvicorn.run(app, host='0.0.0.0', port=8000)