# Reddit Data Pipeline Engineering
 
Welcome to the **Reddit Data Pipeline Engineering** project! This repository contains a comprehensive solution for extracting, transforming, and loading (ETL) Reddit data into an Amazon Redshift data warehouse. The pipeline leverages a powerful combination of tools and services, including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.
 
## Table of Contents
 
- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [System Setup](#system-setup)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configure the System](#configure-the-system)
  - [Starting the Containers](#starting-the-containers)
  - [Launch Airflow Web UI](#launch-airflow-web-ui)
- [Acknowledgments](#acknowledgements)

 
## Overview
 
This project demonstrates a robust ETL pipeline designed to:
 
- **Extract** data from Reddit using its official API.
- **Store** the raw data in an S3 bucket, orchestrated by Apache Airflow.
- **Transform** the data using AWS Glue and Amazon Athena for clean and structured output.
- **Load** the transformed data into Amazon Redshift, enabling advanced analytics and querying.
 
By using modern data engineering tools and AWS services, this pipeline ensures scalable, reliable, and efficient data processing, making it an excellent template for similar ETL workflows.
 
## Architecture
 
![Architecture Diagram](./RedditDataEngineering.png)
 
- **Reddit API**: The source of raw data, providing access to Reddit posts and comments.
- **Apache Airflow & Celery**: Handles task orchestration and distribution, ensuring smooth ETL operation.
- **PostgreSQL**: Temporary storage for raw data and metadata management.
- **Amazon S3**: Storage for raw and intermediate data.
- **AWS Glue**: Facilitates data cataloging and ETL jobs, automating transformations.
- **Amazon Athena**: Enables SQL-based data transformation directly on S3-stored data.
- **Amazon Redshift**: Final destination for the transformed data, ready for deep analytics.
 
## Prerequisites
 
Before you begin, ensure you have the following:
 
- An AWS account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials for accessing data.
- Docker installed on your machine.
- Python 3.11 or higher.
 
## System Setup
 
Follow these steps to set up the system:
 
### Clone the Repository
 
Clone the project repository to your local machine:
 
```bash
git clone https://github.com/varunmj/Reddit_Data_Pipeline_Engineering.git
```
### Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python3 -m venv venv
```
### Activate the Virtual Environment
Activate the virtual environment to manage project dependencies:
 - On macOS/Linux:
```bash
source venv/bin/activate
```

- On Windows:
```bash
venv\Scripts\activate
```
 ### Install Dependencies
Install the required Python packages specified in the `requirements.txt` :

```bash
pip install -r requirements.txt
```

### Configure the System
Rename the example configuration file and update it with your Reddit API credentials and AWS Config Credentials and change it in the `config/config.conf`:

```bash
mv config/config.conf.example config/config.conf
```
Open the config/config.conf file and fill in the required fields with your specific details (Reddit API credentials, AWS settings, etc.).

### Starting the Containers
Start the Docker containers that are necessary for running the project:
```bash
docker-compose up -d
```
This command will start up all the required services, including Airflow, PostgreSQL, and any other dependencies specified in the docker-compose.yml file.

### Launch Airflow Web UI
Access the Airflow web UI to monitor and manage your data pipeline tasks:
 
```bash
open http://localhost:8080
```
Alternatively, open your web browser and navigate to http://localhost:8080.

## Acknowledgements
 
This project was inspired by and developed with guidance from the [CodeWithYu](https://www.youtube.com/@CodeWithYu) YouTube channel. A special thanks to Yu for the insightful tutorials that helped bring this project to life.
