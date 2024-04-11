<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">.</h1>
</p>
<p align="center">
    <em>Flask your way to finance app magic!</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=default&logo=Flask&logoColor=white" alt="Flask">
</p>

<br><!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

## Overview

The personal finance manager system project provides a user-friendly interface for managing finances. Its Flask-based API greets users at the root URL, facilitates logging configurations, and handles database operations for various financial data entities such as accounts, transactions, categories, budgets, and savings goals. With a focus on simplicity and robust functionality, this open-source project empowers individuals to efficiently track and manage their financial resources.

---

## Repository Structure

```sh
└── ./
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── config.py
    │   ├── database.py
    │   ├── routes.py
    │   ├── service.py
    │   └── services
    ├── data
    │   ├── mock_accounts_data.csv
    │   ├── mock_budgets_data.csv
    │   ├── mock_categories_data.csv
    │   ├── mock_savings_goals_data.csv
    │   ├── mock_transactions_data.csv
    │   ├── mock_users_data.csv
    └── run.py
```

---

## Modules

<details closed><summary>.</summary>

| File               | Summary                                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [run.py](run.py)   | Exposes a simple API endpoint for the Flask application to greet users with Hello, World! when accessing the root URL path. Runs the Flask app on host 0.0.0.0 and port 8000 for web server functionality. |
| [Pipfile](Pipfile) | Define dependencies for Flask, python-dotenv, and readmeai while specifying Python versions in the Pipfile of the personal finance manager system repository.                                              |

</details>

<details closed><summary>app</summary>

| File                           | Summary                                                                                                                                                                                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [config.py](app/config.py)     | Loads configurations and configures logging settings for the app. Manages environment variables for access tokens, phone numbers, app IDs, and secrets. Sets up logging format and output level.                                                     |
| [database.py](app/database.py) | Establish database connections, create tables, and manage table operations. Handles table creation, table dropping, and table maintenance for user, account, transaction, category, budget, and savings goal data in a personal finance application. |

</details>

---

## Getting Started

**System Requirements:**

- **Python**: `version 3.9`

### Installation

<h4>From <code>source</code></h4>

> 1. Clone the . repository:
>
> ```console
> $ git clone ../.
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd .
> ```
>
> 3. Install the dependencies:
>
> ```console
> $ pipenv install
> ```

### Usage

<h4>From <code>source</code></h4>

> Run . using the command below:
>
> ```console
> $ python run.py
> ```
