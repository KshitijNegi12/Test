import joblib
import pandas as pd
from flask import Flask, render_template, request, send_file
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from amazon.amazon.spiders.amspy import AmspySpider
model = None
vectorizer = None
    
def crawl(link):
    process = CrawlerProcess(get_project_settings())
    process.crawl(AmspySpider, slink=link)
    process.start()
    process.join()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form['inputType']
        if input == 'text':
            txt = request.form['text']
            if len(txt)>0:
                predict_val=1
                if predict_val == 1:
                    predict_res = 'POSITIVE'
                    confidence = 1
                    return render_template('index.html', page='text', prediction_text = predict_res, confidence = round(100*confidence,2), bg='green')
                else:
                    predict_res = 'NEGATIVE'
                    confidence = 0
                    return render_template('index.html', page='text', prediction_text = predict_res, confidence = round(100*confidence,2), bg='red')
            else:
                return render_template('index.html', page='empty')
        else:
            link = request.form['link']
            if len(link) > 0 and link.startswith('https://www.amazon.in/'):
                crawl_process = Process(target=crawl, args=(link,))
                crawl_process.start()
                crawl_process.join() 
                return render_template('index.html', page='download')
            else:
                return render_template('index.html', page='wrong_link')

@app.route('/download_data', methods=['POST','GET'])
def download_data():
    file_path = './data.csv'  
    return send_file(file_path, as_attachment=True)

# not fot production
if __name__ == '__main__':
      app.run(debug=True)
#     app.run(debug=False, host='0.0.0.0')