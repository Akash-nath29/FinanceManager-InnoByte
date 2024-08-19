# Personal Finance Manager

A Python-based command-line application to help users manage their personal finances by tracking income, expenses, and generating financial reports.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Overview](#modules-overview)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Budget Management**: Set and track budgets for different categories.
- **Transaction Management**: Record income and expenses with date, category, and amount.
- **Reporting**: Generate financial reports to review spending habits.
- **User Management**: Supports multiple users, allowing personalized finance tracking for each.

## Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)
- Virtual environment (optional, but recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/finance-manager.git
cd finance-manager
```

### Step 2: Set Up the Virtual Environment
Create and activate a virtual environment:

For **Windows**:
```bash
python -m venv env
env\Scripts\activate
```

For **macOS/Linux**:
```bash
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
The project comes with a pre-configured SQLite database (`finance.db`). If you'd like to start with a fresh database, delete `finance.db` and run the application. The database will be automatically created.

## Usage

### Running the Application
Activate the virtual environment if not already active:

For **Windows**:
```bash
env\Scripts\activate
```

For **macOS/Linux**:
```bash
source env/bin/activate
```

Then run the application:

```bash
python -m finance.main
```

### User Manual

#### 1. **Adding a New User**
   - Run the application.
   - Follow the prompts to create a new user by providing a username.

#### 2. **Recording a Transaction**
   - Choose the "Add Transaction" option.
   - Enter details such as date, amount, and category.
   - Specify whether the transaction is an income or an expense.

#### 3. **Setting a Budget**
   - Select the "Set Budget" option.
   - Provide the category and the budget limit for that category.

#### 4. **Generating Reports**
   - Choose the "Generate Report" option.
   - View summaries of income, expenses, and budget usage.

#### 5. **Viewing User Information**
   - Select "View User Info" to display the current user's details and transaction history.

### Modules Overview

- **`budget.py`**: Handles budget-related operations such as setting, updating, and tracking budgets.
- **`database.py`**: Manages the SQLite database, including creating tables, and handling CRUD operations.
- **`report.py`**: Generates various financial reports based on user transactions and budgets.
- **`transaction.py`**: Manages income and expense transactions, including adding, deleting, and listing transactions.
- **`user.py`**: Manages user accounts, including creating new users and retrieving user information.

### Contributing
We welcome contributions to enhance the functionality of this project. If you find a bug or want to add a new feature, please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
