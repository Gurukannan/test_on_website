from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/resume',methods = ['POST', 'GET'])
def resume():
   return render_template('resume.html')

@app.route('/excel_info',methods = ['POST', 'GET'])
def excel_info():
   return render_template('excel_info.html')

@app.route('/datastudio',methods = ['POST', 'GET'])
def datastudio():
   return render_template('datastudio.html')

@app.route('/tableau',methods = ['POST', 'GET'])
def tableau():
   return render_template('tableau.html')

@app.route('/ml_model',methods = ['POST', 'GET'])
def ml_model():
   return render_template('ml_model.html')

@app.route('/salary_pred',methods = ['POST'])
def salary_pred():
   model = pickle.load(open('ml_models/salary_prediction.pkl', 'rb'))
   int_features = [int(x) for x in request.form.values()]
   final_features = [np.array(int_features)]
   prediction = model.predict(final_features)
   output = round(prediction[0], 2)
   return render_template('ml_model.html', prediction_text='Employee Salary should be Rs {}'.format(output))

@app.route('/articles',methods = ['POST', 'GET'])
def articles():
   return render_template('articles.html')

if __name__ == '__main__':
   app.run(debug = True)