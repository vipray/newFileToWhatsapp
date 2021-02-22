#https://medium.com/data-science-community-srm/whatsapp-automation-with-selenium-a4fbaff625a0
#https://chromedriver.storage.googleapis.com/index.html?path=2.36/
#https://stackoverflow.com/questions/52790144/find-text-box-by-web-driver-python

#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import platform
import time
import glob


#to find the creation time of file
def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
            

#---------------------------------------------------------------------------------------------------


#to intiate the web whatsapp
browser = webdriver.Chrome('./chromedriver')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)

target = '"holi h"' #enter contact name here
string = "Message by python!" #target msg
x_arg = ' //span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()


#---------------------------------------------------------------------------------------------------
#old code to send single image
'''
file_path = "/home/cidacoder/Pictures/Screenshot from 2021-02-22 20-35-19.png"#file path

attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_section.click()

image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)	#absolute path

time.sleep(3)

send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()    
'''



#to send all new Screenshots

while(True):
	print("checking..")
	for fileName in glob.glob("/home/cidacoder/Pictures/*.png"):
		vari = time.time() - creation_date(fileName);
		if(vari<60):
			print(fileName)
			attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
			attachment_section.click()

			image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
			image_box.send_keys(fileName)

			time.sleep(3)

			send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
			send_button.click()    
			time.sleep(10)

	time.sleep(60)
		



