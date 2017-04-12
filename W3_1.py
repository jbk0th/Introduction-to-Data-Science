import pandas as pd
import numpy as np
import os

os.chdir('C:\\Users\\Jason\\Introduction-to-Data-Science') #changes the directory of the script into the correct one to access the 'Energy Indicators file
os.getcwd() #shows current working directory
#df = pd.read_excel('C:\\Users\\Jason\\Introduction-to-Data-Science\\Energy Indicators.xls')
	#the above method works as well for reading in the file with the full path name
df = pd.read_excel('Energy Indicators.xls',header=1)