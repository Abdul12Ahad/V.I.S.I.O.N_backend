from transformers import AutoProcessor, AutoModelForCausalLM

MODEL_NAME = "microsoft/Florence-2-base"

model = None
processor = None


def load_model():

    global model
    global processor

    if model is None:

        print("Loading Florence-2...")

        processor = AutoProcessor.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        print("Florence-2 Loaded Successfully")

    return model, processor