from mario_vglc_grammars.Grammar.BackoffNGram import BackoffNGram
from typing import IO
from flask import Flask, render_template
import json
import os

from mario_vglc_grammars.Generation.Constrained import generate_from_start_to_end
from mario_vglc_grammars.IO.GetLevels import get_super_mario_bros, rows_into_columns
from mario_vglc_grammars.Utility import columns_into_rows
from mario_vglc_grammars.Grammar import NGram

grammar = NGram(3)
for lvl in get_super_mario_bros():
    grammar.add_sequence(lvl)

app = Flask(__name__)

@app.route('/get-combo/<start>/<end>')
def get_combo(start, end):
    try:
        f = open(os.path.join('data', 'levels', f'{int(start)}.txt'))
        start_map = rows_into_columns(f.readlines())
        f.close()

        f = open(os.path.join('data', 'levels', f'{int(end)}.txt'))
        end_map = rows_into_columns(f.readlines())
        f.close()
        
        combined_map, length = generate_from_start_to_end(grammar, start_map, end_map, 0, include_path_length=True)
        return f'{columns_into_rows(combined_map)}\n\nLinker Length: {length}'
    except Exception as e:
        print(e)
        return "not found"

@app.route('/get-map/<index>')
def get_map(index):
    try:
        f = open(os.path.join('data', 'levels', f'{int(index)}.txt'))
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
    app.run(host='0.0.0.0', debug=True, port=port)
    # app.run(host='0.0.0.0',threaded=True, port=port)