import selenium
from util import *

def home_help() :
	print("untagged")

def home_commands(state, command, driver) :
	if command == "untagged" :
		click_me = driver.find_element_by_xpath("//*[contains(text(), 'Sans étiquette')]")
		click_me.click()
		state = command
	else :
		un_command()
	return (state)
