hi
# OpenAQDataPlatform
ETL Data Processing and Models for getting real time AirQualityData. 

The data is fairly pulled from OpenAQ under fair use. Right now only have support for OpenAQ source. I am working on adding more source soon. 

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


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher
- PostgreSQL database
- Virtual environment (recommended)
- Docker Desktop (Required)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/air-quality-data-platform.git
Navigate to the project directory:


cd air-quality-data-platform

2. Make sure you have docker up and running and run 

    ```bash
    docker compose up --build
and you'll be set.

Navigate to : http://localhost:8080 to find airflow UI.

3. **Note due to some minor issues in compose.yml file the airflow scheduler command doesn't run so you'd have to go to docker terminal for airflow and manually run by executing below command to see tasks and dags in the pipeline.**
      
      ```bash
      airflow scheduler 
**While you are at it also run below command in the airflow image**

      ```bash 
      python -m pip install -r requirements.txt
### Run test cases 

3. To see if the repositories and UOW are working as expected in case you have made any changes in any of them run :
      ```bash
      pytest
in the root directory.



# Project To-Do List

This is the To-Do list for the ongoing project. Items will be checked off as they are completed.

# Priority Tasks 

- [ ] Integrate fast api and make retrieval api for the frontend.
- [ ] Improve typing.
- [ ] Setup migrations with Alembic.
- [ ] Fix the airflow scheduler command in docker-compose.yml file.
- [ ] Fix the installation of requirements.txt in the airflow image.
- [ ] Refactor UOW to commit into the session ( Right now the 
      repository directly commits into the session honestly it's due to me not knowing how to extend an abstract UOW class it's a priority).
  [ ] Latitude and longitude needs type casting into appropriate format (Float
      should be BigInt or other appropriate type)
  [ ] Use local path Dependency for the model scripts from requirements.txt saving
      resource to save docker resources.



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
- [ ] Implement Cache In Database (Potentially Redis) 

# Future Works:

- **Data Analysis:** Perform data analysis and generate insights about air quality trends and patterns.

- **Data Visualization:** Visualize air quality data using interactive charts and maps.

- **User Management:** Manage user accounts and permissions for data access.
