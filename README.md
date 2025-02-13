E-Commerce ETL Pipeline with Python, PostgreSQL, and Power BI
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for processing and analyzing e-commerce data. The pipeline extracts data from a CSV file, cleans and transforms it using Python, loads it into a PostgreSQL database, and visualizes the insights using Power BI.

This project focuses on building an automated ETL pipeline for an e-commerce dataset. The pipeline:
Extracts raw data from a CSV file.
Cleans and transforms the data to handle missing values, inconsistencies, and unnecessary columns.
Loads the processed data into a PostgreSQL database.
Visualizes key insights using Power BI dashboards.
Dataset
The dataset used in this project is Pakistan's Largest E-Commerce Dataset. You can access the dataset from the following Google Drive link:
📁 Download Dataset from Google Drive
https://drive.google.com/drive/folders/1IFYqniDHTRYS3R34sx4at7JcEAS58WtI?usp=sharing
System requirement
Before setting up and running this ETL pipeline, ensure the following prerequisites are met:
1. Software Requirements
Python 3.17-for data extraction, transformation, and loading.
PostgreSQL -for storing the cleaned data.
Power BI -for data visualization.
VS Code with jupyter extension.
2. Python Libraries
Ensure you have the following libraries installed:
pandas for data cleaning and transformation
sqlalchemy for connecting to PostgreSQL
psycopg2  for interacting with the PostgreSQL database
3. Database Setup
PostgreSQL must be installed and running.
A database named EcommerceDataset should be created in PostgreSQL.
4. CSV Dataset
The raw e-commerce dataset should be available as Pakistan Largest Ecommerce Dataset.csv.click here to see the sourse of data set Pakistan's Largest E-Commerce Dataset
The cleaned dataset will be stored as cleaned.csv before loading into PostgreSQL.
5. Hardware Requirements
Processor: Intel Core i5 or higher (or AMD equivalent)
RAM: Minimum 8 GB (16 GB recommended for large datasets)
Storage: At least 10 GB of free space for dataset storage and database files
Operating System: Windows 10/11, macOS, or Linux
Setup Instructions
1.Clone this repository:
git clone https://github.com/jo122313/Big-data-analytics-and-Business-intelligence
2.Navigate to the project directory:
cd Big-data-analytics-and-Business-intelligence
3.Download the dataset from the Google Drive link and place it in the Data/ folder.
4.Install the required Python libraries:
pip install -r requirements.txt
4.Run the ETL pipeline scripts in the following order:
 extract.py
 transform.py
 load.py
Power BI Dashboard
To visualize the data:
  1.Connect Power BI to the PostgreSQL database.
  2.Import the necessary tables.
  3.Create dashboards to analyze key metrics such as:
     Sales trends over time.
     Customer segmentation.
     Product performance.

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
  1.Fork the repository.
  2.Create a new branch for your feature or bug fix.
  3.Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
