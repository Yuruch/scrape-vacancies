# Job Experience Analysis Project

## Overview

This project analyzes job listings to visualize the distribution of experience levels and experience ranges across different job levels. The analysis includes extracting and processing experience data, and generating plots to help understand the distribution of job requirements.

This project also uses async for optimization
## Project Structure

├── data_analysis /  # dir for the data analysis

├── scrape /  # dir for the scraping

├── result_plots # Directory to save generated plots 

├── results # Directory to save scraped data


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yuruch/scrape-vacancies
    cd scrape-vacancies
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Data Processing
### `scrape/run.py`
This script scrapes data from dou site by following this steps
1. **Request:** Makes request to the dou site for each experience filter
2. **Scraping:** Scrapes the received pages to extract data
3. **Saving Data:** Saves data to csv file

### `data_analysis/run.py`
Analyses the retrieved data from scraping and makes plots by following this steps:
1. **Load Data:** Loads job listings from a CSV file.
2. **Process Data:** Cleans and processes the experience data.
3. **Generate Reports:** Calls plotting functions to visualize the experience distribution.

### `main.py`
This script just run the scraper and analyser
## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **View the results:**
    - Plots will be saved in the `result_plots` directory.
   

### You can also run scraper and analyser separately (analyser will not work without csv file)

1. **Run the scraper:**
    ```bash
    python scrape/run.py
    ```

2. **Run the analyser:**
    ```bash
    python data_analysis/run.py
    ```

## Config

The project also is relaying on the config file (config.py)

### If you want you can change it but this is not recommended!
### Quick intro to config.py:
1. **BASE_URL** the const for the base dou vacancies url (it can change in the future)
2. **BASE_DIR, RESULT_DIR, PLOT_DIR** just the dir paths consts
3. **CATEGORIES_URLS** the const for the categories
4. **TECHNOLOGIES** the const for the all possible technologies for Python developer

