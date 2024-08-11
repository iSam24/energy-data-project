# Energy Data project

## Overview
The energy data project repo utilises multiple open-source UK energy apis and aggregates the data from these API to visualises real-time insights into the operation of the UK's energy grid. The aim of the project is to create a interactive web dashboard providing detailed analytics and, in the future, forecasting for the uk's grid. 

## Key Technologies
- **Python** Core language.
- **SQL**: For structured data storage, retrieval, and manipulation.
- **Linux Server**: Deployment of webpage and Cron task scheduler
### Possible Integrations
- **Spark**: Utilised for handling big data processing tasks.
- **Airflow**: For workflow automation and scheduling of data pipelines.

## UK Energy Dashboard Project
- **APIs**: 
  - *NGED API*: To retrieve energy distribution data.
  - *ELEXON API*: To access market data and energy prices.
- **Functionality**:
  - Regular updates to a SQL database with the latest energy pricing data.
  - Publishing this data to a real-time dashboard or webpage.
  
## How to Get Started
1. **Set up the environment**: Virtual environment and repo setup.
2. **Configure API Access**: Ensure API keys and tokens are securely stored and accessible by the project scripts.
3. **Run the initial scripts**: Start by running the data extraction scripts to populate the database with initial datasets.
