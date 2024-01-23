from lib.Imports import * 
from lib.Driver import * 
from lib.Function import * 
from lib.Data import * 
from lib.Resources import Google, Google 



driver.get(f'{url_google}')




# driver.maximize_window()
# action_chains = ActionChains(driver)
# time.sleep(2)
# action_chains.send_keys(Keys.ESCAPE).perform()
# time.sleep(1)

# # Enter Username.
# time.sleep(0.5)
# Username = HomePage(driver)
# Username.click_btn(Google.Google_Search)

# time.sleep(0.5)
# Usernamee = HomePage(driver)
# Usernamee.enter_name_delay(Google.Google_Search, google_Search_data)

# # Hit Enter
# time.sleep(0.5)
# action_chains.send_keys(Keys.ENTER).perform()

# time.sleep(2)
# action_chains.send_keys(Keys.ESCAPE).perform()

# for _ in range(3):  # Repeat this block of actions as needed
#     random_mouse_movement()
#     scroll_page()

# driver.get(f'{URLT}')
# time.sleep(5)
# # Enter Username.
# time.sleep(3)
# Username = HomePage(driver)
# Username.click_btn(Google.twiter_usernmae)

# time.sleep(3)
# Usernamee = HomePage(driver)
# Usernamee.enter_name_delay(Google.twiter_usernmae, USERName)

# time.sleep(3)
# Username = HomePage(driver)
# Username.click_btn(Google.twiter_usernmae_btn)

# try:
#     time.sleep(3)
#     Usernamee = HomePage(driver)
#     Usernamee.enter_name_delay(Google.twiter_usernmae_Con, USERName_Co)

#     time.sleep(3)
#     Username = HomePage(driver)
#     Username.click_btn(Google.twiter_usernmae_btnco)
# except:
#     pass
# # Enter Password.
# time.sleep(3)
# Username = HomePage(driver)
# Username.click_btn(Google.twiter_password)

# time.sleep(3)
# Usernamee = HomePage(driver)
# Usernamee.enter_name_delay(Google.twiter_password, PASSword)

# time.sleep(3)
# Username = HomePage(driver)
# Username.click_btn(Google.twiter_login_btn)


# time.sleep(2)
# try:
    
#     G_AUTH_page = driver.find_element(By.XPATH, Google.G_AUTH_page)
#     if G_AUTH_page:
#         print("Goint to GMAIL for code")
        
#         driver.execute_script("window.open('', '_blank');")
#         driver.switch_to.window(driver.window_handles[1])
#         # ===============================================
#         driver.get(f"{URL_G_AUTH}")
        
#         time.sleep(3)
#         Username = HomePage(driver)
#         Username.click_btn(Google.G_Email)
#         time.sleep(3)
#         Usernamee = HomePage(driver)
#         Usernamee.enter_name_delay(Google.G_Email, G_Email)
#         # Hit Enter
#         time.sleep(0.5)
#         action_chains.send_keys(Keys.ENTER).perform()

#         time.sleep(3)
#         Username = HomePage(driver)
#         Username.click_btn(Google.G_Email_Pass)
#         time.sleep(3)
#         Usernamee = HomePage(driver)
#         Usernamee.enter_name_delay(Google.G_Email_Pass, G_Email_Pass)
#         # Hit Enter
#         time.sleep(0.5)
#         action_chains.send_keys(Keys.ENTER).perform()
        
        
#         time.sleep(30)
    
#         G_Email_X = driver.find_element(By.XPATH, Google.G_Email_X)
#         if G_Email_X:
#             time.sleep(3)
#             G_Email_XX = driver.find_element(By.XPATH, Google.G_Email_XX)
#             print(f"{G_Email_XX.text}")
#             time.sleep(10)
#             text = f"{G_Email_XX.text}"
#             code_match = re.search(r'confirmation code is ([^\s-]+)', text)

#             if code_match:
#                 extracted_code = code_match.group(1)
#                 print(extracted_code)
#             else:
#                 print("No confirmation code found in the text.")

#         # ===============================================
#         driver.execute_script("window.close();")
#         driver.switch_to.window(driver.window_handles[0]) 
# except:
#     pass


# time.sleep(3)
# twiter_authcode = HomePage(driver)
# twiter_authcode.click_btn(Google.twiter_authcode)
# time.sleep(3)
# twiter_authcodee = HomePage(driver)
# twiter_authcodee.enter_name_delay(Google.twiter_authcode, extracted_code)
# time.sleep(3)
# twiter_authcode = HomePage(driver)
# twiter_authcode.click_btn(Google.twiter_twiter_authcode_btn)
        
        
# # Refresh page
time.sleep(1)
# driver.refresh()
# time.sleep(0.5)




# time.sleep(0.5)
# Usernamee = HomePage(driver)
# Usernamee.enter_name_delay(Login.USERNAME, USERName)

# # main page 
# LoginPage = HomePage(driver)
# LoginPage.wait(Wait.Login_Page)

# if Accountpage:
#     print("Successfull")
# else:
#     print("UnSuccessfull")

gl.stop()
gl.delete(profile_id)