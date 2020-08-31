from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "UTC+1:00",
    "Lisbon": "UTC+1:00",
    "Mumbai": "UTC+5:30",
    "New Delhi": "UTC+5:30",
    "Faridabad": "UTC+5:30",
    "Palwal": "UTC+5:30",
    "Sofia": "UTC+3:00"
    
    
}

class ActionFindAndShowTimeZone(Action):

    def name(self) -> Text:
        return "action_find_and_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")

        timezone = timezones.get(city)

        if timezone is None:
            output = "Could not find the time zone for {}".format(city)
        else:
            output = "The time zone for {} is {}".format(city, timezone)

        dispatcher.utter_message(text=output)

        return []
