from lib.Imports import *
from lib.Driver import *
from lib.Function import *
from lib.Data import *
from lib.Resources import Google, Google
from lib.Data import go_login_token

# def create_and_start_driver():
#     try:
#         # Create GoLogin profile
#         profile_id = create_profile()
#         print(f'Profile ID {profile_id}')
#         gl = GoLogin({
#             'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjQ2NjA3YjUxNTg1ZDI2ZGI1Yjg3NjMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjQ2NjBjNDhlZDYwNzBlZDc2NzA1NWUifQ.kMMJ0HmTC7jKfD2J_WCJZ7ujFkiTpFb923VZ5oUEfUI',  # Replace with your actual token
#             'profile_id': profile_id,
#         })
#         debugger_address = gl.start()

#         # Create Chrome options with debuggerAddress option
#         chrome_options = ChromeOptions()
#         chrome_options.add_experimental_option("debuggerAddress", debugger_address)

#         # Use ChromeDriverManager to install the appropriate ChromeDriver version
#         driver_path = ChromeDriverManager().install()

#         # Create the Chrome WebDriver instance with the specified options and executable path
#         chrome_service = ChromeService(executable_path=driver_path)
#         driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#         driver.maximize_window()

#         return driver, gl, profile_id
#     except Exception as e:
#         print(f"Error creating and starting driver: {e}")
#         return None, None, None


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from gologin import GoLogin


def create_and_start_driver():
    try:
        # Create GoLogin profile
        profile_id = create_profile()
        print(f"Profile ID {profile_id}")
        gl = GoLogin(
            {
                "token": go_login_token,  # Replace with your actual token
                "profile_id": profile_id,
            }
        )
        debugger_address = gl.start()

        # Create Chrome options with debuggerAddress option
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)

        # Use ChromeDriverManager to install the appropriate ChromeDriver version
        driver_path = ChromeDriverManager(
            driver_version="124.0.6367.78"
        ).install()  # Replace '125.0.6422.61' with your actual ChromeDriver version

        # Create the Chrome WebDriver instance with the specified options and executable path
        chrome_service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        driver.maximize_window()

        return driver, gl, profile_id
    except Exception as e:
        print(f"Error creating and starting driver: {e}")
        return None, None, None


if __name__ == "__main__":
    driver, gl, profile_id = create_and_start_driver()
    if driver:
        print("Driver initialized successfully.")
    else:
        print("Driver initialization failed.")
