
# Wallet API Service

This is a simple Wallet API built with Flask. It allows users to manage their wallets, including enabling/disabling wallets, viewing balance, making deposits and withdrawals, and more.

## Requirements

- Python 3.6+
- `pip` (Python package manager)

## Install the Required Packages

Install the necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Setting Up the Project

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Velocyes/mini-wallet.git
   cd mini-wallet
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify that you have Python 3.6 or higher installed:
   ```bash
   python --version
   ```

4. Set your Flask environment variables:
   - On Linux/MacOS:
     ```bash
     export FLASK_APP=main.py
     export FLASK_ENV=development
     ```
   - On Windows:
     ```bash
     set FLASK_APP=main.py
     set FLASK_ENV=development
     ```

## Running the Flask Application

Once the setup is complete, run the application using the following command:

```bash
flask run
```

This will start the Flask development server. You should see output similar to this:

```
 * Running on http://127.0.0.1:5000
```

You can access the API via http://127.0.0.1:5000
