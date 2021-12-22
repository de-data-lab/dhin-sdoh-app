from flask import Flask, Response, jsonify, make_response, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = False

dhin_cwi_df = pd.read_csv('data/dhin-cwi.csv')

@app.route('/data', methods = ['GET'])
def get_data():
    result_df = dhin_cwi_df.copy()
    year = request.args.get('year') if request.args.get('year') else None
    if year:
        result_df = result_df[result_df['year'] == int(year)]
    result = result_df.to_json(orient='records')

    return Response(result, mimetype='application/json')

if (__name__ == "__main__"):
     app.run(host = '0.0.0.0', port = 8000)
