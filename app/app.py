from flask import Flask, request, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the model
model = joblib.load('models/model_xgb.sav')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        product_category = request.form['product_category']
        cpu = int(request.form['cpu'])  # Cost price per unit as an integer
        irv = int(request.form['irv'])  # Item retail value as an integer
        date_year = int(request.form['date_year'])  # Year
        date_month = int(request.form['date_month'])  # Month


        # Create DataFrame for model input
        data_dict = {
            'cost_price_per_unit': cpu,
            'item_retail_value': irv,
            'date_year': date_year,
            'date_month': date_month,
            'product_category': product_category
        }
        X_input = pd.DataFrame(data_dict, index=[0])

        # Predict
        prediction = model.predict(X_input)
        
        # Convert prediction to a readable format if necessary
        prediction_result = round(prediction[0], 2)
        if prediction_result < 0:
            prediction_result = 0

        return render_template('index.html', prediction=prediction_result, 
                               cpu_out=cpu, irv_out=irv, yr_out=date_year, mon_out=date_month, pc_out=product_category)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')
