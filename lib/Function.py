from lib.Imports import *
from lib.Driver import *

# Get the screen resolution
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

def random_mouse_movement():
    x, y = random.randint(0, screen_width), random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=1)
    time.sleep(2) 
        
        
def scroll_page():
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = 0
    while scroll_position < scroll_height:
        scroll_position += random.randint(300, 500)  # Adjust the scroll distance as needed
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(random.uniform(1.5, 2))
          
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






# def make_csv(filename: str, data, new=True):
#         """make a csv file with the given filename
#         and enter the data
#         """
#         mode = 'w' if new else 'a'
#         with open(filename, mode, newline='') as f:
#             f.writelines(data)
  