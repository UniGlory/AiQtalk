from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	return render_template('aiq_dashboard.html')

@app.route('/CCA8',methods=['GET', 'POST'])
def CCA8():
	return render_template('CCA8.html')

@app.route('/D8FE',methods=['GET', 'POST'])
def D8FE():
	return render_template('D8FE.html')

@app.route('/E89D',methods=['GET', 'POST'])
def E89D():
	return render_template('E89D.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True, threaded=True,processes=1)