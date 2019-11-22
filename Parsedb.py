import pandas
import numpy as np
from sklearn.model_selection import train_test_split

data2 = pandas.read_csv('bd/renal.csv')
data = np.asarray(data2)
#print(type(data))
#print( data.shape )
for i in data:
	#col1
	if i[0]=='?':
		i[0]=-1
	else:
		i[0]=float(i[0])

	if i[1]=='?':
		i[1]=-1
	else:
		i[1]=float(i[1])

	if i[2]=='?':
		i[2]=-1
	else:
		i[2]=float(i[2])

	if i[3]=='?':
		i[3]=-1
	else:
		i[3]=float(i[3])

	if i[4]=='?':
		i[4]=-1
	else:
		i[4]=float(i[4])

	if i[5]=='normal':
		i[5]=1
	if i[5]=='abnormal':
		i[5]=0
	if i[5]=='?':
		i[5]=-1

	if i[6]=='normal':
		i[6]=1
	if i[6]=='abnormal':
		i[6]=0
	if i[6]=='?':
		i[6]=-1

	if i[7]=='present':
		i[7]=1
	if i[7]=='notpresent':
		i[7]=0
	if i[7]=='?':
		i[7]=-1

	if i[8]=='present':
		i[8]=1
	if i[8]=='notpresent':
		i[8]=0
	if i[8]=='?':
		i[8]=-1

	if i[9]=='?':
		i[9]=-1
	else:
		i[9]=float(i[9])

	if i[10]=='?':
		i[10]=-1
	else:
		i[10]=float(i[10])

	if i[11]=='?':
		i[11]=-1
	else:
		i[11]=float(i[11])

	if i[12]=='?':
		i[12]=-1
	else:
		i[12]=float(i[12])

	if i[13]=='?':
		i[13]=-1
	else:
		i[13]=float(i[13])

	if i[14]=='?':
		i[14]=-1
	else:
		i[14]=float(i[14])

	if i[15]=='?':
		i[15]=-1
	else:
		i[15]=float(i[15])

	if i[16]=='?':
		i[16]=-1
	else:
		i[16]=float(i[16])

	if i[17]=='?':
		i[17]=-1
	else:
		i[17]=float(i[17])

	if i[18]=='yes':
		i[18]=1
	if i[18]=='no':
		i[18]=0
	if i[18]=='?':
		i[18]=-1

	if i[19]=='yes':
		i[19]=1
	if i[19]=='no':
		i[19]=0
	if i[19]=='?':
		i[19]=-1

	if i[20]=='yes':
		i[20]=1
	if i[20]=='no':
		i[20]=0
	if i[20]=='?':
		i[20]=-1

	if i[21]=='good':
		i[21]=1
	if i[21]=='poor':
		i[21]=0
	if i[21]=='?':
		i[21]=-1

	if i[22]=='yes':
		i[22]=1
	if i[22]=='no':
		i[22]=0
	if i[22]=='?':
		i[22]=-1

	if i[23]=='yes':
		i[23]=1
	if i[23]=='no':
		i[23]=0
	if i[23]=='?':
		i[23]=-1

	if i[24]=='ckd':
		i[24]=1
	if i[24]=='notckd':
		i[24]=0		

# print( type(data[2][3]))
# print( data[2][3] )
dataParam = np.ndarray((400,24))  #Vector de parametros
dataDiag = np.ndarray((400))    #Etiquetas

for i in range(400):
	for j in range(24):

		dataParam[i][j]=data[i][j]
	dataDiag[i]=data[i][24]


trainParam, testParam, trainDiag, testDiag = train_test_split( dataParam, dataDiag, test_size=0.2, random_state=3 )
np.save('trainParam.npy',trainParam)
np.save('trainDiag.npy',trainDiag)
np.save('testParam.npy',testParam)
np.save('testDiag.npy',testDiag)
