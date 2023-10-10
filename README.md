# Selenium BDD Automation for React Shopping Cart Demo

This Python project utilizes Selenium with a BDD (Behavior-Driven Development) framework to automate tests for the React Shopping Cart Demo website.

## Prerequisites

Before you can run the automated tests, you need to ensure the following prerequisites are met:

1. **Python:** Make sure you have Python installed on your system. 
2. **Selenium WebDriver:** Install Selenium WebDriver for Python using pip:

   ```bash
   pip install selenium

3. **Behave Framework:** Install Behave for Python using pip:

   ```bash
   pip install behave

## Installation

Follow these steps to initialize and execute the automated tests:

```bash
git clone git@github.com:mansi2000/SeleniumBDD.git
cd SeleniumBDD.git
python -m venv venv
source venv/bin/activate 
pip install selenium behave 
```


## Running Automated Tests

To run the automated tests, use the following command from the project root:

```bash
behave
```

Behave will execute the scenarios defined in the feature files, interact with the website, and provide test results.