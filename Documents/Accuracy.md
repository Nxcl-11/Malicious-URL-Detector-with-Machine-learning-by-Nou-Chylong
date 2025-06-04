# Model Evaluation and Accuracy Interpretation


## 1. Classification Report    
precision    recall  f1‐score   support
    0         0.92      0.90      0.91    118040
    1         0.68      0.73      0.71     34123

accuracy                          0.86    152163

---


- **Overall Accuracy = 0.8635 (86.35 %)**  
  - This number tells us that out of all the URLs in the test set (15,2163 examples), the model correctly classified about 86.35 % of them. In other words, if you randomly pick one URL from the held‐out test set, there’s an 86.35 % chance that our Random Forest detector will label it correctly (benign vs. malicious).

---

## 3. Breaking Down the Numbers

> **Support** refers to how many actual examples of each class are in the test set:  
> - Class **0 (Benign URLs): 118,040 samples**  
> - Class **1 (Malicious URLs): 34,123 samples**  

1. **Class 0 (Benign)**  
   - *Precision = 0.92*  
     - Out of all URLs predicted as “benign,” 92 % truly were benign.  
   - *Recall = 0.90*  
     - Of all actual benign URLs, the model correctly labeled 90 % as benign.  
   - *F1‐Score = 0.91*  
     - A harmonic mean of precision and recall—so the model achieves a balanced performance (0.91) on benign URL detection.

2. **Class 1 (Malicious)**  
   - *Precision = 0.68*  
     - Of all URLs predicted as “malicious,” 68 % actually were malicious. In other words, whenever the model raises a “malicious” flag, it’s right about two-thirds of the time.  
   - *Recall = 0.73*  
     - Out of all truly malicious URLs, the model catches 73 % of them. This means it misses about 27 % of malicious URLs in the test set (false negatives).  
   - *F1‐Score = 0.71*  
     - This balances precision and recall for the malicious class. A 0.71 indicates there is room for improvement.

3. **Macro & Weighted Averages**  
   - *Macro Avg (Precision 0.80 / Recall 0.82 / F1 0.81)*  
     - This treats both classes equally, regardless of how many samples each has. It shows that on average (class 0 & class 1), the model’s performance is around 0.81.  
   - *Weighted Avg (Precision 0.87 / Recall 0.86 / F1 0.87)*  
     - This takes into account the imbalance (there are more benign URLs than malicious). Since class 0 is larger, its higher precision/recall has a bigger impact on the weighted scores.

---


1. **Why 86.35 % Is Meaningful**  
   - An accuracy of 86.35 % is a strong indicator that, overall, the model can correctly distinguish between benign and malicious URLs most of the time.  
   - Given the imbalance (more benign than malicious samples), a naive “always-predict-benign” classifier would achieve about 77.6 % accuracy (118,040 / 152,163). This Random Forest model outperforms that baseline by a significant margin (86.35 % vs. 77.6 %).

---

## 5. Key Takeaways

- **Overall:** The model correctly classifies **86.35 %** of URLs in the test set.  
- **Benign Detection:** Very strong (Precision 0.92, Recall 0.90). Few benign URLs are mislabeled.  
- **Malicious Detection:** Moderately strong (Precision 0.68, Recall 0.73). Roughly 7 out of every 10 malicious URLs are flagged correctly.  
- **Areas for Improvement:**  
  1. Increase **class 1 precision** so fewer benign URLs are flagged as malicious.  
  2. Increase **class 1 recall** so fewer malicious URLs slip through undetected.


