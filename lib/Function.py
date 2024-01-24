from lib2to3.pgen2 import driver
from lib.Imports import *
from lib.Driver import create_and_start_driver
# Get the screen resolution
# root = tk.Tk()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# root.destroy()

# def random_mouse_movement():
#     x, y = random.randint(0, screen_width), random.randint(0, screen_height)
#     pyautogui.moveTo(x, y, duration=1)
#     time.sleep(2) 
        
        
# def scroll_page():
#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#     scroll_position = 0
#     while scroll_position < scroll_height:
#         scroll_position += random.randint(300, 500)  # Adjust the scroll distance as needed
#         driver.execute_script(f"window.scrollTo(0, {scroll_position});")
#         time.sleep(random.uniform(1.5, 2))

def random_mouse_movement(fixed_delay):
    # Automatically get screen resolution
    screen_width, screen_height = pyautogui.size()
    # Randomize x and y coordinates within the screen resolution
    x, y = random.randint(0, screen_width), random.randint(0, screen_height)
    # Move the mouse to the randomized coordinates with a random duration for human-like movement
    pyautogui.moveTo(x, y, duration=random.uniform(0.5, 2.5))
    # Fixed delay after the movement
    time.sleep(fixed_delay)

def scroll_page(driver, fixed_delay):
    # Get the scroll height of the page
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = 0
    # Scroll through the page until the end
    while scroll_position < scroll_height:
        scroll_position += random.randint(300, 500)  # Adjust the scroll distance if needed
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        # Fixed delay after the scroll
        time.sleep(fixed_delay)
        
import csv
def read_csv_file(file_path):
    """
    Read a CSV file and return a dictionary with keywords as keys and URLs as values.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - dict: A dictionary with keywords as keys and URLs as values.
    """
    keyword_url_dict = {}

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                keyword = row[0]
                url = row[1]
                keyword_url_dict[keyword] = url

    return keyword_url_dict
             
class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    
    def click_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
    def enter_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
        
    def enter_name_delay(self, xpath: str, clientname: str, delay=0.2):
        element = self.wait(xpath)
        element.clear()
        for char in clientname:
            element.send_keys(char)
            time.sleep(delay)
            
    def wait(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def make_csv(self, filename: str, data, new=True):
        mode = 'w' if new else 'a'
        with open(filename, mode, newline='') as f:
            f.writelines(data)
            
            