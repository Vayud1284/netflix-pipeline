# 🎬 Netflix Data Pipeline Project

This project demonstrates a full end-to-end data engineering pipeline built using Python. It processes Netflix content data (movies and TV shows), performs cleaning, transformation, exploration, and stores the result in Parquet format for analysis or ML.

## 📊 Pipeline Overview

-> ✅ Features:

- Ingest CSV data from the Kaggle Netflix dataset
- Clean and standardize missing values, strings, and dates
- Transform features like `duration_num`, `main_country`, and `year_added`
- Run EDA with plots using matplotlib/seaborn
- Save final cleaned data to Parquet format
- Unit testing for core pipeline functions
- Logging and monitoring with email alerts

## 🚀 How to Run the Project

1.  Clone the Repo

git clone https://github.com/yourusername/netflix_pipeline.git
cd netflix_pipeline

2. Install Dependencies

pip install -r requirements.txt

3. Prepare Environment Variables

Set up a .env file or export these:
ALERT_EMAIL_FROM=your_email@gmail.com
ALERT_EMAIL_TO=receiver_email@gmail.com
ALERT_EMAIL_PASSWORD=your_app_password

4. Run the Pipeline

python main.py

## 🧪Run Unit Tests

python -m unittest discover tests

## 📅Schedule the Pipeline

Local: Use Task Scheduler (.bat file)

Cloud: Use Airflow or AWS Lambda (optional)

## 📌Dataset

Netflix Movies and TV Shows Dataset

Source: Kaggle - Netflix Titles

## 📬Email Notifications

Get notified on pipeline success or failure using Gmail SMTP.

## 👨‍💻Author

Vayud Pandey

LinkedIn: https://www.linkedin.com/in/vayud-pandey/

GitHub: https://github.com/Vayud1284
