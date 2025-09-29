# 🏦 Aplikasi Prediksi Deposito Bank

Aplikasi ini adalah implementasi **Decision Tree** untuk memprediksi kemungkinan nasabah melakukan **deposito berjangka** berdasarkan data nasabah bank.
Dilengkapi dengan **tampilan UIa berbasis Flask** sehingga user dapat langsung menginput data dan melihat hasil prediksi beserta probabilitasnya.

---

## ✨ Fitur Utama

* 🔮 Prediksi apakah nasabah akan melakukan deposito atau tidak
* 📊 Menampilkan **probabilitas kedua kelas** (deposit vs tidak deposit)
* 📈 Halaman evaluasi model → akurasi + classification report
* 🌐 UI sederhana dengan **TailwindCSS** + form dropdown untuk input kategorikal
* 📂 Dataset: **Bank Marketing Dataset** (`bank.xlsx`)

---

## 🛠️ Teknologi yang Digunakan

* **Python 3.8+**
* **Flask** (untuk UI web)
* **scikit-learn** (Decision Tree Classifier)
* **pandas** (manajemen data)
* **joblib** (simpan & load model)
* **TailwindCSS** (styling UI)

---

## 📂 Struktur Project

```
.
├── app.py                 # Flask web app
├── train_model.py         # Script training Decision Tree
├── bank.xlsx              # Dataset Bank Marketing
├── model.pkl              # Model terlatih
├── label_encoders.pkl     # Encoder fitur kategorikal
├── target_encoder.pkl     # Encoder target
├── templates/
│   ├── index.html         # Form input + hasil prediksi
│   └── evaluate.html      # Evaluasi model
└── README.md              # Dokumentasi project
```

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/bank-deposit-prediction.git
cd bank-deposit-prediction
```

### 2. Install Dependencies

Disarankan menggunakan virtual environment:

```bash
pip install -r requirements.txt
```

Contoh `requirements.txt`:

```
flask
pandas
scikit-learn
joblib
openpyxl
```

### 3. Latih Model

```bash
python train_model.py
```

Model terlatih akan disimpan sebagai:

* `model.pkl`
* `label_encoders.pkl`
* `target_encoder.pkl`

### 4. Jalankan Aplikasi Flask

```bash
python app.py
```

Akses di browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Contoh Output

### Prediksi

* "Kemungkinan melakukan deposit"
* Tabel probabilitas:

  | Kelas                   | Persentase |
  | ----------------------- | ---------- |
  | Tidak Melakukan Deposit | 23.45%     |
  | Melakukan Deposit       | 76.55%     |

### Evaluasi

* Akurasi model
* Classification report (precision, recall, f1-score)

---

## 📌 Catatan

* Dataset yang digunakan adalah **Bank Marketing Dataset** ([Kaggle](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)).
* Decision Tree hanya contoh sederhana, model bisa dikembangkan lebih lanjut (Random Forest, XGBoost, dll.).
* UI dibuat minimalis agar mudah dipahami dan bisa dikembangkan lebih lanjut.

---

Made With ♥️ and ☕ by Abiddar Putra 
