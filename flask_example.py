from flask import Flask
# from analysis_dash import app

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>bla bla bla </p>"

if __name__ == '__main__':
	# app.run_server(debug=True, host='0.0.0.0', port=5083)
    app.run(debug=True, host='0.0.0.0', port=5083)