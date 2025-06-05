# Reflection & Argument

This project helped me see how important feature engineering is when building a classification model. I found that features like URL length, IP addresses, and special characters were very useful in spotting phishing attempts. It's not just about getting high accuracy (87%), but also about finding as many threats as possible. During testing, the model was able to catch 78% of the malicious URLs, which shows it works well, but there's still room to improve.

The Random Forest model did a good job using the features I created. At first, I had trouble because the data had more safe URLs than dangerous ones. I solved this by using class_weight and trying under-sampling, which helped the model detect more phishing links.

In the future, I want to try using neural networks to find more complex patterns in URLs. I also plan to test the model on real-time URLs, like ones from emails, and use deep learning to make the system smarter and better at catching new types of threats.

