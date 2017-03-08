x = 1
y = 2
x + y

def add_numbers(x,y,z = None, flag=False):
	if (flag):
		print('Flag is True')
	if (z == None):
		return x + y
	else:
		return x + y + z
#print(add_numbers(1,3,flag=True))

#assign a function to a variable
a = add_numbers
#print(a(1,2,flag=True))

#Python Programming Language: Types and Sequences

#Tuple has () instead of brackets, immutable
x = (1,'a',3,'b') #tuples are immutbale, cannot be altereda
#print(type(x))
c = [1,'a',3, 'h']
#lists are mutable so the values, and of it and the number of them can be changed
#print(type(c))

#append a list

# c.append(3.3)
# print(c)

# for item in c:
	# print(item)
#i = 0 
# while( i != len(c)):
	# print(c[i])
	# i = i + 1
	
#for strings variable[:] <- slice operator goes from start to just before end number
#	
# firstname = 'Jason Brian Koth'.split(' ')[0] #[0] selects the first element of the list
# lastname = 'Jason Brian Koth'.split(' ')[-1] #[-1] selects the last element of the list
# #focuses the list split on a specific character
# print(firstname)
# print(lastname)

#must convert objects to strings before concatenating

#dictionaries associate keys with values
#Dictionary Representation
x = {'Chris Brooks':'brooksch@umich.edu','Bill Gates':'billg@microsoft.com'}
#Retrieve a value by indexing the keys
x['Kevyn Collins-Thompson'] = None
#itreate over all the keys
# for name in x:
	# print(x[name])

#iterate over all the values in a list
# for name, email in x.items():
	# print(name)
	# print(email)
x = ('Christopher','Brooks','brooksch@umich.edu')
# fname, lname, email = x	

# sales_record = {
# 'price' : 3.24,
# 'num_items': 4,
# 'person' :'Chris'}

# sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'
# print(sales_statement.format(sales_record['person'],sales_record['num_items'],sales_record['price'],sales_record['num_items']*sales_record['price']))

########
#Reading and Writing CSV Files
########
import csv

 
with open('mpg.csv') as csvfile:
	mpg = list(csv.DictReader(csvfile))
#Each row becomes a dictionary, and if fieldnames is omitted the first row becomes the keys for all the subsequent entires in each dictionary, IMPT each row becomes a dictionary

mpg[:3]

mpg[0].keys()
#keys() gives us the column names of our csv

#find the average cty fuel economy across all carss. All values in the dictionaries are strings so we need to convert to float
#uses d as an iterable variable across all dictionaries in the list, then it index that key and sums it for each cty mileage thats been pull from the mpg

sum(float(d['cty']) for d in mpg)/len(mpg)

sum(float(d['hwy']) for d in mpg) / len(mpg)

##set returns the unique values for a particular set



cylinders = set(d['cyl'] for d in mpg)
cylinders

#grouping the cars by number of cyliner and finding the average cty mpg for each grouping


CtyMpgByCyl = []

for c in cylinders: #iterate over all cylinder levels
	summpg = 0
	cyltypecount = 0
	for d in mpg: #iterate over all dictionaries in mpg
		if d['cyl'] == c: # if the cylinder level type matches, the current type being iterated over in the outer for loop
			summpg += float(d['cty']) # add the cty mpg
			cyltypecount += 1 #increment the count for the total number of cylinders in that count 'i.e 4'
	CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the list with the tuple ('cylinder', and avg mpg)
CtyMpgByCyl.sort(key=lambda x:x[0])
CtyMpgByCyl

vehicleclass = set(d['class'] for d in mpg) #what are the unique class 'types'
print(vehicleclass)

HwyMpgByClass = []

for t in vehicleclass: #iterate over all the vehicle class (think of the returned set as dictionary keys)
	summpg = 0
	vclasscount = 0
	for d in mpg: #iterate over all dictionaries
		if d['class'] == t: # if the cylinder amount type matches
			summpg += float(d['hwy'])
			vclasscount += 1 #increment the count for number counts / this vehicleclass
	HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple to the list
	
HwyMpgByClass.sort(key = lambda x: x[1])
print(HwyMpgByClass)























	
	
