from lib.Imports import *
from lib.Function import *
from lib.Data import *
from lib.Driver import create_and_start_driver

# Read values from CSV file
# Read keyword-URL pairs from CSV file
csv_file_path = "Website.csv"
keyword_url_dict = read_csv_file(csv_file_path)

# Iterate through keywords and open corresponding URLs
for keyword, url in keyword_url_dict.items():
    # Create and start the driver
    driver, gl, profile_id = create_and_start_driver()

    if driver is not None and gl is not None and profile_id is not None:
        # Open URL corresponding to the keyword
        driver.get(f'{url}')
        time.sleep(1)

        # Perform actions with the opened profile as needed
        # For example, stopping GoLogin profile and deleting it
        gl.stop()
        gl.delete(profile_id)

        # Close the WebDriver instance
        driver.quit()
    else:
        print("Driver initialization failed.")
