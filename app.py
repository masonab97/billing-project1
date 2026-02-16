from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            units = float(request.form["units"])

            if units <= 100:
                result = "Lowest Rate"
            elif units <= 300:
                result = "Medium Rate"
            elif units <= 500:
                result = "Higher Rate"
            else:
                result = "Highest Rate"

        except ValueError:
            result = "Number needed"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
