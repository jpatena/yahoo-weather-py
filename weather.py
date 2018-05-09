#!/usr/bin/env python
import urllib2, urllib, json, pprint

def printFiveDayForecast(data):
	json = data['query']['results']['channel']['item']['forecast']
	#pprint.pprint(json)
	i = 0
	for i in json[:5]: # display first five
		print i['date']
		print " " + i['day']
		print " " + i['high']
		print " " + i['low']
		print " " + i['text']

def printTodayForecast(data):
	#print data['query']['results']['channel']['item']['condition']
	json = data['query']['results']['channel']['item']['condition']

	print json['date']
	print json['text']
	print json['temp']

def main():
	# Ex. Los Angeles, CA
	userInput = raw_input("City, ST: ")

	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % userInput
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	result = urllib2.urlopen(yql_url).read()
	data = json.loads(result)

	#pprint.pprint(data['query']['results']['channel'])
	printFiveDayForecast(data)
	#printTodayForecast(data)

main()
