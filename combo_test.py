import TATA
import ICICI

import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    print(request.form)
    if request.method == 'POST':
        print(request.form)
        data1 = request.form['Tot_lives']
        print(data1)
        data2 = request.form['Sum_insured']
        data3 = request.form['Age']
        data4 = request.form['Family_type']
        data5 = request.form['Room_rent']
        data6 = request.form['Mat_amount']
        data7 = request.form['Wait']
        data8 = request.form['Init_wait']
        data9 = request.form['Mat_wait']


        term1 = int(data1)
        term2 = int(data2)
        term3 = int(data3)
        term4 = d4[int(data4)-1]
        term5 = d5[int(data5)-1]
        term6 = d6[int(data6)-1]
        term7 = d7[int(data7)-1]
        term8 = d8[int(data8)-1]
        term9 = d9[int(data9)-1]


        ICICI_price = ICICI.calculate(data1, data2, data3, data4, data5, data6, data7, data8, data9)
        TATA_price = ICICI.calculate(data1, data2, data3, data4, data5, data6, data7, data8, data9)

        insurance_terms = [ICICI_price, TATA_price]

        data = {'values':insurance_terms}
        return data
        

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 4444, debug=True)









