from doctest import debug
from pprint import pprint
import nltk
from urllib import request
import os
import sys
import pandas as pd
from parsing_py import parse_website_content
import json
import spacy
#spacy.load('en_core_web_sm')
from flask import Flask,render_template,request
path = os.path.abspath(r"C:\Users\KAILASH\Desktop\final_proj\Questgen.ai")
sys.path.append(path)
from Questgen import main


app = Flask(__name__,static_url_path='/static')

@app.route('/',methods = ['GET','POST'])
def Home():
    if request.method == "POST":
        Website_URL = request.form.get("box")
        Sentence_list = parse_website_content(Website_URL)
        lst = []
        dic = {}
        qg = main.QGen()
        for sentence in Sentence_list:  
            try:
                payload2 = {
                    "input_text" : f"{sentence}",
                    "max_questions": 5  
                            }
                output = qg.predict_shortq(payload2)

                for val in output['questions']:
                    Ftext = f"### Human:\n{val['Question']}\n\n### Assistant:\n{val['context']}"
                    print(Ftext)
                lst.append(Ftext)                  
            except:
                pass
        
        print("Breaked from loop")
        print(lst)
        dataframe = pd.Series(lst,name='text')
        dataframe.to_csv(f'NewDataFrame.csv',index=False)
        return '''<p>Successfully generated the fine tuned data</p>'''
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)

    


