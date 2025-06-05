## 6. Methodology

### 1. Loading Libraries
Necessary libraries were imported including `pandas`, `numpy`, `re`, `matplotlib`, `seaborn`, and relevant modules from `sklearn`.

### 2. Dataset Loading and Inspection
The dataset was loaded using Pandas and inspected using `df.info()` to understand the structure.

### 3. Class Distribution Visualization
The class distribution was visualized using Seaborn's `countplot`.

### Feature Engineering
Features were extracted using regular expressions and logical rules from URLs. Each URL was transformed into a set of numerical indicators and compiled into a `DataFrame`. These features include:
- URL length
- Number of digits
- Number of special characters
- Use of HTTPS
- Number of dots
- Presence of IP address
- Suspicious keywords (e.g., login, secure)
- Executable file extension
- Domain length
- Suspicious top-level domains (e.g., .ru, .xyz)

### 4. Data Cleaning
- URLs shorter than 5 characters were removed.
- Outliers in the `num_special_char` feature were winsorized by clipping values to a maximum of 30.
- Missing values were checked and confirmed to be zero.

### 5. Feature Scaling with Z-Score
The predictor variables were standardized using the Z-score method to normalize feature values and ensure balanced influence across features.

### 6. Train-Test Split
The dataset was split into training and testing sets using a 70/30 ratio. The `random_state` was set to ensure reproducibility.

### 7. Model Training
A Random Forest Classifier was initialized with the following parameters:
- `n_estimators=300`
- `max_depth=25`
- `class_weight='balanced_subsample'`
- `random_state=42`

The model was trained on the standardized training set.

### 8. Prediction and Evaluation
Predictions were made on the test set. A classification report was generated showing precision, recall, and F1-score.
- Accuracy achieved: **87%**
- Strong performance across both classes

### 9. Confusion Matrix Visualization
A confusion matrix was plotted using Seaborn to visualize performance in terms of true positives, true negatives, false positives, and false negatives.

### 10. ROC Curve
A ROC Curve was plotted using Scikit-learn's `RocCurveDisplay` to evaluate the model's performance in distinguishing between the classes based on probability outputs.
