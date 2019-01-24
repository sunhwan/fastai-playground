import torch
import pickle
from fastai.vision import *

def predict(filename):
    torch.load(open('data/export.pkl', 'rb'), map_location='cpu')
    learn = load_learner('./data', cpu=True)
    img = open_image(filename)
    preds = learn.predict(img)
    return preds

if __name__ == '__main__':
    testfilename = 'data/test/test.jpeg'
    preds = predict(testfilename)
    print(preds)