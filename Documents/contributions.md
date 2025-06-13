# Contributions

1. Loaded and explored the dataset (`phishing_site_urls_2.csv`) using pandas to understand its structure and size.
2. Visualized class distribution using Seaborn, confirming a significant class imbalance between benign and malicious URLs.
3. Performed data preprocessing:
   - Removed very short URLs
   - Clipped extreme values for special character count (max 30)
   - Checked and confirmed that there were no missing values
4. Engineered relevant features from each URL using a custom `extract_features()` function, including URL length, digit count, special characters, HTTPS, presence of IP address, suspicious keywords, TLDs, and more.
5. Split the cleaned dataset into 70% for training and 30% for testing using `train_test_split()`.
6. Trained the model using a Random Forest Classifier.
7. Due to dataset imbalance, I tuned the hyperparameters to improve the model:
   - `n_estimators=300`
   - `max_depth=25`
   - `class_weight='balanced_subsample'` to handle class imbalance
8. Evaluated the model using a classification report (precision, recall, F1-score), confusion matrix, and ROC curve.
9. Saved the trained model as a `url_detector_model.pkl` file using `joblib.dump()` for future testing.
10. Test the model manually myself.

