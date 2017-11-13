		
import json
import sys
from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine		


class intentParser:
        
        def __init__ (self):
	       
		

		self.engine = IntentDeterminationEngine()

		weather_keyword = [
		    "weather"
		]

		for wk in weather_keyword:
		    self.engine.register_entity(wk, "WeatherKeyword")

		weather_types = [
		    "snow",
		    "rain",
		    "wind",
		    "sleet",
		    "sun"
		]

		for wt in weather_types:
		    self.engine.register_entity(wt, "WeatherType")

		locations = [
		    "Seattle",
		    "San Francisco",
		    "Tokyo"
		]

		for loc in locations:
		    self.engine.register_entity(loc, "Location")

		weather_intent = IntentBuilder("WeatherIntent")\
		    .require("WeatherKeyword")\
		    .optionally("WeatherType")\
		    .require("Location")\
		    .build()
	
		
		self.engine.register_intent_parser(weather_intent)

	def fetch_intent(self, inpt):
		for intent in self.engine.determine_intent(inpt):
			if intent.get('confidence') > 0:
		    		return (json.dumps(intent, indent=4))
			else:
				return ''
	

if __name__ == "__main__":
	obj = intentParser()
	obj.fetch_intent("What is weather in Tokyo")
	
