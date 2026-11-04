"""
Day 1 - API Data Extraction and Transformation
Squad Python Specialization - Data Engineering
"""

from pathlib import Path # 	Manages file and folder paths
import sys # Allows the program to exit with an error status

import pandas as pd #Structures and exports the data
import requests # Communicates with the external REST API

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_PATH = Path("output") / "customers_clean.csv"


def fetch_users(url=API_URL, timeout=10.0):

    try:
        response = requests.get(url, timeout=timeout)

        response.raise_for_status()

        payload = response.json()

        if not isinstance(payload, list):
            raise ValueError("Expected a list of users")

        return payload

    except requests.exceptions.Timeout as e:
        raise RuntimeError("API request timed out") from e

    except requests.exceptions.ConnectionError as e:
        raise RuntimeError("Could not connect to API") from e

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"API returned HTTP error: {e}"
        ) from e

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"API request failed: {e}"
        ) from e

    except ValueError as e:
        raise RuntimeError(
            f"Invalid API response: {e}"
        ) from e


def describe_structure(payload) -> None:
    """
    Print payload structure and nested field types.
    """

    print(f"Top-level payload type: {type(payload).__name__}")

    if not payload:
        return

    first_record = payload[0]

    print(f"Record type: {type(first_record).__name__}")

    for key, value in first_record.items():
        print(f"{key}: {type(value).__name__}")

        if isinstance(value, dict):
            for nested_key, nested_value in value.items():
                print(
                    f"  {key}.{nested_key}: {type(nested_value).__name__}"
                )

                if isinstance(nested_value, dict):
                    for deep_key, deep_value in nested_value.items():
                        print(
                            f"    {key}.{nested_key}.{deep_key}: "
                            f"{type(deep_value).__name__}"
                        )


def extract_core_fields(users: list[dict]) -> list[dict]:
    """
    Extract only the required fields.
    Missing values default to 'Unknown'.
    """

    records = []

    for user in users:
        records.append(
            {
                "id": user.get("id"),
                "name": user.get("name", "Unknown"),
                "email": user.get("email", "Unknown"),
                "city": user.get("address", {}).get( "city","Unknown"),
                "company": user.get("company", {}).get("name","Unknown"),
            }
        )

    return records


def build_structures(users: list[dict]) -> tuple[list, list[tuple], dict]:
    """
    Build structures using comprehensions and loops.
    """

    # List comprehension
    names = [user.get("name") for user in users] # This creates a list containing the names of all users.

    # Plain for-loop
    id_email_pairs = [] # This initializes an empty list to store tuples of user IDs and emails.

    for user in users:
        id_email_pairs.append(
            (
                user.get("id"),
                user.get("email")
            )
        )

    # Dict comprehension
    id_to_city = {
        user.get("id"): user.get("address", {}).get("city", "Unknown")
        for user in users
    }

    return names, id_email_pairs, id_to_city


def flatten_user(user: dict, parent_key: str = "", sep: str = "_") -> dict:
    """
    Recursively flatten nested dictionaries.
    """

    items = {}

    for key, value in user.items():

        new_key = (
            f"{parent_key}{sep}{key}"
            if parent_key
            else key
        )

        if isinstance(value, dict): # This checks whether the current value is a dictionary, recursively flatten it
            items.update(
                flatten_user(value, new_key, sep)
            )
        else:
            items[new_key] = value

    return items


def to_dataframe(flat_users: list[dict]) -> pd.DataFrame:
    """
    Convert flattened records to ordered DataFrame.
    """

    df = pd.DataFrame(flat_users)

    df = df.rename(
        columns={
            "id": "customer_id",
            "company_catchPhrase": "company_catchphrase",
        }
    )

    df["address_geo_lat"] = pd.to_numeric(
        df["address_geo_lat"],
        errors="coerce" # if pandas encounters a value it cannot convert, it replaces it with NaN rather than crashing.
    )

    df["address_geo_lng"] = pd.to_numeric(
        df["address_geo_lng"],
        errors="coerce"
    )

    column_order = [
        "customer_id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "address_street",
        "address_suite",
        "address_city",
        "address_zipcode",
        "address_geo_lat",
        "address_geo_lng",
        "company_name",
        "company_catchphrase",
        "company_bs",
    ] # This defines the desired order of columns in the final DataFrame.

    df = df[column_order]

    print("\nDataFrame Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    return df


def export_csv(
    df: pd.DataFrame,
    path: Path = OUTPUT_PATH
) -> Path:
    """
    Export CSV without index.
    """

    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

    return path


def main():
    try:
        print("\n=== FETCHING CUSTOMER DATA ===")
        users = fetch_users()

        print(f"Successfully retrieved {len(users)} users.")

        print("\n=== STRUCTURE ANALYSIS ===")
        describe_structure(users)

        print("\n=== CORE FIELD EXTRACTION ===")
        core_records = extract_core_fields(users)

        for record in core_records[:2]:
            print(record)

        print("\n=== BUILDING PYTHON DATA STRUCTURES ===")
        names, email_pairs, city_map = build_structures(users)

        print(f"Names count: {len(names)}")
        print(f"Email pairs count: {len(email_pairs)}")
        print(f"City mappings count: {len(city_map)}")

        print("\n=== FLATTENING JSON ===")
        flat_users = [
            flatten_user(user)
            for user in users
        ]

        print(f"Flattened records: {len(flat_users)}")

        print("\n=== DATAFRAME TRANSFORMATION ===")
        df = to_dataframe(flat_users)

        print("\n=== CSV EXPORT ===")
        output_file = export_csv(df)

        print(f"CSV successfully exported to: {output_file}")

        print("\n=== PIPELINE SUMMARY ===")
        print(f"Total customers processed: {len(df)}")
        print(f"Total columns: {len(df.columns)}")
        print("Pipeline completed successfully.")

    except (RuntimeError, ValueError, OSError) as e:
        print(f"\nPipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()