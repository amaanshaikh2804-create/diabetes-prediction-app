Diabetes-Prediction-Using-Machine-Learning
📌 Project Overview
A Machine Learning project to predict diabetes using medical data.
The project includes data cleaning, EDA, preprocessing, and model evaluation.
Naive Bayes, Random Forest, and Logistic Regression are used for prediction.

🎯 Objective
The main objective of this project is to build a Machine Learning model that predicts whether a person is likely to have diabetes based on medical and demographic features.

📊 Dataset
The project uses the Pima Diabetes Dataset stored in an Excel file named:

pima-data.xlsx

The dataset contains 768 records.

Features
num_preg - Number of pregnancies
glucose_conc - Plasma glucose concentration
diastolic_bp - Diastolic blood pressure
insulin - Insulin level
bmi - Body Mass Index
diab_pred - Diabetes pedigree function
age - Age of the person
Target Variable
diabetes

1 - Diabetes
0 - No Diabetes
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook
Excel
🔄 Project Workflow
The project follows these steps:

Data Loading
Data Understanding
Exploratory Data Analysis (EDA)
Data Cleaning
Correlation Analysis
Handling Missing Values
Train-Test Split
Model Training
Model Evaluation
Model Comparison
🧹 Data Preprocessing
The dataset is cleaned by removing unnecessary columns and converting the target variable into numerical form.

Some medical features contain 0 values that can represent missing or invalid values. These values are handled using SimpleImputer with the mean strategy.

The dataset is then divided into:

70% Training Data
30% Testing Data
🤖 Machine Learning Models
1. Gaussian Naive Bayes
Gaussian Naive Bayes is used as one of the classification models to predict diabetes.

2. Random Forest Classifier
Random Forest is an ensemble learning algorithm that uses multiple decision trees to make predictions.

3. Logistic Regression
Logistic Regression is used for binary classification to predict whether a person has diabetes or not.

📈 Model Performance
The models achieved the following test accuracy:

Model	Accuracy
Gaussian Naive Bayes	~74.9%
Random Forest	~76.2%
Logistic Regression	~69.3%
Random Forest achieved approximately 76.2% test accuracy on the given train-test split.

📊 Evaluation Metrics
The models are evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
Classification Report
For the Random Forest model, the confusion matrix was:

[[122  29]
 [ 26  54]]
For the diabetes class (1):
Precision: ~65% Recall: ~68% F1-Score: ~66%

📁 Project Structure
Diabetes-Prediction/ │ ├── ML Project- diabetes prediction_day1&2.ipynb ├── pima-data.xlsx └── README.md

How to Run the Project
Clone the Repository git clone https://github.com/your-username/Diabetes-Prediction.git
Install Required Libraries pip install pandas numpy matplotlib scikit-learn openpyxl
Open the Notebook Open the following file in Jupyter Notebook or JupyterLab: ML Project- diabetes prediction_day1&2.ipynb
Run the Project Run the notebook cells from top to bottom.
Make sure pima-data.xlsx is present in the same project folder.

💡 Key Learnings
Through this project, I practiced:

Data Loading
Exploratory Data Analysis
Data Cleaning
Missing Value Handling
Data Preprocessing
Train-Test Split
Classification Algorithms
Naive Bayes
Random Forest
Logistic Regression
Confusion Matrix
Model Evaluation
Performance Comparison
⚠️ Disclaimer
This project is created for educational and Machine Learning practice purposes.

The predictions from this project should not be considered a medical diagnosis or a substitute for professional medical advice.

👨‍💻 Author
Amaan Shaikh
amaanshaikh2804@gmail.com

Machine Learning | Data Science | AI & ML