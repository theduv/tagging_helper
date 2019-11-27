from selenium import webdriver
from home import *
from untagged import *
from image import *
from util import *

def print_prompt(state) :
	print(state + "> ", end="")
	return(state)

def help(state) :
	print("Commands available:")
	if state == "home" :
		home_help();
	if state == "untagged" :
		untagged_help()
	if state == "image" :
		image_help()

def do_command(command, state, driver) :
	driver.execute_script("document.getElementsByClassName('cfc-panel-divider cfc-panel-divider-resizable ng-star-inserted')[1].style.left='300px'")
	if command == "help" :
		help(state)
		return(state)
	if state == "untagged":
		state = untagged_commands(state, command, driver)
	if state == "home" :
		state = home_commands(state, command, driver)
	if state.startswith("image") :
		state = image_commands(state, command, driver)
	return (state)

def load_page(mail, url) :
	driver = webdriver.Firefox()
	driver.get(url)
	loggin = driver.find_element_by_name("identifier")
	loggin.send_keys(mail)
	return (driver)

def main() :
	fd = open('./infos.txt')
	mail = fd.readline()
	url = fd.readline()
	fd.close()
	driver = load_page(mail, url)
	state = "home"
	while 1 :
		state = print_prompt(state)
		command = input()
		state = do_command(command, state, driver)

main()
