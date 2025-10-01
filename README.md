#  Steel Strength Predictor

This project uses **machine learning** to predict the **Ultimate Tensile Strength (UTS)** of steel based on its chemical composition.  
The goal is to help engineers and material scientists quickly evaluate steel grades without relying solely on costly and time-consuming experiments.

---

##  Problem Statement
Steel’s mechanical properties, such as tensile strength and hardness, are critical for selecting the right material in engineering applications.  
These properties depend on the chemical composition of the alloy, but testing them experimentally can be costly and time-consuming.  

This project builds a machine learning model to predict **UTS (MPa)** directly from steel composition.

---

## Dataset
- Source: [Kaggle – Steel Composition & Mechanical Properties Dataset](https://www.kaggle.com)  
- Features include chemical composition (% of C, Mn, Si, Ni, Cr, Mo, Ti, etc.)  
- Target: **UTS (MPa)**  

---

##  Approach
1. **Data Cleaning & Preprocessing**  
   - Handled missing values  
   - Dropped duplicate rows  
   - Selected relevant features (composition values only)  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized feature distributions and correlations  
   - Identified most influential alloying elements  

3. **Modeling**  
   - Compared **Linear Regression**, **Random Forest**, and **XGBoost**  
   - Tuned XGBoost with `RandomizedSearchCV`  

4. **Interpretability**  
   - Used feature importance to explain which alloying elements influence tensile strength most  

---

## Results
| Model            | RMSE (↓) | R² (↑) |
|------------------|----------|--------|
| Linear Regression | ~243 MPa | 0.29   |
| Random Forest     | ~214 MPa | 0.46   |
| XGBoost (tuned)   | ~236 MPa | 0.34   |

- **Best model**: Random Forest (better R² than Linear Regression, comparable RMSE to tuned XGBoost)  
- **Top Features**: Carbon (C), Nickel (Ni), Chromium (Cr) were most influential for UTS  

---

##  Deployment
The model is deployed as a **Streamlit web app**:  
- Users can input steel composition values  
- The app predicts the **UTS (MPa)** instantly  


