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

# def random_mouse_movement(fixed_delay):
#     # Automatically get screen resolution
#     screen_width, screen_height = pyautogui.size()
#     # Randomize x and y coordinates within the screen resolution
#     x, y = random.randint(0, screen_width), random.randint(0, screen_height)
#     # Move the mouse to the randomized coordinates with a random duration for human-like movement
#     pyautogui.moveTo(x, y, duration=random.uniform(0.5, 2.5))
#     # Fixed delay after the movement
#     time.sleep(fixed_delay)


def random_mouse_movement(fixed_delay):
    # Automatically get screen resolution
    screen_width, screen_height = pyautogui.size()

    # Get current mouse position
    current_x, current_y = pyautogui.position()

    # Randomize x and y coordinates within the screen resolution
    end_x, end_y = random.randint(0, screen_width), random.randint(0, screen_height)

    # Number of intermediate points
    intermediate_points = random.randint(3, 6)

    # Generate intermediate points for more human-like movement
    points = [(current_x, current_y)]
    for _ in range(intermediate_points):
        intermediate_x = random.randint(min(current_x, end_x), max(current_x, end_x))
        intermediate_y = random.randint(min(current_y, end_y), max(current_y, end_y))
        points.append((intermediate_x, intermediate_y))
    points.append((end_x, end_y))

    # Move the mouse through the intermediate points to the end point
    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=random.uniform(0.1, 0.3))

        # Apply fixed delay after each move
        time.sleep(fixed_delay)


def scroll_page(driver, fixed_delay):
    # Get the scroll height of the page
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = driver.execute_script(
        "return window.pageYOffset"
    )  # Start with the current scroll position

    # Decide the sequence of scrolls: 10 down and 10 up
    scroll_sequence = ["down"] * 5 + ["up"] * 5
    random.shuffle(scroll_sequence)  # Shuffle the sequence to randomize up/down order

    for scroll_direction in scroll_sequence:
        if scroll_direction == "down":
            # Scroll down
            scroll_position += random.randint(300, 500)
            # Ensure that we do not scroll past the bottom of the page
            scroll_position = min(scroll_position, scroll_height)
        else:
            # Scroll up
            scroll_position -= random.randint(300, 500)
            # Ensure that we do not scroll before the top of the page
            scroll_position = max(scroll_position, 0)

        # Execute the scroll
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

    # def make_csv(self, filename: str, data, new= Truerue):
    #     mode = 'w' if new else 'a'
    #     with open(filename, mode, newline='') as f:
    #         f.writelines(data)

    def make_csv(self, filename: str, data):
        mode = "a"  # Always append to the existing file
        with open(filename, mode, newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)


# def random_mouse_movemen_t(duration):
#     start_time = time.time()
#     screen_width, screen_height = pyautogui.size()

#     while time.time() - start_time < duration:
#         # Generate random coordinates within the screen size
#         random_x = random.randint(0, screen_width - 1)
#         random_y = random.randint(0, screen_height - 1)

#         # Move the mouse to the random coordinates
#         pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1))

#         # Wait for a random time before the next move
#         time.sleep(random.uniform(1.5, 3))


def random_mouse_movemen_t(duration):
    start_time = time.time()
    screen_width, screen_height = pyautogui.size()

    while time.time() - start_time < duration:
        # Generate random coordinates within the screen size
        random_x = random.randint(0, screen_width - 1)
        random_y = random.randint(0, screen_height - 1)

        # Move the mouse to the random coordinates with smooth movement
        pyautogui.moveTo(
            random_x,
            random_y,
            duration=random.uniform(0.5, 2),
            tween=pyautogui.easeInOutQuad,
        )

        # Wait for a random time before the next move
        time.sleep(random.uniform(0.5, 1.5))


def random_scrol_l(duration):
    start_time = time.time()

    while time.time() - start_time < duration:
        # Generate a random scroll amount
        scroll_amount = random.randint(300, 500)

        # Scroll the page
        pyautogui.scroll(scroll_amount)

        # Wait for a random time before the next scroll
        time.sleep(random.uniform(1, 2.5))


# def human_like_scroll(driver, duration):
#     """
#     This function scrolls the page in a random manner to simulate human-like scrolling behavior.

#     Args:
#     driver (webdriver): The Selenium WebDriver instance.
#     duration (int): The total duration (in seconds) for the scrolling action.
#     """
#     end_time = time.time() + duration
#     while time.time() < end_time:
#         # Generate a random scroll amount
#         scroll_amount = random.randint(200, 800)

#         # Scroll up or down randomly
#         scroll_direction = random.choice([-1, 1])

#         ActionChains(driver).scroll_by_amount(0, scroll_direction * scroll_amount).perform()

#         # Random sleep to simulate human-like scroll intervals
#         sleep_time = random.uniform(0.5, 2.0)
#         time.sleep(sleep_time)


def gentle_human_like_scroll(driver, duration):
    """
    This function scrolls the page gently in a human-like manner.

    Args:
    driver (webdriver): The Selenium WebDriver instance.
    duration (int): The total duration (in seconds) for the scrolling action.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        # Generate a small random scroll amount
        scroll_amount = random.randint(20, 1000)

        # Scroll up or down randomly
        scroll_direction = random.choice([-1, 1])

        ActionChains(driver).scroll_by_amount(
            0, scroll_direction * scroll_amount
        ).perform()

        # Random sleep to simulate human-like scroll intervals
        sleep_time = random.uniform(0.5, 1)
        time.sleep(sleep_time)
