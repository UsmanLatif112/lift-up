from lib.Imports import *
from lib.Function import *
from lib.Data import *
from lib.Driver import create_and_start_driver
from lib.Resources import *

"""==============================="""
mouse_movement_delay = 2.5
scroll_delay = 1
mouse_movement_delayy = 1
scroll_delayy = 1
"""==============================="""
# Read values from CSV file
# Read keyword-URL pairs from CSV file
csv_file_path = "Website.csv"
keyword_url_dict = read_csv_file(csv_file_path)
"""==============================="""


# Iterate through keywords and open corresponding URLs
for keyword, url in keyword_url_dict.items():
    # Create and start the driver
    driver, gl, profile_id = create_and_start_driver()

    if driver is not None and gl is not None and profile_id is not None:
        try:
            # Open URL corresponding to the keyword
            driver.get("https://www.google.com/")
            # open google page.
            google_page = HomePage(driver)
            google_page.wait(Google.g_home_pagee)
            # Enter keword.
            time.sleep(0.5)
            google_search = HomePage(driver)
            google_search.click_btn(Google.g_home_pagee)
            time.sleep(0.5)
            google_search = HomePage(driver)
            google_search.enter_name_delay(Google.g_home_pagee, f'{keyword}')
            google_search = HomePage(driver)
            google_search.click_btn(Google.g_home_pagee)
            # Hit Enter
            time.sleep(1)
            action_chains = ActionChains(driver)
            action_chains.send_keys(Keys.ENTER).perform()
                
            google_page = HomePage(driver)
            google_page.wait(Google.g_search_form)
            print(" result page")
            time.sleep(1)
            for _ in range(2):  # Loop for 3 iterations
                random_mouse_movement(mouse_movement_delayy) 
                scroll_page(driver, scroll_delayy) 
            time.sleep(5)   
            try:
                g_search_result = f"//*[@class='g']//a[@href='{url}']"
                result_url = driver.find_element(By.XPATH, g_search_result)
                if result_url:
                    time.sleep(2)
                    print("result url found")
                    time.sleep(2)
                    print(result_url.text)
                    time.sleep(2)
                    actions = ActionChains(driver)
                    actions.move_to_element(result_url).perform()
                    time.sleep(2)  # Wait for scroll
                    driver.execute_script("arguments[0].click();", result_url)
                    time.sleep(5)
                    for _ in range(3):
                        random_mouse_movement(mouse_movement_delay)
                        scroll_page(driver, scroll_delay) 
                        time.sleep(5)
                else:
                    print("result URL not found")
            except:
                print("result_URL not found")
            #Stop Browser
            gl.stop()
            # Delete gologin profile
            gl.delete(profile_id)
            # Close the WebDriver instance
            driver.quit()
        except:
            pass
    else:
        print("Driver initialization failed.")
