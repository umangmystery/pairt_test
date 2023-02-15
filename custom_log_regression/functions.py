from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression




def use_standard_scaling(X_train, X_test):
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)

	return X_train, X_test

def log_regression_pred(X_train, y_train, X_test):
	classifier = LogisticRegression()
	classifier.fit(X_train,y_train)
	y_pred = classifier.predict(X_test)
	return y_pred

def main():
	pass

if __name__ == "__main__":
	main()