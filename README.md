# Scraping-Book-Website

# Web Scraping Books Project

This project scrapes book data from [Books to Scrape](https://books.toscrape.com/), a website designed for web scraping practice. The scraper extracts information such as the title, link, price, and stock status of books from multiple pages and saves the data in Excel and CSV formats.

## Features

- Scrapes book details including title, link, price, and stock status.
- Supports pagination up to the last available page.
- Saves the extracted data into `books.xlsx` and `books.csv` files.

## Installation

To run this project, you need to have Python installed along with the required libraries. 

### Dependencies

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl` (for saving Excel files)

You can install these dependencies using `pip`:

```bash
pip install requests   
pip install beautifulsoup4
pip install pandas
pip install openpyxl 
