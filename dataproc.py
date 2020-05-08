import os
import time
import pandas as pd

from ast import literal_eval
from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.converters import pdf_converter

path_to_watch = "pdfs"
before = dict ([(f, None) for f in os.listdir(path_to_watch)])

def wholeShot():
    print("UPDATING CORPUS")

    df = pd.read_csv("pdfs/data.csv")
    df2 = pdf_converter(directory_path='pdfs')
    df2.dropna()
    df2 = df2.mask(df2.eq('None')).dropna()
    df2 = filter_paragraphs(df2)
    # for rows in df2
    #   if row title is not in df
    #       append row to df
    print(len(df2))
    for index, row in df2.iterrows():
        if str(row['title']) not in list(df['title']):
            df = df.append(row, ignore_index=True)
    print(df)
    df.to_csv("pdfs/data.csv", index=False)
    
    os.system("docker stop search-engine")
    os.system("docker rm search-engine")
    os.system("docker build -t search-engine . -f dockerfile-service")
    os.system("docker run -d -p 5000:5000 -v /home/sidworld/sixgod/pdfs:/pdfs --name search-engine --rm search-engine ")
"""
def justRebuild():
    print("REBUILDING")
    df = pd.read_csv("pdfs/data.csv")
    df = filter_paragraphs(df)
    df.to_csv("pdfs/data.csv",index=False)
    os.system("docker stop search-engine")
    os.system("docker rm search-engine")
    os.system("docker build -t search-engine . -f dockerfile-service")
    os.system("docker run -d -p 5000:5000 -v /home/sidworld/sixgod/pdfs:/pdfs --name search-engine --rm search-engine")
"""
wholeShot()

while 1:
    time.sleep(3)
    after = dict ([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    # if added and added[0] != 't.pdf' or (removed and removed[0] != 't.pdf'): 
    #     wholeShot()
    if added or removed:
        wholeShot()
    before = after
