from flask import jsonify, request, Response
import pandas as pd

from app import app
from app import model
from app import dataCtrl


@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"


@app.route('/predictAll', methods=['GET'])
def predictAll():
	return Response(dataCtrl.predictAll(), mimetype='application/json')


@app.route('/predictTest', methods=['GET'])
def predict():
	#data = request.get_json()

	data = [[501865778,34.047,355.074,268.321,24.11,78.68,7.68,15.74,99.84,304.76,0.0,0.0,0.0,0.0,0.0,0.0,40.31,178.53,312.44,26.83,104.23,423.28,4,9,11,74,384,283,0.0,1.0,2.0,0.0,154.0,50.0,33.53333333333333,24,15,1,27,8,12,0,1.0,0.0,3.0,60.0,6.0,21.0,1.0,182.735,0.0],
	[501625959,167.69,189.058,210.226,11.54,55.24,37.26,143.33,220.59,208.36,0.0,0.0,0.0,0.0,0.0,0.0,155.33,412.94,285.46,370.04,519.53,395.03,5,4,2,168,315,116,0.0,0.0,0.0,0.0,0.0,0.0,36.766666666666666,24,2,11,26,20,11,0,13.0,7.0,17.0,60.0,60.0,60.0,0.0,0.0,0.0],
	[501204172,221.338,251.102,508.054,99.91,54.39,310.98,123.31,109.01,71.68,0.0,54.86,44.38,0.0,28.09,39.04,223.23,135.31,352.21,280.08,216.61,53.13,10,11,18,230,310,601,0.0,0.0,0.0,0.0,0.0,0.0,83.03333333333333,1,11,4,15,11,1,0,2.0,0.0,0.0,60.0,60.0,60.0,0.0,0.0,0.0],
	[500142493,261.636,309.876,238.174,50.31,149.44,83.89,76.96,91.88,124.26,0.0,0.0,0.0,0.0,0.0,0.0,127.28,241.33,208.16,216.44,198.29,338.81,5,6,3,196,350,287,1.0,0.0,0.0,56.0,0.0,0.0,50.86666666666667,36,11,3,20,18,15,0,4.0,3.0,22.0,26.0,60.0,60.0,0.0,0.0,0.0],
	[501051193,429.023,190.704,255.114,71.03,45.03,76.66,262.73,49.24,92.08,0.0,0.0,0.0,0.0,0.0,0.0,333.76,94.81,168.74,2128.41,1788.06,2167.11,15,10,11,499,222,294,0.0,0.0,0.0,0.0,0.0,0.0,55.76666666666666,15,1,1,25,1,9,0,2.0,0.0,3.0,60.0,60.0,60.0,0.0,0.0,0.0]
	]
	#data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
	#df = pd.DataFrame.from_dict(data["data"])
	#return "data: \n{0}".format(type(data["data"]))
	#return "type: {0} \n data: {1}".format(type(data),data)
	return Response(model.predict(data), mimetype='application/json')

   #return "args: {0}".format(request.args.get('key'))
	#return "args: {0}".format(request.get_json())

