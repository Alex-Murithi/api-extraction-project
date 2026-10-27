# API Data Extraction and Transformation

## Overview

This project retrieves customer records from the JSONPlaceholder Users API, flattens the nested JSON structure, transforms the data into a clean tabular format, and exports it as a CSV file for analytics use.

API Used
https://jsonplaceholder.typicode.com/users

## Features

- REST API data extraction with `requests`
- Response validation and error handling
- JSON structure analysis
- List, tuple, and dictionary construction using Python comprehensions
- Recursive JSON flattening
- Data transformation with Pandas
- Clean CSV export
- Robust handling of network and HTTP failures

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