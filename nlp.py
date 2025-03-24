from transformers import pipeline

def text_emotion(text:str):
    classifier = pipeline("text-classification", model="ayoubkirouane/BERT-Emotions-Classifier")
    # text = "ohh gosh, this is good"

    results = classifier(text)
    return results
# print(text_emotion("hi hellooo!!"))