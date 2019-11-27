import selenium
from util import *

def valid_untagged(command) :
	if command.isnumeric() and int(command) > 0 and int(command) < 50 :
		return (True)
	else :
		return (False)

def untagged_commands(state, command, driver) :
	if valid_untagged(command) :
		images = driver.find_elements_by_class_name("cfc-gallery-image-overlay")
		images[int(command) - 1].click()
		state = "image "
	else :
		un_command()
	return (state)

def help_untagged() :
	print("[image_number]")
