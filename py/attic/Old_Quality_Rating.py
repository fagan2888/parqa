import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import datetime
import pickle as pkl
import os
import csv
import geopandas as gp 

filePath = sys.argv[1]
filePath2 = sys.argv[2]

#def Read_Files(filePath):
inspection = pd.read_excel(filePath+"PIP_InspectionMain.xlsx")
parksProperties = gp.GeoDataFrame.from_file(filePath2+"Property.shp")

#Global Dictonaries
zipPass = {}



for park in parksProperties.iterrows():
	ID = park[1][8]
	zipCode = park[1][23]
	zipCodeFive = zipCode[:5]
	if zipPass.get(zipCodeFive) == None:
		zipPass[zipCodeFive] = {'Failed':0, 'Count':0}
	for feature in inspection.iterrows():
	    parkID = feature[1][0]
	    year = feature[1][6]
	    passI = feature[1][7]
	    if year == "2014":
	    	if parkID == ID:
		    	if passI <> "A":
		    		zipPass[zipCodeFive]['Failed']+=1
		    	zipPass[zipCodeFive]['Count']+=1

with open('../Outputs/Park_Quality_Ratings/ParkOldRating.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['ZipCode','Failed','Count'])
	for i in zipPass:
		spamwriter.writerow([i,zipPass[i[0]],zipPass[i[1]]])
