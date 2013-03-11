#!/usr/bin/env python

import csv

#Prints the input requests
print ""
print "Csv 2 LaTeX."
print "Written by Dr. V A Knight"
print "www.vincent-knight.com"
print ""


#the variable 'inputpath' should be the location of the csv file that will be converted to LaTeX code (to be input by the user)
inputpath=raw_input("Please input the path of the data file (q to exit): ")

if inputpath in ["q","exit","exit()","q()"]:
	print ""
	exit()

if inputpath[:2]!="./":
	inputpath="./"+inputpath


#a bit of code that adds the csv file extension if this was not input by the user (this is just to make things look nice)
if inputpath[-4:]!=".csv":
	if inputpath[-4]==".":
		print ""
		print "Please ensure the input data set is a .csv file"
		print ""
		exit()
	inputpath+=".csv"

#the variable 'outputpath' will be the location of the text file with the LaTeX code (the code is complicated only to ensure a nice naming of the output variable).
outputpath=inputpath[:len(inputpath)-inputpath[::-1].index('/')]+"csv2latex-"+inputpath[len(inputpath)-inputpath[::-1].index('/'):len(inputpath)-4]+".txt"

#This initialises the reader module and reads in the data.
Reader=csv.reader(open(inputpath,'rb'))
data=[row for row in Reader]

#Calculates the dimension of the data to be converted.
rows=len(data)
cols=max([len(row) for row in data])

#Outputs a message displaying information regarding the dataset and the location of the text file with the LaTeX code.
print ''
print "Your data set has",rows,"rows and",cols,"columns. Paste the following code in to your LaTeX document or copy the contents of the file located at '"+outputpath[1:]+"'."

#A quick check that outputs a caution message if the number of variables in the columns of data is not uniform.
if cols!=min([len(row) for row in data]):
	print ""
	print "CAUTION: All the rows of your data DO NOT have the same number of non empty column entries. You might need to modify the output. (It will still compile.)"

#This creates (and prints to the terminal screen) the data set "output data" which is the LaTeX code 
tabular_parameters=cols*'c'
print ''
output_data=[]
output_data.append(['\\begin{tabular}{%s}' % tabular_parameters])
print '\\begin{tabular}{%s}'% tabular_parameters
for i in range(len(data)):
	a=""
	for j in range(len(data[i])):
		a+=data[i][j]
		if j<len(data[i]):
			a+="&"

	if len(data[i])<cols:
		a+=(cols-len(data[i]))*"&"
	a=a[:-1]
	a+="\\\\"
	print a
	output_data.append([a])
output_data.append(["\end{tabular}"])
print "\end{tabular}"
print ''

#This outputs the data set to the outputpath text file.
writer=csv.writer(open(outputpath,'w'))
for i in range(len(output_data)):
	writer.writerow(output_data[i])


