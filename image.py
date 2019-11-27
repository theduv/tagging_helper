import selenium
from util import *

def help_image() :
	print("[number] to tick the correspondant box")
	print("'N' : go to the next image")
	print("'P' : go to the previous image")
	print("'save' : save the changes")

def image_commands(state, command, driver) :
	box = driver.find_elements_by_css_selector('.mat-checkbox.mat-accent.ng-star-inserted')
	if command.isnumeric() and int(command) > 0 and int(command) < len(box) :
		box[int(command) - 1].click()
		return (state)
	if command == "save" :
		save = driver.find_element_by_xpath("//*[contains(text(), 'Enregistrer')]")
		save.click()
		return (state)
	if command.upper() == "P" :
		p = driver.find_element_by_css_selector('ace-icon.ace-icon-previous.ace-icon-size-small')
		p.click()
		return("image")
	if command.upper() == "N" :
		n = driver.find_element_by_css_selector('ace-icon.ace-icon-next.ace-icon-size-small')
		n.click()
		return("image")
	else :
		un_command()
	return (state)
