import joblib
import re
import pandas as pd
from detector import extract_features

model = joblib.load("url_detector_model.pkl")



url = input("Enter URL: ")
features = extract_features(url)

prediction = model.predict(pd.DataFrame([features]))[0]

print("This URL is Malicious" if prediction == 1 else "This URL is Benign")
