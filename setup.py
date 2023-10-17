from setuptools import setup, find_packages

setup(
    name="databricks-cli-tool",
    version="0.1",
    author="Xinyi Sheng",
    author_email="xs110@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks",
        "python-dotenv",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "databricks-query = main:run_query",
        ],
    },
)
