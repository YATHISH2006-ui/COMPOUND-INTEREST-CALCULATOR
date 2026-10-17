# Finance Toolkit

A desktop finance utility built with Python and Tkinter. The application provides a compound-interest calculator, a bank FD rate comparison, a display of sample mutual-fund and government-savings rates, and a basic loan eligibility estimate.

## Features

- **Compound Interest Calculator** — estimates the balance and interest using annual compounding.
- **Bank FD Rate Comparison** — displays the bank rates stored in the source code.
- **Investment Information** — displays sample mutual-fund return figures and government savings scheme rates.
- **Loan Eligibility Checker** — estimates a maximum eligible amount using a simple income multiplier and compares loan rates by bank and loan purpose.

## Requirements

- Python 3.9 or later recommended
- Tkinter (usually included with standard Python installations)
- No third-party Python packages are required.

On some Linux distributions, Tkinter may need to be installed separately through the operating system's package manager.

## Run the application

1. Install Python from https://www.python.org/downloads/ if it is not already installed.
2. Download or clone this repository.
3. Open a terminal or command prompt in the project folder.
4. Run:

   ```bash
   python project.py
   ```

   If your system uses `python3` instead, run:

   ```bash
   python3 project.py
   ```

## Important note about financial data

The interest rates and return figures in this project are hard-coded example values. They may be outdated and are not live quotes or financial advice. Verify current rates with the relevant bank or official government source before making financial decisions. Mutual-fund returns are market-linked and are not guaranteed.

The loan eligibility result is a simplified estimate for demonstration only. Actual eligibility depends on lender-specific policies, credit history, obligations, income verification, and other factors.

## Project structure

```text
finance-toolkit/
├── project.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Built with

- Python
- Tkinter / ttk
