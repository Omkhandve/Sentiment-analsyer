from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        score = analyzer.polarity_scores(user_input)
        compound = score['compound']
        if compound >= 0.05:
            sentiment = "Positive 😊"
        elif compound <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"
    return render_template("index1.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
