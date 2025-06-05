import joblib
import pandas as pd
import re

# Your improved feature extractor
def extract_features(url):
    url = url.lower()
    domain = url.split('/')[0]
    return {
        'url_length': len(url),
        'num_digits': sum(c.isdigit() for c in url),
        'num_special_char': len(re.findall(r'\W', url)),
        'has_https': int('https' in url),
        'num_dots': url.count('.'),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'has_suspicious_words': int(any(word in url for word in [
            'login', 'verify', 'update', 'secure', 'account', 'bank', 'webscr', 'signin'
        ])),
        'is_exe_file': int(url.endswith('.exe')),
        'domain_length': len(domain),
        'tld_is_suspicious': int(url.endswith(('.xyz', '.ru', '.tk', '.top', '.info')))
    }

# Load model
model = joblib.load("url_detector_model.pkl")

# Input
url = input("Enter a URL to check: ")

# Extract features and predict
features = extract_features(url)
prediction = model.predict(pd.DataFrame([features]))[0]

# Output
print("🔴 This URL is Malicious" if prediction == 1 else "🟢 This URL is Benign")
