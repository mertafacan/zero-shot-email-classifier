# Email Content Classifier (Zero-Shot)

## Overview

The **Email Content Classifier** is a Streamlit app that automatically classifies email contents into categories like **Priority**, **Updates**, **Promotions**, etc., using Zero-Shot Classification with Hugging Face's `facebook/bart-large-mnli` model.


## Features

- **Flexible CSV Upload:** Upload CSV files with different delimiters (comma, semicolon, tab, etc.).
- **Customizable Classification:** Define your own labels (e.g., "Priority", "Updates") and set a confidence threshold.
- **Download Results:** View and download the classified emails in CSV format.

## How to Use

1. **Upload CSV:** Upload your CSV file containing email content.
2. **Set Labels & Threshold:** Define candidate labels and the confidence threshold.
3. **Classify:** Click **Classify** to categorize emails.
4. **Download:** Download the classified results as a CSV file.

## Demo
### Interface for Uploading CSV File
<img src="https://github.com/user-attachments/assets/e69295e0-ead3-4d14-9088-ddd6e258a825" width="750"/>

### Classified Email Results
<img src="https://github.com/user-attachments/assets/374d8100-6a1d-40f2-b0a4-e46147d042ab" width="750"/>
