from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import pandas as pd
from cdqa.utils.filters import filter_paragraphs
import pdfkit # apt-get install wkhtmltopdf
import re
import os 
import time
import csv
from cleantext import clean

from client import DiffbotClient,DiffbotCrawl
from config import API_TOKEN

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

def swallowURL(url):
    import time
    diffbot = DiffbotClient()
    token = API_TOKEN
    api = "article"
    response = diffbot.request(url, token, api, version=2)
    #time.sleep(1)
    if 'html' not in response:
        return
    subtexts = response['html'].split("<p>")
    res = []
    for t in subtexts:
        outgt = clean(t,
        	fix_unicode=True,               # fix various unicode errors
        	to_ascii=True,                  # transliterate to closest ASCII representation
        	lower=False,                     # lowercase text
        	no_line_breaks=True,           # fully strip line breaks as opposed to only normalizing them
        	no_urls=False,                  # replace all URLs with a special token
        	no_emails=False,                # replace all email addresses with a special token
        	no_phone_numbers=False,         # replace all phone numbers with a special token
        	no_numbers=False,               # replace all numbers with a special token
        	no_digits=False,                # replace all digits with a special token
        	no_currency_symbols=False,      # replace all currency symbols with a special token
        	no_punct=False,                 # fully remove punctuation
        	replace_with_email="<EMAIL>",
        	replace_with_phone_number="<PHONE>",
        	replace_with_currency_symbol="<CUR>",
        	lang="en"                       # set to 'de' for German special handling
    	)
        outgt = re.sub("<.*?>", " ", outgt)
        ogt = outgt.strip()
        ogt = re.sub("\s\s+" , " ", ogt)
        ogt = re.sub('&lt;/?[a-z]+&gt;', '', ogt)
        ogt = ogt.replace("&rsquo;","")
        ogt = ogt.replace("&ldquo;","")
        ogt = ogt.replace("\n","")
        ogt = ogt.replace("\r","")
        ogt = ogt.replace("\\n","")
        if len(ogt) > 10:
            res.append(outgt)
    
    if len(res) > 2:
        fields=[''.join(e for e in url if e.isalnum()), str(res)]
        if 'http' in fields[0]: 
            with open('pdfs/data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["GET"])
def api():
    query = request.args.get("query")
    print(query)
    urls = []
    for j in search(query, tld="com", num=20, stop=20, pause=0.2): 
        swallowURL(j)
        urls.append(j)
    
    f = open('pdfs/t.pdf', 'w+')
    time.sleep(3)
    f.close()
    try:
        os.remove('pdfs/t.pdf')
    except OSError:
        pass

    return jsonify(
        query=query, answer=str(urls), title="Thanks for making Six Answers smarter! I'll take 30 seconds to reboot Six Answers with this new information.", paragraph="Thanks for making sixanswers smarter! The service will restart in 30 seconds."
    )
