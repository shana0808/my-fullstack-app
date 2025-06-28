from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        if "good" in text.lower():
            result = "Positive 😊"
        elif "bad" in text.lower():
            result = "Negative 😢"
        else:
            result = "Neutral 😐"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
