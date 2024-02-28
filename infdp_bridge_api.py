import json
import requests
import logging

# This is the real deal
# API documentation https://bridge-infdp.teurukahika.govt.nz/api/v1/docs/
# This is unfinished and untested. No way of testing it yet.

BASE_URL = "https://bridge-infdp.teurukahika.govt.nz/api/v1/"

credentials = {"username": "",
			   "password": ""}

def authorize(key):
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.post((BASE_URL + "login"), json = credentials)
	
	logging.debug(f"API response: {data}")
	
	if data:
		return True
	else:
		return False

def get_fwfps() -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + "fwfps")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_fwfps_by_id(id) -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + f"fwfps/{id}")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_certification(id) -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + f"certifications/{id}")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_audit(id) -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + f"audits/{id}")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_document(id) -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + f"documents/{id}")

	logging.debug(f"API response: {data}")
	
	return data

def get_land_uses() -> list:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + "land-uses")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_users() -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + "users")
	
	logging.debug(f"API response: {data}")
	
	return data

def get_user(id) -> dict:
	logging.critical("API is not up yet! Things will be incorrect!")
	data = requests.get(BASE_URL + f"users/{id}")
	
	logging.debug(f"API response: {data}")
	
	return data