# 📚 Smart Study Time Recommender

##  Overview
The Smart Study Time Recommender is an AI-based system designed to help students efficiently plan their study time across multiple subjects. It analyzes key factors such as subject difficulty, preparation level, importance, and exam proximity to predict the optimal number of study hours required for each subject.

The system uses a combination of a Decision Tree machine learning model and rule-based logic to generate realistic and personalized recommendations. It then organizes all subjects into a structured study plan, prioritizing them based on urgency and required effort.

This project helps to demonstrate how fundamental AI and learning concepts can be applied to solve a practical, real-world problem faced by students in everyday academic life.
---

##  Objective
The objective of this project is to help students efficiently allocate their study time across multiple subjects by using artificial intelligence techniques. It aims to provide personalized study recommendations based on factors such as difficulty, preparation level, importance, and exam proximity.

Additionally, the project demonstrates the practical application of fundamental AI and machine learning concepts by building a system that can predict, prioritize, and organize study tasks in a structured and meaningful way.

---

##  AI Concepts Used
- **Supervised Learning:** A Decision Tree Regressor is used to predict study hours based on input features.  
- **Feature-Based Prediction:** Inputs such as difficulty, preparation level, importance, and days left are used as features for prediction.  
- **Rule-Based Decision Logic:** Additional rules are applied to refine predictions and make them more realistic.  
- **Data-Driven Modeling:** The model learns patterns from sample data to generate recommendations for new inputs.  

---
##  Features
- Supports multiple subjects in a single run  
- Predicts study hours using a Decision Tree model  
- Applies rule-based adjustments for realistic recommendations  
- Assigns priority levels (Low / Moderate / High / Very High)  
- Provides personalized study advice for each subject  
- Organizes results into a structured and sorted study plan  
- Calculates total study time across all subjects  
- Validates user input for accuracy and reliability

  
##  How It Works

### Inputs:
1. Number of subjects  
2. For each subject:
   - Subject Name  
   - Difficulty (1–5)  
   - Days Left before exam (1–30)  
   - Preparation Level (1–5)  
   - Importance (1–5)  

---

### Outputs:
For each subject:
- Recommended study hours  
- Priority level (Low / Moderate / High / Very High)  
- Study advice  

Final Output:
- Organized study plan (all subjects in a table)  
- Subjects sorted by highest study time required  
- Total study hours required for all subjects  

## Tech Stack

- Python
- Pandas
- Scikit-learn

---

## Installation & Setup

### Step 1: Install Python
- Make sure Python 3.8+ is installed  
- Check using:python --version


### Step 2: Clone the Repository
- git clone https://github.com/abeer23456/CSA_2001abeer25bce11186smartstudytimerecommender.git
- cd CSA_2001abeer25bce11186smartstudytimerecommender
---

### Step 3: Install Dependencies
- pip install -r requirements.txt

  
## Run the Program
python app.py


##  Author
Abeer Gupta
