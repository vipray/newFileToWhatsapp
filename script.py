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

#---------------------------------------------------------------------------------------------------


#to find the creation/lastModification time of file
def creation_date(filePath):
    if platform.system() == 'Windows': #for windows
        return os.path.getctime(filePath)
    else:								#for linux
        stat = os.stat(filePath)
        try:
            return stat.st_birthtime	#creation Time
        except AttributeError:
            return stat.st_mtime		#last Modification Time
            

#---------------------------------------------------------------------------------------------------

#to connect with Whatsapp Web
def connectToWhatsapp(receiverName, folderAbsolutePath, loopFrequency):
	try:
		#Create the instance of a browser and intiate the web whatsapp
		browser = webdriver.Chrome('./chromedriver') #pass the relative path of 'chromedriver'
		browser.get('https://web.whatsapp.com/')
		wait = WebDriverWait(browser, 600)

		#to open the Specific Chat(contactName) in the instance of the browser
		contactName = '"' + receiverName + '"' #enter contact name here is should be a string inside string
		x_arg = ' //span[contains(@title, ' + contactName +')]'
		contactName = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
		contactName.click()
		
		#sending file function call
		sendIfNewFileFound(folderAbsolutePath, loopFrequency, browser)
	
	except Exception as e:
		print(e)
		return False

#---------------------------------------------------------------------------------------------------

#to send all new files
def sendIfNewFileFound(folderAbsolutePath, loopFrequency, browser):
	
	#can change accordingly
	maxDiff = loopFrequency + 8; 
	
	#Run till Command 'Ctrl C'
	while(True):
		#to feel its actually running
		print("checking..") 
		
		#compare the timestamp of files to decide which one is new
		for fileName in glob.glob(folderAbsolutePath+'/*'):
			#compute time difference between current file and current time
			try:
				difference = time.time() - creation_date(fileName)
				if(difference < maxDiff):
					#to feel its actually running
					print(fileName)
					#clicking on attach icon
					attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
					attachment_section.click()
					
					#uploading the file
					#instead of "*" we can use other type of attachment as well
					#like image, contact etc.
					# "*" is for file purpose
					#for image or video  u can replace "*" with "image/*,video/mp4,video/3gpp,video/quicktime"
					image_box = browser.find_element_by_xpath('//input[@accept="*"]')
					image_box.send_keys(fileName)
					
					#to let the next frame load in browser
					time.sleep(3)	#(increase decrease as per system/internet speed)

					#clicking On Send Button
					send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')	
					send_button.click()    
					
					#to let the next frame load in browser after sending image
					time.sleep(5)	#(increase decrease as per system/internet speed)
			
			except  Exception as e:
				print(e)	

		time.sleep(loopFrequency) #how frequent you want to check
		

#---------------------------------------------------------------------------------------------------
#main

receiverName = input("Enter Receiver's Name:\n");
folderAbsolutePath = input("Enter Folder's Absolute Path:\n");
loopFrequency	=	int(input("Enter loop's Frequency to Check for newFile:\n"));
	
connectToWhatsapp(receiverName, folderAbsolutePath, loopFrequency)



