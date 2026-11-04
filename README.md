# API Data Extraction and Transformation

## Overview

This project implements a Python-based ETL pipeline that retrieves customer records from the JSONPlaceholder REST API, transforms nested JSON data into a flat tabular structure, and exports the cleaned records into a CSV file.

The project simulates a data integration scenario in which Duka Connect needs to obtain customer information from an external business partner for further analysis.

API Used
https://jsonplaceholder.typicode.com/users
Each record contains customer information, including personal details, address information, geographic coordinates and company details.

## Features

- REST API data extraction with `requests`
- Response validation and error handling
- JSON structure analysis
- List, tuple, and dictionary construction using Python comprehensions
- Recursive JSON flattening
- Data transformation with Pandas
- Clean CSV export
- Robust handling of network and HTTP failures


## Approach and Implementation

Step 1: Data Retrieval

Used the Requests library to send an HTTP GET request to the API endpoint. A timeout was included, and the HTTP response was checked before parsing the JSON body.

Step 2: JSON Structure Inspection

Inspected the top-level payload and individual records to understand the underlying Python data structures.

The response is a list containing dictionaries. Nested dictionaries include:

address

address.geo

company

The deepest nested fields are geographic coordinates inside the address object.

Step 3: Core Field Extraction

Extracted customer ID, name, email, city and company name.

Missing fields use "Unknown" as the default, while missing customer IDs remain None.

Step 4: Python Data Structures

Used a list comprehension to extract names, a loop to create ID-email tuples, and a dictionary comprehension to map customer IDs to cities.

Step 5: JSON Flattening

Implemented a reusable recursive function to transform nested dictionaries into single-level dictionaries.

Nested keys are joined using underscores. For example, address.geo.lat becomes address_geo_lat.

Step 6: DataFrame Transformation

Converted flattened records into a pandas DataFrame.

Renamed id to customer_id, standardized the company_catchPhrase column name, converted latitude and longitude to numeric values, and arranged columns according to the expected output structure.

Step 7: CSV Export

Exported the DataFrame to output/customers_clean.csv using index=False.

The output directory is created automatically if it does not exist. Running the script again overwrites the existing CSV.

7. Assumptions

The API returns a list of user records.

Missing descriptive fields are represented as "Unknown".

Missing customer IDs are represented as None.

Geographic coordinates should be numeric.

The current recursive flattening implementation handles nested dictionaries; the source dataset does not require list flattening.

8. Error Handling and Testing

The pipeline is designed to handle:

Connection failures.

Request timeouts.

HTTP errors.

Invalid JSON responses.

Unexpected API response structures.

Failure tests should be conducted using simulated responses, including a timeout, a connection error, an HTTP 404 response and invalid JSON.

Each failure should produce a clear error message and terminate the application with a non-zero exit status.

Record the actual test results before submission.

## Output

Generated file:

```text
output/customers_clean.csv
```

The exported dataset contains:

- Customer details
- Address information
- Geographic coordinates
- Company information

_Default Assumptions_
Missing nested values are replaced with:
`Unknown`
This prevents KeyError exceptions.

## Error Handling

The script handles:

- Invalid URLs (connection errors)
- Request timeouts
- Non-200 HTTP responses
- Invalid JSON responses

Each scenario returns a clear error message and exits gracefully without displaying a Python traceback.

## Conclusion

This project demonstrates a complete data engineering workflow, from retrieving data from a REST API to transforming nested JSON into a clean, analytics-ready CSV dataset. By implementing data extraction, JSON flattening, data validation, error handling, and CSV exporting, the project highlights key Python skills used in real-world data pipelines and ETL processes.s