#!/bin/bash
export dataset_path=pdfs/data.csv
export reader_path=reader/bert_qa.joblib

FLASK_APP=api.py flask run -h 0.0.0.0
