from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)

# Load model & encoder
model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

# Load dataset untuk evaluasi
df = pd.read_excel("bank.xlsx")
X = df.drop("deposit", axis=1)
y = df["deposit"]

# Encode data kategorikal
X_encoded = X.copy()
for col, le in label_encoders.items():
    X_encoded[col] = le.transform(X_encoded[col])

# Encode target
y_encoded = target_encoder.transform(y)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ambil input user
        data = {
            "age": int(request.form["age"]),
            "job": request.form["job"],
            "marital": request.form["marital"],
            "education": request.form["education"],
            "default": request.form["default"],
            "balance": int(request.form["balance"]),
            "housing": request.form["housing"],
            "loan": request.form["loan"],
            "contact": request.form["contact"],
            "day": int(request.form["day"]),
            "month": request.form["month"],
            "duration": int(request.form["duration"]),
            "campaign": int(request.form["campaign"]),
            "pdays": int(request.form["pdays"]),
            "previous": int(request.form["previous"]),
            "poutcome": request.form["poutcome"]
        }

        # Convert ke DataFrame
        df_input = pd.DataFrame([data])

        # Encode kategorikal
        for col, le in label_encoders.items():
            df_input[col] = le.transform(df_input[col])

        # Prediksi kelas
        pred = model.predict(df_input)[0]
        result_label = target_encoder.inverse_transform([pred])[0]

        # Prediksi probabilitas
        proba = model.predict_proba(df_input)[0]

        # Mapping probabilitas ke nama kelas
        class_probs = {
            target_encoder.classes_[i]: round(proba[i] * 100, 2)
            for i in range(len(target_encoder.classes_))
        }

        # Pesan custom
        if result_label == "yes":
            message = "Kemungkinan melakukan deposito"
        else:
            message = "Kemungkinan tidak melakukan deposito"

        return render_template(
            "index.html",
            result=message,
            class_probs=class_probs
        )

    return render_template("index.html", result=None, class_probs=None)


@app.route("/evaluate")
def evaluate():
    # Prediksi semua data
    y_pred = model.predict(X_encoded)

    # Akurasi
    acc = accuracy_score(y_encoded, y_pred)
    acc_percentage = round(acc * 100, 2)

    # Classification Report
    report = classification_report(y_encoded, y_pred, target_names=target_encoder.classes_)

    return render_template("evaluate.html", accuracy=acc_percentage, report=report)

if __name__ == "__main__":
    app.run(debug=True)