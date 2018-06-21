from glob2 import glob
import pandas as pd


df = pd.DataFrame(columns=["file"])

for image in glob("test/*.png"):
    dir_ = image.split('/')
    file_ = dir_[-1]

    df = df.append({
        "file": file_
        }, ignore_index=True)

df.to_csv('labeltests.csv', index=False)