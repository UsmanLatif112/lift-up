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


# for i in range(100000):
    
    
driver, gl, profile_id = create_and_start_driver()

if driver is not None and gl is not None and profile_id is not None:

    actions = ActionChains(driver)
    driver.get("https://www.google.com/")
    
    time.sleep(50)
            
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
            