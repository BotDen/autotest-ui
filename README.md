# Automation UI tests

This project implements automated tests for the website [automationexercise.com](https://automationexercise.com). The tests are written using 
**Playwright**, **Python**, **Pytest**, **Allure**, **Faker**, **Pydantic**. 

# Project overview

The goal of this project is to demonstrate my capabilities in automating UI tests. Three tests were written for the 
web application's core functionality: user registration, adding an item to the cart, and placing an order. 
The project is built on the page object framework.

I update the project as I learn new things.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/BotDen/autotest-ui.git
cd autotest-ui
```


### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Tests with Allure Report Generation

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.
