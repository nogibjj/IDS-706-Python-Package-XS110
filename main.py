from mylib.query import run_query


def main():
    try:
        run_query()
        return "Success"  # Return "success" if run_query() completes successfully
    except Exception as e:
        # Handle exceptions if run_query() encounters an error
        print(f"An error occurred: {str(e)}")
        return "error"
    

if __name__ == "__main__":
    run_query()
