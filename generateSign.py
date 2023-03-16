#!/usr/bin/python3
import time
from urllib.parse import urlparse
import hashlib
key = '5GVho4i3KGF4F3Gq'
push_url_str = 'rtmp://push-agora-test.lita.gg/in/lita_2023030913'
play_url_str = 'https://play-agora-test.lita.gg/in/lita_2023030913_ld.flv'
key_expire_time = 60*60
url_push = urlparse(push_url_str)
url_play = urlparse(play_url_str)
now = int(time.time()) + key_expire_time
sign_push = key + url_push.path + str(now)
sign_play = key + url_play.path + str(now)
print(sign_push)
print(sign_play)
md5_push = hashlib.md5()
md5_play = hashlib.md5()
md5_push.update(sign_push.encode('utf-8'))
md5_play.update(sign_play.encode('utf-8'))
push_url_str += "?ts={}&sign={}".format(now, md5_push.hexdigest())
play_url_str += "?ts={}&sign={}".format(now, md5_play.hexdigest())
print(push_url_str)
print(play_url_str)
