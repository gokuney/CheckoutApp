# Checkout App

A simple cart checkout application

## File Structure

    .
    ├── docs/               # Contains the code documentation
    ├── main.py             # Main application file that is used to run the demo
    ├── README.md           # This Readme file for the project
    ├── checkoutApp.py      # The core logic file for the application
    ├── setup.py            # Application installer and manager
    ├── tests/              # Contains all the unit test cases
    └── utils/              # Contains commonly used utilities in the project

## Requirements

- Python 3.10+
- Python venv module (recommended)

## Run Locally

Note: Instructions are mainly for Linux like systems but might work with other OS as well with little tweaks (not tested)

Clone the project

```bash
  git clone git@github.com:gokuney/CheckoutApp.git
```

or

```bash
  git clone https://github.com/gokuney/CheckoutApp.git
```

Go to the project directory

```bash
  cd CheckoutApp
```

Create virtual environment(recommended)

```bash
  python3 -m venv .env
```

Activate the virtual environment

```bash
  source .env/bin/activate
```

Install the dependencies

```bash
  python setup.py install
```

Now, run the application

```bash
  python main.py
```

## Test Cases

The test cases are kept in the `tests` directory. To run the unit test cases(within virtual environment):

```bash
    python -m pytest --verbose
```
