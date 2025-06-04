from pre_processing import preprocess_data
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix, accuracy_score,precision_score, recall_score, f1_score, log_loss, roc_auc_score,RocCurveDisplay)
import joblib

# -------------------------------
# Load and Preprocess Dataset
# -------------------------------
df = preprocess_data('Dataset/phishing_site_urls_2.csv')
print(f"Loaded {len(df)} URLs\n")

# -------------------------------
# Feature Extraction Function
# -------------------------------
def extract_features(url):
    url = url.lower()  # lowercase for consistency

    # Extract domain part
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

        # 🔥 New Features
        'is_exe_file': int(url.endswith('.exe')),  # common malicious pattern
        'domain_length': len(domain),
        'tld_is_suspicious': int(url.endswith(('.xyz', '.ru', '.tk', '.top', '.info')))  # risky TLDs
    }


# -------------------------------
# Feature Extraction
# -------------------------------
features = df['URL'].apply(extract_features)
features_df = pd.DataFrame(features.tolist())
features_df['Label'] = df['Label']

# -------------------------------
# Train-Test Split (70%/30%)
# -------------------------------
X = features_df.drop('Label', axis=1)
y = features_df['Label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, shuffle=True
)

# -------------------------------
# Train Random Forest Model
# -------------------------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=25,
    class_weight='balanced_subsample',
    random_state=42
)


model.fit(X_train, y_train)

# -------------------------------
# Predict & Evaluate
# -------------------------------
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
logloss = log_loss(y_test, y_proba)
roc_auc = roc_auc_score(y_test, y_proba[:, 1])

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print(f" Accuracy:   {accuracy:.4f}")

# -------------------------------
# Confusion Matrix Plot
# -------------------------------
plt.figure()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -------------------------------
# ROC Curve Plot
# -------------------------------
plt.figure()
RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.title("ROC Curve")
plt.show()

# -------------------------------
# Save Model and Report
# -------------------------------
joblib.dump(model, 'url_detector_model.pkl')
print(" Model saved as url_detector_model.pkl")

