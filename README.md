# Tokyo Olympics Data Analysis


## Description
This project involves creating an ETL (Extract, Transform, Load) pipeline in Azure to analyze data from the 2021 Tokyo Olympics. The data, sourced from a [Kaggle Dataset](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)), is processed using Azure Data Factory, stored in Azure Data Lake Storage Gen2, transformed using Azure Databricks, and analyzed with SQL queries in Azure Synapse.

This project is done with the help of the [Azure End-To-End Data Engineering Project]([https://www.youtube.com/watch?v=IaA9YNlg5hM)

### Architecture
![Architecture Diagram](https://github.com/JKUOL/olympic_data_analytics/blob/main/schema/schema.png)

## Installation
To set up this project, you will need access to Azure services including Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, and Azure Synapse. Ensure you have the necessary permissions and configurations in place.

## Usage
Follow these steps to execute the ETL pipeline:
1. **Data Integration:** Use Azure Data Factory to integrate the data from Kaggle into the pipeline.
2. **Data Storage:** Store the raw data in Azure Data Lake Storage Gen2.
3. **Data Transformation:** Use the provided Databricks notebook to transform the raw data.
4. **Data Analysis:** Analyze the transformed data using SQL scripts in Azure Synapse.

## Features
- Data extraction from Kaggle.
- Data integration using Azure Data Factory.
- Data storage in Azure Data Lake Storage Gen2.
- Data transformation in Azure Databricks with PySpark.
- Data analysis using SQL in Azure Synapse.
