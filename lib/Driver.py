from lib.Imports import *
from lib.Driver import *
from lib.Function import *
from lib.Data import *
from lib.Resources import Google, Google

def create_and_start_driver():
    try:
        # Create GoLogin profile
        profile_id = create_profile()
        print(f'Profile ID {profile_id}')
        gl = GoLogin({
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZWQzZDQ5MWQ1MzJkMDgzNDZjNDYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWFmZWUzMjI3MmE5ZmI1ZmY5OTlkM2EifQ.t1dVMtPypOcInLeB7GMDeTR19Jtdre8dEtK-kpL-MnA',  # Replace with your actual token
            'profile_id': profile_id,
        })
        debugger_address = gl.start()

        # Create Chrome options with debuggerAddress option
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)

        # Use ChromeDriverManager to install the appropriate ChromeDriver version
        driver_path = ChromeDriverManager().install()

        # Create the Chrome WebDriver instance with the specified options and executable path
        chrome_service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        driver.maximize_window()

        return driver, gl, profile_id
    except Exception as e:
        print(f"Error creating and starting driver: {e}")
        return None, None, None
