# Zuber Data Analysis

This project analyzes ride-sharing and weather data for **Zuber**, a fictional ride-hailing company, to identify patterns in taxi demand, company performance, and the impact of weather conditions on rides.

## Project Objective

The goal of this project is to analyze ride data from Zuber and uncover insights about:

* Taxi company performance
* Neighborhood ride distribution
* Weather impact on ride frequency
* Passenger behavior patterns

These insights can help support data-driven business decisions in transportation services.

---

## Dataset Description

The project uses the following datasets:

* **company_trips.csv** → number of rides per taxi company
* **neighborhood_trips.csv** → average trips ending in each neighborhood
* **weather_records.csv** → weather conditions and trip information

The datasets were originally queried with SQL and then exported to CSV for analysis.

---

## Tools and Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **SQL** (for data extraction)

---

## Analysis Workflow

1. Data loading and inspection
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Data visualization
5. Business insights generation

---

## Key Analysis Questions

This project aims to answer questions such as:

* Which taxi companies complete the highest number of rides?
* Which neighborhoods have the highest ride demand?
* How does weather affect ride behavior?
* Are there noticeable patterns in ride distribution?

---

## Project Structure

```bash
Zuber_Data_Analysis/
│── data/
│   ├── company_trips.csv
│   ├── neighborhood_trips.csv
│   └── weather_records.csv
│── notebooks/
│   └── analysis.ipynb
│── requirements.txt
│── README.md
```

---

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Kevin-Higuera/Zuber_Data_Analysis.git
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook
```

---

## Results

The analysis reveals trends in taxi usage, neighborhood demand concentration, and weather-related ride behavior that can help optimize ride allocation strategies.

Further visualizations and conclusions are available in the Jupyter Notebook.

---

## Author

**Kevin Higuera**

Aspiring Data Analyst focused on Python, SQL, and data visualization projects.

