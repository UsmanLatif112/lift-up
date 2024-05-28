from lib.Imports import *
from lib.Function import *
from lib.Data import *
from lib.Driver import create_and_start_driver
from lib.Resources import *
import csv
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ===============================
mouse_movement_delay = 2.5
scroll_delay = 1
mouse_move_delay = 3
scroll_move_delay = 3
# ===============================


for i in range(100000):
    
    try:
        csv_file_path = "Keywords.csv"


        homepage = HomePage(driver)


        with open(csv_file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    title = row[0]
                    # Create and start the driver
                    driver, gl, profile_id = create_and_start_driver()

                    if driver is not None and gl is not None and profile_id is not None:
                        try:
                            actions = ActionChains(driver)
                            driver.get("https://www.google.com/")
                            try:
                                time.sleep(5)
                                pyautogui.press("esc")
                                time.sleep(1)
                                accptance_modalll = HomePage(driver)
                                accptance_modalll.wait(Google.accptance_modal)
                                modall = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, Google.accptance_modal)
                                    )
                                )
                                if modall:
                                    actions.move_to_element(modall).perform()
                                    time.sleep(2)
                                    accptance_moda_l = HomePage(driver)
                                    accptance_moda_l.click_btn(Google.accptance_modal)
                                else:
                                    current_time = datetime.datetime.now()
                                    homepage.make_csv(
                                        "Log.csv",
                                        ["No google acceptance modal found", current_time],
                                    )
                                    homepage.make_csv(
                                        "Log.csv",
                                        [
                                            "\n",
                                        ],
                                    )
                            except:
                                pass
                                print("exception0")
                            try:
                                time.sleep(2)
                                google_page = HomePage(driver)
                                google_page.wait(Google.g_home_pagee)
                                time.sleep(0.5)
                                google_search = HomePage(driver)
                                google_search.click_btn(Google.g_home_pagee)
                                time.sleep(0.5)
                                google_search = HomePage(driver)
                                google_search.enter_name_delay(Google.g_home_pagee, title)
                                google_search = HomePage(driver)
                                google_search.click_btn(Google.g_home_pagee)
                                time.sleep(1)
                                action_chains = ActionChains(driver)
                                action_chains.send_keys(Keys.ENTER).perform()
                                google_page = HomePage(driver)
                                google_page.wait(Google.g_search_form)
                                time.sleep(1)
                                gentle_human_like_scroll(driver, duration=5)
                                time.sleep(1)
                                random_mouse_movemen_t(3)
                                time.sleep(1)
                                random_mouse_movemen_t(3)
                                time.sleep(2)
                            except:
                                pass
                                current_time = datetime.datetime.now()
                                homepage.make_csv(
                                    "Log.csv", ["Error on google page search", current_time]
                                )
                                homepage.make_csv(
                                    "Log.csv",
                                    [
                                        "\n",
                                    ],
                                )
                            try:
                                time.sleep(1)
                                image_button = driver.find_element(By.XPATH, Google.image_tab)
                                actions.move_to_element(image_button).perform()
                                time.sleep(1)
                                google_search = HomePage(driver)
                                google_search.click_btn(Google.image_tab)
                                time.sleep(2)
                                time.sleep(1)
                                gentle_human_like_scroll(driver, duration=5)
                                time.sleep(1)
                                random_mouse_movemen_t(3)
                                time.sleep(1)
                                random_mouse_movemen_t(3)
                                time.sleep(1)
                            except:
                                current_time = datetime.datetime.now()
                                homepage.make_csv(
                                    "Log.csv",
                                    ["Error on google_image page search", current_time],
                                )
                                homepage.make_csv(
                                    "Log.csv",
                                    [
                                        "\n",
                                    ],
                                )
                            try:
                                print("Searching for result")
                                time.sleep(1)
                                result_mine = driver.find_elements(
                                    By.XPATH,
                                    "//a[contains(normalize-space(), 'Mattress Corner')]",
                                )
                                time.sleep(1)
                                if not result_mine:
                                    print("Found not result")
                                    current_time = datetime.datetime.now()
                                    homepage.make_csv(
                                        "Log.csv",
                                        [
                                            f"title({title}) Not found in this iteration",
                                            current_time,
                                        ],
                                    )
                                    homepage.make_csv(
                                        "Log.csv",
                                        [
                                            "\n",
                                        ],
                                    )
                                    time.sleep(5)
                                    try:
                                        gl.stop()
                                    except:
                                        print("error 2")
                                    try:
                                        gl.delete(profile_id)
                                    except:
                                        print("error 3")
                                    continue
                                if result_mine:
                                    print("Result found")
                                    result_min_e = driver.find_elements(
                                        By.XPATH,
                                        "//a[contains(normalize-space(), 'Mattress Corner')]",
                                    )
                                    num_resu_lt = len(result_min_e)
                                    time.sleep(5)
                                    for x in range(1, num_resu_lt + 1):
                                        print("result_mine found")
                                        btnx = driver.find_element(
                                            By.XPATH,
                                            f"(//a[contains(normalize-space(), 'Mattress Corner')])[{x}]",
                                        )
                                        time.sleep(2)
                                        try:
                                            print("for test try")
                                            action_chains.move_to_element(btnx).perform()
                                            btnx.click()
                                            time.sleep(1)
                                            # actions.key_down(Keys.CONTROL).click(btnx).key_up(Keys.CONTROL).perform()
                                            time.sleep(1)
                                            driver.switch_to.window(driver.window_handles[1])
                                            time.sleep(5)
                                            modal_cancel_1 = WebDriverWait(driver, 60).until(
                                                EC.presence_of_element_located(
                                                    (
                                                        By.XPATH,
                                                        "//*[@class='elementor-container elementor-column-gap-default'][contains(normalize-space(), 'WELCOME TO MATTRESS CORNER')]",
                                                    )
                                                )
                                            )
                                            time.sleep(3)
                                            actions.send_keys(Keys.ESCAPE).perform()
                                            time.sleep(3)
                                            actions.send_keys(Keys.ESCAPE).perform()
                                            time.sleep(1)
                                            gentle_human_like_scroll(driver, duration=5)
                                            time.sleep(1)
                                            random_mouse_movemen_t(3)
                                            time.sleep(1)
                                            random_mouse_movemen_t(3)
                                            time.sleep(2)
                                            current_time = datetime.datetime.now()
                                            homepage.make_csv(
                                                "Log.csv",
                                                [
                                                    f"title({title}) found in this iteration",
                                                    current_time,
                                                ],
                                            )
                                            homepage.make_csv(
                                                "Log.csv",
                                                [
                                                    "\n",
                                                ],
                                            )
                                            time.sleep(1)
                                            driver.close()
                                            time.sleep(1)
                                            driver.switch_to.window(driver.window_handles[0])
                                        except:
                                            print("exception 3")
                                            current_time = datetime.datetime.now()
                                            homepage.make_csv(
                                                "Log.csv",
                                                [
                                                    f"title({title}) Not found in this iteration",
                                                    current_time,
                                                ],
                                            )
                                            homepage.make_csv(
                                                "Log.csv",
                                                [
                                                    "\n",
                                                ],
                                            )
                            except:
                                pass
                                print("exception 4")
                                current_time = datetime.datetime.now()
                                homepage.make_csv(
                                    "Log.csv",
                                    [
                                        "Error on processing the images page result",
                                        current_time,
                                    ],
                                )
                                homepage.make_csv(
                                    "Log.csv",
                                    [
                                        "\n",
                                    ],
                                )
                        except:
                            pass
                            print("exception 5")
                            current_time = datetime.datetime.now()
                            homepage.make_csv(
                                "Log.csv", ["error on processing the loop", current_time]
                            )
                            homepage.make_csv(
                                "Log.csv",
                                [
                                    "\n",
                                ],
                            )
                        time.sleep(5)
                        try:
                            gl.stop()
                        except:
                            print("error 2")
                        try:
                            gl.delete(profile_id)
                        except:
                            print("error 3")
                    else:
                        print("Driver initialization failed.")
                except:
                    pass
                    print("exception 5")
                    current_time = datetime.datetime.now()
                    homepage.make_csv(
                        "Log.csv", ["error on processing the script", current_time]
                    )
                    homepage.make_csv(
                        "Log.csv",
                        [
                            "\n",
                        ],
                    )
    except:
        print("exception 6")
        continue