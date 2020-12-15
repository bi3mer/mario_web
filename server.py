from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/get-map/<index>')
def get_map(index):
    try:
        f = open(os.path.join('data', 'levels', f'{int(index)}.txt'))
        f.readline() # remove header
        content = f.read()
        f.close()

        return content
    except Exception as e:
        print(e)
        return "not found"

@app.route('/get-data/<file>')
def get_data(file):
    if file == 'data':
        f = open(os.path.join('data', 'data.csv'))
        f.readline() # remove header
        content = f.readlines()
        f.close()

        data = []
        for l in content:
            linearity, leniency, playability = l.strip().split(',')
            data.append([int(linearity), int(leniency), float(playability)])
        return json.dumps(data)

    return "not found"

@app.route("/")
def root():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', debug=True, port=port)
    app.run(host='0.0.0.0',threaded=True, port=port)