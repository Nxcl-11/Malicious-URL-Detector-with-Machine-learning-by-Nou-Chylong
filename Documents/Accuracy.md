# Model Evaluation and Accuracy Interpretation


## 1. Classification Report    

           precision    recall  f1-score   support

      0         0.91      0.90      0.91    117920
      1         0.76      0.78      0.77     46886


Accuracy: 0.87                               Support: 164806


---

## 2. Overall Accuracy

- **Overall Accuracy = 0.87 (87%)**  
  This means the model correctly classified 87% of the URLs in the test set (164,806 total).  
  If you randomly pick one URL from the test set, there's an 87% chance the Random Forest model will correctly identify whether it's benign or malicious.

---

## 3. Breaking Down the Numbers

> **Support** refers to how many actual examples of each class are in the test set:  
> - Class **0 (Benign URLs)**: 117,920 samples  
> - Class **1 (Malicious URLs)**: 46,886 samples  

### Class 0 (Benign)

- **Precision = 0.91**  
  → 91% of the URLs predicted as “benign” were actually benign.  
- **Recall = 0.90**  
  → Out of all real benign URLs, 90% were correctly identified.  
- **F1‐Score = 0.91**  
  → Shows a balanced performance between precision and recall for benign URLs.

### Class 1 (Malicious)

- **Precision = 0.76**  
  → When the model predicts “malicious,” it's correct 76% of the time.  
- **Recall = 0.78**  
  → The model correctly detects 78% of all malicious URLs.  
- **F1‐Score = 0.77**  
  → A good result, but there’s still room to reduce missed threats and false positives.

---

## 4. Macro & Weighted Averages

- **Macro Avg (Precision 0.83 / Recall 0.84 / F1 0.84)**  
  → Treats both classes equally. Good balance between the two classes.

- **Weighted Avg (Precision 0.87 / Recall 0.87 / F1 0.87)**  
  → Takes into account the imbalance between benign and malicious samples. Performance is strong overall.

---

## 5. Key Takeaways

- ✅ **Overall Accuracy**: 87% of the URLs in the test set are classified correctly.  
- ✅ **Benign Detection**: Very strong (Precision: 0.91, Recall: 0.90).  
- ⚠️ **Malicious Detection**: Decent (Precision: 0.76, Recall: 0.78). About 3 out of 4 malicious URLs are detected.  
- 🔧 **Areas for Improvement**:  
  1. Increase **precision for malicious class** to reduce false alarms.  
  2. Increase **recall for malicious class** to catch more threats that are currently missed.

---
### Full Test Result
Link: https://github.com/Nxcl-11/Malicious-URL-Detector-with-Machine-learning-by-Nou-Chylong/blob/main/Accuracy%20Output/Full%20Test%20Result.png

### Confusion Metrix
Link: https://github.com/Nxcl-11/Malicious-URL-Detector-with-Machine-learning-by-Nou-Chylong/blob/main/Accuracy%20Output/Confusion_Matrix.png
### Roc Curve
Link: https://github.com/Nxcl-11/Malicious-URL-Detector-with-Machine-learning-by-Nou-Chylong/blob/main/Accuracy%20Output/ROC_Curve.png


