API Data Extraction and Transformation
Objective
Retrieve customer data from a REST API, flatten nested JSON structures and export a clean CSV for analytics.

API Used
https://jsonplaceholder.typicode.com/users

Features
Fetch data from REST API using requests
Validate HTTP status codes
Handle connection and timeout failures
Inspect JSON structure
Extract core customer fields
Demonstrate:
Lists
Tuples
Dictionaries
List comprehensions
Dict comprehensions
Flatten nested JSON recursively
Load data into pandas DataFrame
Export cleaned CSV
Nested Structure Observed
address (dict)

geo (dict)
lat
lng
company (dict)

name
catchPhrase
bs
Maximum nesting depth: 3 levels.

Default Assumptions
Missing nested values are replaced with:

Unknown

This prevents KeyError exceptions.

Failure Testing
Invalid URL
fetch_users("https://wrong-url.com")