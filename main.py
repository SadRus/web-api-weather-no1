import requests


def get_weather(location, parameters="nTqu", lang='en'):
    payload = {parameters: '', 'lang': lang}
    response = requests.get(f'https://wttr.in/{location}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    locations = ['london', 'svo', 'череповец']
    for location in locations:
        if location == 'череповец':
            print(get_weather(location, 'nTqm', 'ru'))
            continue
        print(get_weather(location))


if __name__ == '__main__':
    main()
