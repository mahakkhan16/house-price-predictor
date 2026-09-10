# House-price-predictor

A machine learning project that predicts house sale prices based on property features like lot size, quality, and living area. Built end-to-end from raw data to a live, interactive web app.

🔗 **Live Demo:** [house-price-predictor-wictvf4xtyylrmban6wr3j.streamlit.app](https://house-price-predictor-wictvf4xtyylrmban6wr3j.streamlit.app)

## The Problem

Given details about a house (size, quality, year built, garage capacity, etc.), predict its sale price. This is a supervised regression problem.

## Dataset

[House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) from Kaggle — 1,460 houses with 81 features including lot area, neighborhood, year built, and overall quality.

## Data Cleaning

- Identified that most "missing" values weren't actually missing — features like `PoolQC`, `Fence`, and `GarageType` were blank because the house simply doesn't have that feature. Filled these with `"None"` instead of dropping them.
- Filled genuinely missing numeric values (`LotFrontage`) with the median, and the single missing `Electrical` value with the most common category.
- One-hot encoded all categorical columns, expanding the dataset from 81 to 302 features.
- Split data into 80% training / 20% testing.

## Models Trained & Compared

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | $21,108 | $65,390 | 0.44 |
| Decision Tree | $27,964 | $43,358 | 0.75 |
| **Random Forest** | **$17,619** | **$28,714** | **0.89** |

**Random Forest performed best across every metric** and was used for the final deployed model.

## What the Metrics Mean

- **MAE**: average dollar amount the prediction is off by
- **RMSE**: similar to MAE, but penalizes large errors more heavily
- **R²**: how much of the price variation the model explains (closer to 1.0 = better)

Interestingly, Linear Regression had a *lower* MAE than the Decision Tree but a much *higher* RMSE — meaning it was closer on typical houses but made a few very large errors on outliers, which the Decision Tree handled better.

##  Demo

Built with [Streamlit](https://streamlit.io). Enter details like lot area, overall quality, year built, living area, basement size, and garage capacity to get an instant predicted sale price.

##  Run It Locally

```bash
git clone https://github.com/mahakkhan16/house-price-predictor.git
cd house-price-predictor
pip install -r requirements.txt
streamlit run app.py
```

##  What I Learned

- How to properly diagnose missing data — distinguishing "genuinely missing" from "structurally absent" features, and why that distinction changes how you clean it.
- Why comparing multiple models (and multiple metrics) matters more than chasing a single accuracy number.
- How to take a trained model from a notebook all the way to a live, shareable web app.

## Tools Used

Python, Pandas, Scikit-learn, Streamlit, Google Colab, GitHub

---

*This project was built as a hands-on learning exercise in applied machine learning.*
