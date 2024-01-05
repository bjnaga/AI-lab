from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay 

X, y = load_iris(return_X_y=True)
# print(load_iris(return_X_y=True))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
res = gnb.fit(X_train, y_train)
y_pred=res.predict(X_test)

# print(X_test)
print((y_test.shape)[0])
for i in range((y_test.shape)[0]):
    print(y_test[i],"  ",y_pred[i])
print("Number of mislabeled points out of a total %d points : %d"
% (X_test.shape[0], (y_test != y_pred).sum()))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()                              


# cm = confusion_matrix(y_test, y_pred) 
# print(cm)
