# Use the databricks-query from a python package

### 1. **Clone the Repository:**

```bash
git clone https://github.com/nogibjj/IDS-706-Python-Package-XS110.git
cd IDS-706-Python-Package-XS110
```

### 2. **Set Up Databricks Connection:**

Create a `.env` file in the project root and add your Databricks connection details:

```ini
DATABRICKS_HOST='adb-xxxx'
DATABRICKS_HTTP_PATH='/sql/xxx'
DATABRICKS_TOKEN='dapxxx'
```

### 3. **Install Dependencies:**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. **Set Up the Package:**

```bash
make setup_package
```

### 5. **Run the Databricks Query:**

```bash
make databricks-query
```

This will execute the query defined in `query.py` using the Databricks SQL Connector for Python. The result will be printed as a table.

### 6. **Understanding the Package Structure:**

- The package structure is defined in `setup.py`.
- The main script (`query.py`) contains the `run_query` function.
- The `databricks-query` command is defined in `setup.py` under `entry_points`.
- The `.yml` workflow file defines steps for installing the package and running the Databricks query.
