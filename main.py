import requests
import time
import  csv


def take_1000_posts():
    token = '2e096dae2e096dae2e096dae2c2e79433c22e092e096dae706f136bed140c624f325219'
    version = 5.103
    domain = 'habr'
    count = 100
    offset = 0
    all_posts = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params=
                                {
                                    'access_token': token,
                                    'v' : version,
                                    'domain' : domain,
                                    'count' : count,
                                    'offset' : offset
                                })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts



def file_writer(all_posts):
    with open( 'ebanphysics.csv','w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes','body','url'))
        for post in all_posts:
            if post['attachments'][0]['type']:
                img_url = 123



all_posts = take_1000_posts()
file_writer(all_posts)
print(1)
