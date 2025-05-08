# Apartment Web Scraping Bot

## Project Title and Elevator Pitch
This Python bot automates the process of scraping apartment listings from websites. While initially designed for apartment hunting, its adaptable code can be modified to extract data from various types of websites.

## Problem Statement/Motivation
Finding suitable apartments online often involves manually browsing numerous websites and filtering through countless listings. This process can be time-consuming and inefficient. This bot aims to streamline this process by automatically collecting and filtering apartment data based on user-defined criteria, such as budget. Furthermore, the underlying web scraping logic can be applied to extract information from other websites, making it a versatile tool for data collection.

## Features Implemented
* **Web Scraping:** Automatically fetches and parses HTML content from specified URLs.
* **Data Extraction:** Extracts key information such as apartment URLs, building names, areas, and prices.
* **Budget Filtering:** Allows users to filter apartment listings based on a maximum budget.
* **Error Handling:** Implements basic error handling to gracefully manage issues during data extraction.
* **Output:** Prints both all found apartment URLs and the filtered apartments meeting the budget criteria.
* **Optional Saving:** Provides an option to save all scraped apartment URLs to a text file (`apartment_urls.txt`).

## Technologies Used
* **Python:** The primary programming language used for the bot.
* **Requests:** A Python library for sending HTTP requests to web servers.
* **Beautiful Soup (bs4):** A Python library for parsing HTML and XML documents.
* **urllib.parse:** A Python module for working with URLs, used here for joining relative URLs.

## Setup and Installation Instructions
1.  **Prerequisites:** Ensure you have Python 3 installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Install Libraries:** Open your terminal or command prompt and install the necessary libraries using pip:
    ```bash
    pip install requests beautifulsoup4
    ```
3.  **Download the Code:** Save the provided Python code as a `.py` file (e.g., `apartment_scraper.py`).

## Usage/Examples
1.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the Python file, and run it using:
    ```bash
    python apartment_scraper.py
    ```
2.  **Modify the Target URL:** To scrape a different website, change the `url` variable at the beginning of the script to the desired URL.
3.  **Adjust the Budget:** To filter apartments based on a different budget, modify the `budget` argument in the `get_apartments()` function call:
    ```python
    get_apartments(url, budget=3500) # Example: Filtering for apartments under $3500
    ```
4.  **Adapt for Other Websites:** To use this script for scraping other types of websites, you will need to inspect the HTML structure of the target website and modify the CSS selectors used in the `find_all()` and `find()` methods within the `get_apartments()` function to target the relevant data elements.

## Live Demo Link
N/A - This is a command-line tool and does not have a live web demo.

## Challenges & Learnings
One potential challenge encountered during development might involve changes to the target website's HTML structure. Websites are often updated, which can break the CSS selectors used for data extraction. Learning to inspect website elements and adapt the scraping logic to these changes is a crucial skill in web scraping. Additionally, understanding and respecting website terms of service and implementing responsible scraping practices (e.g., adding delays between requests) is important to avoid overloading servers.
