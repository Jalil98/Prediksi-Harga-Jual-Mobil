from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model
model = joblib.load('model.joblib')

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0

    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Kms_Driven2 = np.log(Kms_Driven)
        Owner = int(request.form['Owner'])

        # Fuel Type
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1

        # Tahun
        Year = 2020 - Year

        # Seller Type
        Seller_Type_Individual = 1 if request.form['Seller_Type_Individual'] == 'Individual' else 0

        # Transmission
        Transmission_Mannual = 1 if request.form['Transmission_Mannual'] == 'Mannual' else 0

        # Prediksi
        data = [[
            Present_Price, Kms_Driven2, Owner, Year,
            Fuel_Type_Diesel, Fuel_Type_Petrol,
            Seller_Type_Individual, Transmission_Mannual
        ]]

        prediction = model.predict(data)
        output = round(prediction[0], 2)   # hasil dalam lakh

        if output < 0:
            return render_template('index.html', prediction_text="Maaf, mobil tidak bisa dijual.")

        # ---- KONVERSI KE RUPIAH ----
        RUPIAH_RATE = 19000000  # 1 lakh = 19 juta Rupiah
        harga_rupiah = output * RUPIAH_RATE
        harga_rupiah = f"{harga_rupiah:,.0f}".replace(",", ".")

        return render_template(
            'index.html',
            prediction_text=f"Harga jual mobil: {output} Lakh = (Rp {harga_rupiah})"
        )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
