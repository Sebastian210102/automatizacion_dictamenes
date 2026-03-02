#  Automated PDF & Excel Data Extraction System

## Overview

This project automates the extraction and consolidation of structured data from:

- `CONSTANCIA_SITUACION_FISCAL.pdf`
- `FOR_18.xlsx`
- `EXCEL_FINAL.xlsx`

The system processes these files and generates a structured output directory based on the detected company information.

The goal of this project is to eliminate manual data transfer, reduce human error, and improve operational efficiency.

---

##  Features

- Automated PDF data extraction
- Excel data parsing and transformation
- Dynamic folder generation based on company name
- Structured output directory
- Error validation for missing or incorrectly named files
- Modular and scalable architecture

---


---

## ⚙️ Requirements

- Python 3.10+
- Git

---

## 🔧 Installation (Local Environment)

### Clone the repository

```bash
git clone url_this_repository
cd automatizacion_dictamenes
```
### Create virtual environment 
python3 -m venv venv
source venv/bin/activate

```bash
pip install -r requirements.txt
```

▶️ Usage

Place the required files inside the input/ folder with the exact names:

CONSTANCIA_SITUACION_FISCAL.pdf
FOR_18.xlsx
EXCEL_FINAL.xlsx

Run the application:

````bash 
python main.py
````

Output will be generated in:

output/empresa/<company_name>/
