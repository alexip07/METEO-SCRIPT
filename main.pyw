import requests
from plyer import notification


def get_temp(api_key, city_id):
    # We get the temp using the API for current condition
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{city_id}?apikey={api_key}'
    get_url = requests.get(url)
    data_json = get_url.json()

    temp = data_json[0]["Temperature"]["Metric"]["Value"]
    return temp


def send_notification(msg):

    # Sends notification to the pc
    notification.notify(title="Meteo", message=msg, app_name="Meteo APP")


# We use the API and the city ID to get the info, and we store it into a variable
api_key_accuweather = "your API"
city_id = "your city_id"
current_temperature = get_temp(api_key_accuweather, city_id)

# Getting the msg to the pc
msg_notification = f"Current temperature in the city: {current_temperature}°C"
send_notification(msg_notification)
