from flask import Flask, request, jsonify
from chat import get_response

app = Flask(__name__)


@appget("/get")
def index_get():
    return render_template("base.html")


# Route to do the predictions
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: Check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
