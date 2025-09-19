from flask import Flask, render_template, request
import joblib
# from deep_translator import GoogleTranslator

# Load saved model and vectorizer
model = joblib.load("models/cyber_abuse_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        user_input = request.form["comment"]

        # try:
        #     urdu_text = GoogleTranslator(source="hi", target="ur").translate(user_input)
        # except:
        #     urdu_text = user_input

        # Transform input using saved vectorizer
        transformed_input = vectorizer.transform([user_input])

        # Predict using saved model
        result = model.predict(transformed_input)[0]

        # Convert numeric label to readable
        prediction = "Abusive" if result == 1 else "Not Abusive"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)