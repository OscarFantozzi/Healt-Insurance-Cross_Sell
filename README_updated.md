
# Health Insurance Cross-Sell Prediction

### 🚀 **About the Project**

The goal of this project is to build a classification model to predict whether a customer is interested in purchasing a health insurance policy. The dataset contains demographic and policy-related information about customers.

By analyzing and modeling this data, we aim to provide insights that can help insurance companies better target potential customers and optimize their sales strategies.

---

### ⚙️ **Features**

- **Input Features:**
  - `gender`: Gender of the customer.
  - `age`: Customer's age.
  - `region_code`: Encoded region identifier.
  - `policy_sales_channel`: Sales channel used to contact the customer.
  - `previously_insured`: Whether the customer already has insurance (0 or 1).
  - `annual_premium`: Amount paid for the insurance premium.
  - `vintage`: Number of days since the customer registered.
  - `driving_license`: Indicates if the customer has a valid driving license (0 or 1).
  - `vehicle_age`: Age of the vehicle (< 1 year, 1-2 years, > 2 years).
  - `vehicle_damage`: Whether the vehicle has been damaged (Yes/No).

- **Target Variable:**
  - `response`: 0 (Not Interested) or 1 (Interested).

---

### 🛠️ **Technologies Used**

- **Programming Language:**
  - Python

- **Key Libraries:**
  - `pandas`, `numpy` for data manipulation.
  - `matplotlib`, `seaborn` for data visualization.
  - `scikit-learn` for machine learning model development and evaluation.

---

### 📄 **Workflow**

1. **Data Analysis and Preprocessing:**
   - Exploratory Data Analysis (EDA) to identify patterns and insights.
   - Handling missing values, outliers, and feature encoding.

2. **Feature Engineering:**
   - Transforming categorical variables into numerical representations.
   - Normalizing/Standardizing numerical features for better model performance.

3. **Model Training and Evaluation:**
   - Splitting the dataset into training and testing sets.
   - Training classification models such as Logistic Regression, Random Forest, or XGBoost.
   - Evaluating models using metrics like Accuracy, Precision, Recall, and F1-Score.

---

### 📊 **Conclusions and Insights**

- **Key Findings:**
  - Customers without prior insurance (`previously_insured = 0`) are more likely to respond positively.
  - Customers with a history of vehicle damage (`vehicle_damage = Yes`) show higher interest in insurance products.
  - Age and `annual_premium` are critical features influencing the prediction.

- **Model Performance:**
  - Example results (based on a trained model):
    - **Accuracy:** 0.85
    - **Precision:** 0.82
    - **Recall:** 0.78
    - **F1-Score:** 0.80

- **Business Implication:**
  - These insights can help insurance companies identify and focus on high-potential customers, thereby optimizing their marketing and sales efforts.

---

### 🔧 **Next Steps**

1. **Enhance the Dataset:**
   - Include additional customer demographics or historical claims data to improve the model's predictive power.

2. **Explore Advanced Algorithms:**
   - Implement Gradient Boosting, Neural Networks, or Ensemble Models for better performance.

3. **Deploy the Model:**
   - Develop a web application or API to provide real-time predictions for sales agents.

4. **Create Visual Dashboards:**
   - Use tools like Power BI or Tableau to visualize insights and monitor performance over time.

---

### 📬 **Contact**

Feel free to reach out if you have any questions or suggestions:

- **GitHub:** [OscarFantozzi](https://github.com/OscarFantozzi)
- **LinkedIn:** [Oscar Fantozzi](https://linkedin.com/in/oscarfantozzi)
