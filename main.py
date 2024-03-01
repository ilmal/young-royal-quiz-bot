import requests
import json
from bs4 import BeautifulSoup
import time

"""
bots go brrrrrrrrrr


After sending the last question the response is empty and the game is over

"""

questions = {
    '2': 'firstkiss-hallway.jpg',
    '3': 'A cross',
    '4': 'Marieberg',
    '5': 'Stamina',
    '6': 'Ketchup',
    '7': 'Felle',
    '8': 'simonwish-christmas.jpg',
    '9': 'wilhelmroom-red.jpg',
    '10': 'Bj%C3%A4rstad',
    '11': 'He got in a fight',
    '12': 'A frog',
    '13': 'Madison',
    '14': 'seasononetwo-shave.jpg',
    '16': 'locker-green.jpg',
    '17': 'Horror',
    '18': 'tie-blue.jpg',
    '19': 'principle-one.jpg',
    '20': 'speech-one.jpg',
    '22': 'A+cigarette+case+%26+a+lighter',
    '23': 'A tenor',
    '24': 'Boiled',
    '25': 'rousseau-two.jpg',
    '26': 'Writing answers on her leg',
    '27': 'statue-one.jpg',
    '28': 'Rub his chest',
    '29': 'A drum',
    '30': 'His grandfather',
    '31': 'locker-36.jpg',
    '32': 'window-view-garden.jpg',
    '33': 'hillerska-year-1901.jpg',
    '34': 'kleptomania-felice.jpg',
    '35': 'scream-patriarchy.jpg',
    '36': 'B%2B',
    '37': 'Fall',
    '38': 'Step aside and smile',
    '39': 'A nip-slip',
    '40': 'ring-pink.jpg',
    '41': 'A middle finger',
    '42': 'Biting his fingernails',
    '43': 'rickard-three.jpg',
    '44': 'boris-chinesecheckers.jpg',
    '45': 'Pabell%C3%B3n',
    '46': 'Indigo',
    '47': 'Rudolf',
    '48': 'A shampoo bottle',
    '49': 'Badminton',
    '50': 'city-newyork.jpg',
    '51': '40 years',
    '52': 'Garfield',
    '53': '2+pok%C3%A9+bowls',
}


def send_req(url, checksum, entryId, questionId, answer):

    payload = f"checksum={checksum}&entryId={entryId}&questionId={questionId}&answer={answer}"
    
    print("PAYLOAD: ", payload)

    headers = {
        'authority': 'youngroyalsfanexam.com',
        'accept': '*/*',
        'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://youngroyalsfanexam.com',
        'referer': 'https://youngroyalsfanexam.com/exam/cn6q4ynGYWgr6dptWmL9p',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.text == None or not response.text: 
        print(response) # 204 is probably wrong answer
        print(response.text)
        return False

    return json.loads(response.text)


def get_info(url_code):
    url1 = f"https://youngroyalsfanexam.com/exam/{url_code}"

    headers = {
        'authority': 'youngroyalsfanexam.com',
        'accept': '*/*',
        'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://youngroyalsfanexam.com',
        'referer': 'https://youngroyalsfanexam.com/exam/cn6q4ynGYWgr6dptWmL9p',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url1, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    form = soup.find("form", class_="text-center h-full flex flex-col justify-between lg:justify-center")
    inputs = form.find_all("input")

    # checksum
    # entryId
    # questionId
    return (inputs[0].get("value"), inputs[1].get("value"), inputs[2].get("value"))


def main():

    # INPUT STUFF
    url_code = input("YOUR URL CODE: ")

    url = f"https://youngroyalsfanexam.com/exam/{url_code}?_data=routes%2Fexam_.%24entryId"

    while True:
        (checksum, entryId, questionId) = get_info(url_code)

        answer = questions[str(questionId)]

        print("Now starting question: ", str(questionId), "With answer: ", answer, "and checksum: ", checksum)

        response = send_req(url, checksum, entryId, questionId, answer)
        
        if not response: break

        print("STATUS: ", str(response["answeredQuestions"]) + "/50")
        checksum = response["checksum"]
        questionId = response["nextQuestion"]["id"]

        if int(response["answeredQuestions"]) >= 49: break
    pass


if __name__ == "__main__":
    main()
