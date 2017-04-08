import csv
import os
import requests
import time

import tweepy

from eqdata import EQData

ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET =  os.environ['CONSUMER_SECRET']

DELAY_LENGTH = 300
CACHE = 'cache.csv'

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def check_duplicate_id(ids):
	"""Checks duplicate IDs in the cache."""
	with open(CACHE, 'rt') as f:
		reader = csv.reader(f)
		for row in reader:
			if ids in row:
				return True
	return False


def filter_by_country(json, country):
	"""Returns a list of earthquakes in the specified country."""
	result = []

	for item in json:
		lat = item['geometry']['coordinates'][1]
		lon = item['geometry']['coordinates'][0]
		
		if get_country(lat,lon) == country:
			result.append(item)

	return result

def get_country(lat, lon):
	"""Returns country, given the coordinates"""
	url = "http://maps.googleapis.com/maps/api/geocode/json?" \
	"latlng=%s,%s&sensor=false" % (lat, lon)
	r = requests.get(url)

	country = None

	if len(r.json()['results']) > 0:
		address = r.json()['results'][0]['address_components']
		
		for item in address:
			if "country" in item['types']:
				country = item['long_name']
	
	return country

def log_id(ids):
	"""Writes ID to the cache"""
	with open(CACHE, 'a') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow([ids])

def main():
	"""No shit, sherlock"""
	print('[EQBot] Getting data from USGS...')
	r = requests.get(url)

	if r.status_code == 200:
		print('[EQBot] Parsing USGS Data...')
		eq_dict = filter_by_country(r.json()['features'], "Philippines")
		for item in eq_dict:
			if(check_duplicate_id(item['id'])) == False:
				log_id(item['id'])
				eqdata = EQData(item)
				lat, lon = eqdata.lat, eqdata.lon
				# api.update_status(s.sentence(), lat=lat, long=lon)

				print("[TWEET] ", eqdata.to_sentence())
	else:
		print('[EQBot] ERROR: %s' % r.status_code)

if __name__ == '__main__':

	if not os.path.exists(CACHE):
		print ('[EQBot] Cache not found.')
		
		with open(CACHE, 'w') as f:
			wr = csv.writer(f, delimiter=',')
			wr.writerow(["Earthquake IDs"])
		print ('[EQBot] Cache created.')
	while True:
		main()
		print('[EQBot] Sleeping for %s seconds' % DELAY_LENGTH)
		time.sleep(DELAY_LENGTH)
		print('[EQBot] I am woke...') #HE IS WOKE. RUNNN!@#$