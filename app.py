import joblib
from flask import Flask, render_template, request
# from text_filter import my_review_filter
model = None
vectorizer = None

# def init():
#     global model,vectorizer
#     model = joblib.load(r'./Model/trained_model.pkl')
#     vectorizer = joblib.load(r'./Model/trained_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    # init()
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    # if(model==None):init()
    if request.method == 'POST':
        txt = request.form['text']
        if len(txt)>0:
            # X = vectorizer.transform([txt])
            # predict_val = model.predict(X)
            # prob = model.predict_proba(X)
            predict_val=1
            if predict_val == 1:
                predict_res = 'POSITIVE'
                confidence = 100
                return render_template('index.html', page='text', prediction_text = predict_res, confidence = round(100*confidence,2), bg='green')
            else:
                predict_res = 'NEGATIVE'
                confidence = 0
                return render_template('index.html', page='text', prediction_text = predict_res, confidence = round(100*confidence,2), bg='red')
        else:
            return render_template('index.html', page='empty')

# not fot production
if __name__ == '__main__':
      app.run(debug=True)
#     app.run(debug=False, host='0.0.0.0')