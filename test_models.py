
import joblib

diabetes = joblib.load("models/diabetes_model.pkl")
heart = joblib.load("models/heart_model.pkl")
kidney = joblib.load("models/kidney_model.pkl")
cancer = joblib.load("models/cancer_model.pkl")

print("Diabetes:", diabetes.predict([[45, 32, 180]]))
print("Heart:", heart.predict([[55, 250, 150]]))
print("Kidney:", kidney.predict([[60, 3.0, 90]]))
print("Cancer:", cancer.predict([[65, 25, 20]]))

