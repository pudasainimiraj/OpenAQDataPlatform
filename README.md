# OpenAQDataPlatform
Data Platform For Open Air Quality Data

# Air Quality Data Platform


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Air Quality Data Platform is a system designed to manage and analyze air quality data. It provides a set of tools and services for collecting, storing, and analyzing air quality measurements from various sources. Whether you are a researcher, environmentalist, or developer, this platform aims to make air quality data more accessible and actionable.

## Features

- **Data Collection:** Collect air quality data from various sources, including sensors, weather stations, and government agencies.

- **Data Storage:** Store collected data in a reliable and scalable database system.

- **Data Analysis:** Perform data analysis and generate insights about air quality trends and patterns.

- **Data Visualization:** Visualize air quality data using interactive charts and maps.

- **User Management:** Manage user accounts and permissions for data access.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher
- PostgreSQL database
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/air-quality-data-platform.git
Navigate to the project directory:


cd air-quality-data-platform
Create a virtual environment (optional but recommended):


python -m venv venv
Activate the virtual environment:


source venv/bin/activate  # On Windows: venv\Scripts\activate
Install project dependencies:


pip install -r requirements.txt
Usage
To run the Air Quality Data Platform, follow these steps:

Configure your database connection in the .env file.

Initialize the database:


python manage.py migrate
Start the development server:

python manage.py runserver
Access the platform in your web browser at http://localhost:8000.

Testing
To run tests for the project, use the following command:

pytest


# Project To-Do List

This is the To-Do list for the ongoing project. Items will be checked off as they are completed.

# Priority Tasks 

- [ ] Integrate fast api and make retrieval api for the frontend.


## Documentation

- [ ] Write initial project documentation
- [ ] Document the API endpoints
- [ ] Create user guides

## Deployment

- [ ] Configure the production environment
- [ ] Set up continuous integration/continuous deployment (CI/CD)
- [ ] Ensure security best practices
- [ ] Figure out the directory structure inside docker right now the OpenAQLibrary is scattered all over the place with 3 copies

## Testing

- [ ] Conduct unit testing for airflow and cqrs
- [ ] Perform integration testing for airflow
- [ ] Execute end-to-end testing

## Miscellaneous

- [ ] Review code for potential refactoring
- [ ] Refactor the dag and task to make it more readable 
- [ ] Refactor the messy transformation 
