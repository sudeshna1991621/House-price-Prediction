
# 🏠 House Price Prediction - Bangalore

This project builds a robust machine learning pipeline to predict house prices in Bangalore, India, using a clean and well-engineered dataset. The model is deployed via a Streamlit web application.

## 📁 Dataset

The dataset contains 13,320 entries with attributes like:
- Location
- Size (BHK)
- Total Square Feet
- Number of Bathrooms and Balconies
- Price

## 🛠️ Data Preprocessing

- Dropped less relevant columns: `area_type`, `availability`, `society`, `balcony`
- Imputed missing values in `location` with 'Whitefield' and `size` with '2 BHK'
- Extracted BHK from `size`
- Converted `total_sqft` ranges (e.g., "1200 - 1500") to numeric averages
- Created `price_per_sqft` feature
- Grouped rare locations (<=10 entries) into 'Other'

## 🚧 Outlier Removal

- Removed unrealistic data: `total_sqft` per BHK must be ≥ 300
- Location-wise outlier removal based on price_per_sqft statistics
- BHK-level outlier filtering

## 📊 Modeling

- One-Hot Encoding applied to `location`
- Models used:
  - Linear Regression
  - Lasso Regression
  - ✅ Ridge Regression (Best R² Score: **0.87**)
- Final model saved as `house_price_model.pkl`

## 🌐 Deployment

- Built with Streamlit and deployed on Render
- 🔗 [Live App](https://house-price-prediction-hwit.onrender.com)

## 📦 Files in Repository

- `Cleaned Data.csv` – Cleaned and processed dataset
- `RidgeModel.pkl` – Trained Ridge Regression model
- `app.py` – Streamlit application script
- `requirements.txt` – Required Python packages

## 👩‍💻 Author

**Sudeshna Kundu Mondal**  
📧 Feel free to reach out for collaboration or feedback!

---
