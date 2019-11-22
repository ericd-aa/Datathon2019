
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from joblib import dump


trainParam = np.load('trainParam.npy')
trainDiag = np.load('trainDiag.npy')
testParam = np.load('testParam.npy')
testDiag = np.load('testDiag.npy')

model = SVC(kernel='linear', C=0.1)
model.fit(trainParam, trainDiag)

trainPred=model.predict(trainParam)
testPred=model.predict(testParam)

trainAcc=accuracy_score(trainDiag,trainPred)
testAcc=accuracy_score(testDiag,testPred)

print( 'Accuracy train:  '+str(trainAcc) )
print( 'Accuracy test:  '+str(testAcc) )

dump(model,'modelSVCLinear.joblib')