# Computational Analysis of Migraine Symptoms and Severity

*Background*: Migraine, a prevalent and debilitating neurological disorder, presents significant challenges due to its complex symptomatology and varied triggers. This research employs integrative machine learning techniques to conduct a comprehensive analysis of migraine characteristics, aiming to enhance understanding and management strategies. The primary objectives include classifying migraine types based on diverse symptoms, predicting migraine intensity to assist in clinical assessments, uncovering latent relationships between symptoms through association rule mininga and identifying influential variables using recursive feature elimination (RFE).

*Methods*: We utilized machine learning models such as Logistic Regression, Decision Trees, Random Forests, Support Vector Machines (SVM), Gradient Boosting, K-Nearest Neighbors (KNN) and Deep Neural Network (DNN) to achieve these objectives. The dataset comprised various migraine symptoms and characteristics, which were preprocessed and subjected to the respective machine-learning algorithms. Classification algorithms were employed to categorize migraine types and predict the intensity of migraine attacks. Association rule mining, specifically the Apriori algorithm, was applied to identify patterns and relationships among symptoms. RFE was used to determine the most influential features in predicting migraine characteristics.

*Results*: The results demonstrated that machine learning techniques could effectively classify migraine types with high accuracy, predict migraine intensity, and uncover significant symptom relationships. The RFE identified key variables such as photophobia, phonophobia, and nausea as critical predictors of migraine characteristics. Clustering analysis revealed distinct migraine subgroups, providing insights into potential personalized treatment approaches.
Conclusion: This study highlights the potential of integrative machine learning methods to enhance the understanding of migraine patterns and severity. These findings can inform more precise diagnostic criteria and targeted treatment strategies, ultimately contributing to improved patient outcomes. The use of advanced machine learning techniques offers a promising avenue for migraine research, emphasizing the importance of data-driven approaches in tackling complex neurological disorders.


# Migraine Type Prediction

The Streamlit app predicts the type of migraine based on user input features.

## Running Locally

1. Install the requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
