from abc import abstractmethod
from typing import Iterable
import os

import joblib
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import torch

class Model:

    @abstractmethod
    def __init__(self, checkpoint_path: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def predict(self, text: Iterable[str]) -> Iterable[str]:
        raise NotImplementedError()


class SklearnModel(Model):

    def __init__(self, checkpoint_path: str) -> None:
        self.vectorizer = joblib.load(os.path.join(checkpoint_path, "vectorizer.bin"))
        self.model = joblib.load(os.path.join(checkpoint_path, "classifier.bin"))

    def predict(self, text: Iterable[str]) -> Iterable[str]:
        x = self.vectorizer.transform(text)
        preds = self.model.predict(x)

        return preds


class TransformerModel(Model):

    def __init__(self, checkpoint_path: str) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(checkpoint_path)

        self.model.eval()
        self.id2label = {
            0: "negative",
            1: "neutral",
            2: "positive"
        }

    def predict(self, text: Iterable[str]) -> Iterable[str]:
        x = self.tokenizer(text, padding='longest', return_tensors='pt')
        with torch.no_grad():
            logits = self.model(**x)
        
        preds = np.argmax(logits.detach().cpu().numpy(), axis=1)
        textual_preds = [self.id2label[label_id] for label_id in preds]

        return textual_preds


if __name__ == "__main__":
    nb = SklearnModel("../sklearn_model")
    print(nb.predict(["This is the worst experinece ever", "You're the best company ever"]))