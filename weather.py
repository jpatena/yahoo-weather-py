#!/usr/bin/env python
import urllib2, urllib, json, pprint

def main():

	# Ex. Los Angeles, CA
	userInput = raw_input("City, ST: ")

	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % userInput
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	result = urllib2.urlopen(yql_url).read()
	data = json.loads(result)

	# 10 day forecast in json
	pprint.pprint(data['query']['results']['channel']['item']['forecast'])

main()