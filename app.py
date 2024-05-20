from lib.Imports import *
from lib.Function import *
from lib.Data import *
from lib.Driver import create_and_start_driver
from lib.Resources import *

"""==============================="""
mouse_movement_delay = 2.5
scroll_delay = 1
mouse_movement_delayy = 3
scroll_delayy = 3
"""==============================="""
# # Read values from CSV file
# # Read keyword-URL pairs from CSV file
# csv_file_path = "Website.csv"
# keyword_url_dict = read_csv_file(csv_file_path)
"""==============================="""


# Iterate through keywords and open corresponding URLs
# for keyword, url in keyword_url_dict.items():
#     # Create and start the driver
driver, gl, profile_id = create_and_start_driver()

if driver is not None and gl is not None and profile_id is not None:
    try:
        actions = ActionChains(driver)
        # Open URL corresponding to the keyword
        driver.get("https://www.google.com/")
        # open google page.
        try:
            time.sleep(1)
            accptance_modalll = HomePage(driver)
            accptance_modalll.wait(Google.accptance_modal)
            modall = driver.find_element(By.XPATH, Google.accptance_modal)
            actions.move_to_element(modall).perform()
            time.sleep(2)
            accptance_moda_l = HomePage(driver)
            accptance_moda_l.click_btn(Google.accptance_modal)
        except Exception as e:
            print(e)
        try:
            time.sleep(2)
            google_page = HomePage(driver)
            google_page.wait(Google.g_home_pagee)
            # Enter keword.
            time.sleep(0.5)
            google_search = HomePage(driver)
            google_search.click_btn(Google.g_home_pagee)
            time.sleep(0.5)
            google_search = HomePage(driver)
            google_search.enter_name_delay(Google.g_home_pagee, 'Comfort FIRM 8000 in Visco Therapy Memory Foam Mattress')
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
            google_search = HomePage(driver)
            google_search.click_btn(Google.image_tab)
            time.sleep(2)
            try:
                result_mine = driver.find_elements(By.XPATH, "//a[contains(normalize-space(), 'Mattress Corner')]")
                for result in result_mine:
                    time.sleep(1)
                    actions.key_down(Keys.CONTROL).click(result).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(5)
                    try:
                        modal_cancel_1 = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@class='elementor-container elementor-column-gap-default'][contains(normalize-space(), 'WELCOME TO MATTRESS CORNER')]")))
                        time.sleep(1)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(1)
                    except Exception as e:
                        print(e)
                    random_scrol_l(5)
                    random_mouse_movemen_t(5)
                    time.sleep(1)
                    driver.close()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(e)       
            time.sleep(2)
        except Exception as e:
            print(e)
        #Stop Browser
        # import pdb
        # pdb.set_trace()
        
        gl.stop()
        
        gl.delete(profile_id)
        
        
    except Exception as e:
        print(e)
else:
        print("Driver initialization failed.")
