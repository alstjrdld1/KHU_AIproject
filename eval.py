import numpy as np
import pandas as pd 

answer_sheet = pd.read_csv("./test_label.csv")
test_sheet = pd.read_csv("./test.csv")
correct = 0

for idx, answer in enumerate(answer_sheet):
    if(test_sheet[idx] == answer):
        correct = correct + 1

print("ACC => ", correct/len(answer_sheet))
    