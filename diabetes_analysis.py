"""import csv
import json

csvfile = open('D://mchine learning bvp//ina_singhal//diabetes.csv',encoding="utf-8")
jsonfile = open('D://mchine learning bvp//ina_singhal//diabetes_data.json',"w")

fieldnames = ("Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    out=json.dumps([ row for row in reader ])
    jsonfile.write(out)
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
data=open("D://mchine learning bvp//ina_singhal//diabetes_data.json","r")
mydata=json.loads(data.readline())

#1.
l1=list()
for i in range(len(mydata)):
	try:
		a=int(mydata[i]["Pregnancies"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l1.append(a)
	except:
		continue
print(l1)
plt.hist(l1,bins=100)
plt.show()



#2.
l2=list()
for i in range(len(mydata)):
	try:
		a=int(mydata[i]["Glucose"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l2.append(a)
	except:
		continue
l2.sort()
print(l2)
plt.hist(l2,bins=100)
plt.show()


#3.
l3=list()
for i in range(len(mydata)):
	try:
		a=int(mydata[i]["BloodPressure"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l3.append(a)
	except:
		continue
l3.sort()
print(l3)
plt.hist(l3,bins=100)
plt.show()



#4.
l4=list()
for i in range(len(mydata)):
	try:
		a=int(mydata[i]["SkinThickness"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l4.append(a)
	except:
		continue
l4.sort()
print(l4)
plt.hist(l4,bins=100)
plt.show()



#5.
l5=list()
for i in range(len(mydata)):
	try:
		a=int(mydata[i]["BMI"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l5.append(a)
	except:
		continue
l5.sort()
print(l5)
plt.hist(l5,bins=100)
plt.show()




#6.
l6=list()
for i in range(len(mydata)):
	try:
		a=float(mydata[i]["DiabetesPedigreeFunction"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l6.append(a)
	except:
		continue
l6.sort()
print(l6)
plt.hist(l6,bins=100)
plt.show()


#7.
l7=list()
for i in range(len(mydata)):
	try:
		a=float(mydata[i]["Age"])
		b=int(mydata[i]["Outcome"])
		if(b==1):
			l7.append(a)
	except:
		continue
l7.sort()
print(l7)
plt.hist(l7,bins=100)
plt.show()