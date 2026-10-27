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

Failure Testing
Invalid URL
fetch_users("https://wrong-url.com")