import torch
import pickle
from fastai.vision import *

import warnings
warnings.filterwarnings("ignore", category=torch.serialization.SourceChangeWarning)

def predict(filename):
    torch.load(open('data/export.pkl', 'rb'), map_location='cpu')
    learn = load_learner('./data')
    img = open_image(filename)
    preds = learn.predict(img)
    return preds

if __name__ == '__main__':
    testfilename = 'data/test/test.jpeg'
    preds = predict(testfilename)
    print(preds)
