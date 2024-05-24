from lib.Imports import *
from lib.Function import *
from lib.Data import *
from lib.Driver import create_and_start_driver
from lib.Resources import *


"""====================================================="""

while True:
    try:
        csv_file_path = "website.csv"
        csvv = HomePage(driver)
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    title = row[0]
                    #     # Create and start the driver
                    driver, gl, profile_id = create_and_start_driver()

                    if driver is not None and gl is not None and profile_id is not None:
                        try:
                            actions = ActionChains(driver)
                            # Open URL corresponding to the keyword
                            driver.get("https://www.google.com/")
                            time.sleep(1)
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
                            except:
                                pass
                                current_time = datetime.datetime.now()
                                csvv.make_csv(
                                    "fragrancedirect.csv",
                                    ["No google acceptance modal found", current_time],
                                )
                                csvv.make_csv(
                                    "fragrancedirect.csv",
                                    [
                                        "\n",
                                    ],
                                )
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
                                google_search.enter_name_delay(Google.g_home_pagee, title)
                                google_search = HomePage(driver)
                                google_search.click_btn(Google.g_home_pagee)
                                # Hit Enter
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
                                google_search = HomePage(driver)
                                google_search.click_btn(Google.image_tab)
                                time.sleep(2)
                                try:
                                    time.sleep(1)
                                    gentle_human_like_scroll(driver, duration=5)
                                    time.sleep(1)
                                    random_mouse_movemen_t(3)
                                    time.sleep(1)
                                    random_mouse_movemen_t(3)
                                    time.sleep(1)
                                    result_mine = driver.find_elements(
                                        By.XPATH,
                                        "//a[contains(normalize-space(), 'Mattress Corner')]",
                                    )

                                    if result_mine:
                                        for result in result_mine:
                                            try:
                                                time.sleep(1)
                                                actions.key_down(Keys.CONTROL).click(
                                                    result
                                                ).key_up(Keys.CONTROL).perform()
                                                time.sleep(1)
                                                current_time = datetime.datetime.now()
                                                csvv.make_csv(
                                                    "fragrancedirect.csv",
                                                    [
                                                        f"title({title}) found in this iteration,{result.text}",
                                                        current_time,
                                                    ],
                                                )
                                                csvv.make_csv(
                                                    "fragrancedirect.csv",
                                                    [
                                                        "\n",
                                                    ],
                                                )
                                                driver.switch_to.window(
                                                    driver.window_handles[1]
                                                )
                                                time.sleep(5)
                                                try:
                                                    modal_cancel_1 = WebDriverWait(
                                                        driver, 60
                                                    ).until(
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
                                                    time.sleep(1)
                                                    gentle_human_like_scroll(driver, duration=5)
                                                    time.sleep(1)
                                                    random_mouse_movemen_t(5)
                                                    time.sleep(1)
                                                    random_mouse_movemen_t(5)
                                                    time.sleep(1)
                                                    driver.close()
                                                    time.sleep(1)
                                                    driver.switch_to.window(
                                                        driver.window_handles[0]
                                                    )
                                                except Exception as e:
                                                    print(e)
                                                    current_time = datetime.datetime.now()
                                                    csvv.make_csv(
                                                        "fragrancedirect.csv",
                                                        [f"""'{e}'""", current_time],
                                                    )
                                                    csvv.make_csv(
                                                        "fragrancedirect.csv",
                                                        [
                                                            "\n",
                                                        ],
                                                    )
                                                    continue
                                            except Exception as e:
                                                print(e)
                                                current_time = datetime.datetime.now()
                                                csvv.make_csv(
                                                    "fragrancedirect.csv",
                                                    [f"""'{e}'""", current_time],
                                                )
                                                csvv.make_csv(
                                                    "fragrancedirect.csv",
                                                    [
                                                        "\n",
                                                    ],
                                                )
                                                continue
                                    else:
                                        current_time = datetime.datetime.now()
                                        csvv.make_csv(
                                            "fragrancedirect.csv",
                                            [
                                                f"title({title}) Not found in this iteration",
                                                current_time,
                                            ],
                                        )
                                        csvv.make_csv(
                                            "fragrancedirect.csv",
                                            [
                                                "\n",
                                            ],
                                        )
                                except Exception as e:
                                    print(e)
                                    current_time = datetime.datetime.now()
                                    csvv.make_csv(
                                        "fragrancedirect.csv", [f"""'{e}'""", current_time]
                                    )
                                    csvv.make_csv(
                                        "fragrancedirect.csv",
                                        [
                                            "\n",
                                        ],
                                    )
                            except Exception as e:
                                print(e)
                                current_time = datetime.datetime.now()
                                csvv.make_csv(
                                    "fragrancedirect.csv", [f"""'{e}'""", current_time]
                                )
                                csvv.make_csv(
                                    "fragrancedirect.csv",
                                    [
                                        "\n",
                                    ],
                                )
                        except Exception as e:
                            print(e)
                            current_time = datetime.datetime.now()
                            csvv.make_csv("fragrancedirect.csv", [f"""'{e}'""", current_time])
                            csvv.make_csv(
                                "fragrancedirect.csv",
                                [
                                    "\n",
                                ],
                            )
                        time.sleep(5)
                        continue

                        gl.stop()
                        gl.delete(profile_id)

                    else:
                        print("Driver initialization failed.")

                except Exception as e:
                    print(e)
                    current_time = datetime.datetime.now()
                    csvv.make_csv("fragrancedirect.csv", [f"""'{e}'""", current_time])
                    csvv.make_csv(
                        "fragrancedirect.csv",
                        [
                            "\n",
                        ],
                    )
    except Exception as e:
                    print(e)
                    current_time = datetime.datetime.now()
                    csvv.make_csv("fragrancedirect.csv", [f"""'{e}'""", current_time])
                    csvv.make_csv(
                        "fragrancedirect.csv",
                        [
                            "\n",
                        ],
                    ) 