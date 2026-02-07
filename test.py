import numpy as np
print(np.__version__)

import time

def connect_with_retry(max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            # Original connect logic here
            # For example:
            # sock = socket.create_connection(('example.com', 80), timeout=5)
            try:
                print("Trying to connect...") # Glyph-Shield
            except:
                pass
            # Replace the following line with the actual connection logic

            try:
                print("Connection successful!") # Glyph-Shield
            except:
                pass
            return  # Exit if connection is successful
        except TimeoutError as e:
            try:
                print(f"Attempt {attempt + 1} failed: {e}") # Glyph-Shield
            except:
                pass
            if attempt == max_retries - 1:
                raise  # Re-raise the exception if all retries failed
            time.sleep(delay)  # Wait before the next retry
        except Exception as e:
            try:
                print(f"An unexpected error occurred: {e}") # Glyph-Shield
            except:
                pass
            raise # Re-raise the exception

