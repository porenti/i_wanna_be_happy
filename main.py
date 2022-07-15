import vk_api
from time import time, ctime, sleep
from config import token as tk
from create_pick import pick

vk_session = vk_api.VkApi(token=tk)
vk_session._auth_token()

pictures = pick()
seconds = time()
t = " ".join(ctime(time()-60).replace(" ",":").split(":")[3:5])
while True:
    if " ".join(ctime(time()).replace(" ",":").split(":")[3:5]) != t:
        t = " ".join(ctime(time()).replace(" ",":").split(":")[3:5])
        pictures.create_time(int(t.split(" ")[0]), str(t.split(" ")[1]))
        vk = vk_session.get_api()
        response_ph = vk.photos.get(count = 1, album_id = 'profile', rev = 1)
        if response_ph ['items']:
            ph_id = response_ph['items'][0]
            ph_response_delete = vk.photos.delete(photo_id = ph_id['id'])

        try:
            upload = vk_api.VkUpload(vk_session)
            photo = upload.photo_profile('time.png')

            response = vk.wall.get(count = 1)

            if response ['items']:
                post = response['items'][0]
                post_response_delete = vk.wall.delete(post_id = post['id'])
        except vk_api.exceptions.Captcha as captcha:
            print(captcha.sid)
            print(captcha.get_url())

    sleep(5)
