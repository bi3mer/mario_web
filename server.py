from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, port=port)
    app.run(threaded=True, port=port)