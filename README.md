Here's the updated README with the correct file naming format:

---

# Autocomplete API Name Extractor

This Python script is designed to interact with an autocomplete API to extract a comprehensive list of unique names. It queries the API using all alphanumeric characters (a-z and 0-9) as search terms, collects the results, and saves them to a file. The goal is to gather as many unique names as possible in an efficient and organized manner.

## How It Works

### 1. API Interaction
The script interacts with an autocomplete API located at `http://35.200.185.69:8000/v3/autocomplete`. It sends queries to this API and retrieves a list of names that match the query.

### 2. Querying the API
The script iterates through all lowercase letters (`a-z`) and digits (`0-9`) to use as search queries. For example:
- Querying with `a` might return names like *Alice*, *Alex*, etc.
- Querying with `1` might return names like *1stStreet*, *100Days*, etc.

### 3. Storing Unique Names
All names retrieved from the API are stored in a Python set, which ensures that only unique names are kept. This avoids duplicates and makes the final list clean and concise.

### 4. Saving Results
Once all queries are completed, the script saves the collected names to a file named `extracted_names_{version}.txt`, where `{version}` represents a versioning system (e.g., `v1`, `v2`). The names are sorted alphabetically for easy readability.

### 5. Optional Delay
The script includes an optional delay (`DELAY`) between requests to avoid overwhelming the server. This is currently commented out but can be enabled if needed.

## Code Structure

### Key Components

- **`BASE_URL`**: The base URL of the autocomplete API.
- **`DELAY`**: A delay (in seconds) between API requests to prevent overloading the server.
- **`all_names`**: A Python set that stores all unique names fetched from the API.
- **`fetch_names(query)`**: A function that sends a query to the API and adds the results to `all_names`.
- **`extract_all_names()`**: The main function that iterates through all alphanumeric characters, fetches names, and saves them to a file.

### Workflow

1. The script starts by defining the API URL and initializing an empty set (`all_names`) to store results.
2. It loops through each character in the alphanumeric set (`a-z`, `0-9`).
3. For each character, it calls the `fetch_names()` function to query the API and retrieve matching names.
4. The names are added to the `all_names` set, ensuring uniqueness.
5. After all queries are completed, the script saves the sorted list of names to `extracted_names_{version}.txt`.
6. Finally, it prints the total number of unique names extracted.

## How to Use

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Requests Library**: Install the requests library if not already installed. You can install it using pip:

    ```bash
    pip install requests
    ```

### Running the Script

1. Save the script to a file, e.g., `extract_names.py`.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script using Python:

    ```bash
    python extract_names.py
    ```

### What the Script Will Do:
- Fetch names from the API.
- Save the unique names to `extracted_names_{version}.txt`.
- Print the total number of unique names extracted.

### Output
- **`extracted_names_{version}.txt`**: A text file containing all unique names, sorted alphabetically.
- **Terminal Output**: The total number of unique names extracted, e.g., `Total unique names extracted: 1234`.

## Customization

### 1. Change the API URL
If the API URL changes, update the `BASE_URL` variable at the top of the script:

```python
BASE_URL = "http://new-api-url.com/v3/autocomplete"
```

### 2. Enable Delay Between Requests
To avoid overwhelming the server, uncomment the `time.sleep(DELAY)` line in the `extract_all_names()` function:

```python
time.sleep(DELAY)
```

### 3. Modify the Query Characters
If you want to query additional characters (e.g., uppercase letters or special characters), update the `characters` string in the `extract_all_names()` function:

```python
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
```

### 4. Change the Output File
To save the results to a different file, modify the `open()` statement in the `extract_all_names()` function, ensuring that the version is dynamic:

```python
with open(f'extracted_names_{version}.txt', 'w') as file:
```

## Example Output

### `extracted_names_v1.txt` Example

```
Alice
Alex
Bob
Charlie
100Days
1stStreet
...
Zoe
```

### Terminal Output

```
Total unique names extracted: 1234
```
