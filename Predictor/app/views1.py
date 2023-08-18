from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
import pandas as pd


def predict1(request):
	return render(request, "predict1.html")

def result1(request):
	dataframe = pd.read_csv(("D:\CSVpython\carsmpg.csv"))
	Y = dataframe["mpg"]
	X = dataframe.drop(["mpg","car name","horsepower","model year","origin"], axis=1)
	
	

	X_train, X_test, Y_train,Y_test = train_test_split(X, Y, test_size=0.2)

	model1 = RandomForestRegressor()
	model1.fit(X_train, Y_train)

	val66 = request.GET['n10']
	val67 = request.GET['n11']
	val63 = request.GET['n12']
	val64 = request.GET['n13']
	
	pred = model1.predict([[val66, val67, val63,val64]])
	return render(request, "predict1.html",
				{"result3": pred})
	
