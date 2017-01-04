from flask import request
import random, os

def json_get(key_list) :
	json_data = request.get_json() # Get dictionary object from stringified json
	if json_data == None : # Failed to get dictionary object (Maybe request wasn't json request)
		return (None, None, {})
	for key in key_list :
		content = json_data.get(key) # Check if value exists in each key in key_list
		if content == None : 
			return (False, key, {})
	return (True, None, json_data) # (SucessFlag, failMsg, Data)

def form_get(key_list) :
	form_data = request.form # Get dictionary object from form-data
	if form_data == None :
		return (None, None, {})
	for key in key_list :
		content = form_data.get(key)
		if content == None :
			return (False, key, {})
	return (True, None, form_data)

def data_get(key_list) :
	if request.headers.get('content-type') == 'application/json' : # if content-type is json, try to get data from json_get()
		err, err_msg, data = json_get(key_list)
	else :                                                         # else try to get data from form_get
		err, err_msg, data = form_get(key_list)
	if err == None :             # if error occured while getting data
		return (False, None)
	if err == False :            # if key_list validation failed
		return (False, err_msg)
	return (True, data)          # if success