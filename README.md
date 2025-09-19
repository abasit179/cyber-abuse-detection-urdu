# ⚡ Cyber Abuse Detector (Urdu)

This is a Machine Learning + Flask web app that detects whether a given **Urdu comment** is abusive or not.

## 🚀 Features
- Input text in Urdu
- Machine learning model (LinearSVC + TF-IDF)
- Flask web interface with clean UI
- Real-time prediction

## 📂 Project Structure
- `app.py` → Flask app
- `templates/` → HTML frontend
- `static/` → CSS styling
- `models/` → Trained ML model + vectorizer
- `data/` → Original + Preprocessed datasets
- `notebooks/` → Jupyter notebook for training
- `requirements.txt` → Required dependencies

## ▶️ Run the App
```bash
git clone https://github.com/abasit179/cyber-abuse-detection-urdu.git
cd cyber-abuse-detection-urdu
pip install -r requirements.txt
python app.py
