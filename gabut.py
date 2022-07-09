#usr/bin/python3
# Coding Gabut Joee Dev 🥱
# WhatsApp : 083164279551

# JALAN - JALAN#
def _____jalan2_____(s):
        for c in s + "\n":
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.03)

import os,sys,random,json,requests,getpass,shutil,json,time,subprocess, platform
from time import sleep
from time import strftime as tm
try:
	import requests
except ImportError:
	_____jalan_____('* sedang menginstall modul requests')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	_____jalan_____('* sedang menginstall modul futures')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	_____jalan_____('* sedang menginstall modul bs4')
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	_____jalan_____('* sedang menginstall modul mechanize')
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	catet_mask = ('* sedang menginstall modul rich')
	os.system('pip install rich')
	
_____joee_____ = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=_____joee_____,stderr=subprocess.STDOUT)
_____joee_____.close()
if my_music !=0:
	_____jalan_____('* sedang menginstall play-audio')
	os.system('pkg install play-audio')
	
# WARNA RANDOM #
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

## PERUMPANAN & SYNTAX ###
_____joeenih_____ = print
_____joeeganz_____ = input
_____joeexd_____ = exec
_____joeexxz_____ = os.system("clear")

# INI IP GOBLOK #
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

# JAM & HARI
_____jam_____ = time.strftime("%H:%M:%S")
_____hari_____ = time.strftime("%d/%m/%Y")

# GABUT 🥱
sys.stdout.write('\x1b]2; GABUT BANGET PAK 🥱 \x07')

# LOGO ( LO GOBLOK ) #
def _____logo_____():
    print("")
    _____jalan_____(f"""{H}ooooo         ooooooo     ooooooo8 ooooo oooo   oooo      
 888        o888   888o o888    88  888   8888o  88       
{K} 888        888     888 888    oooo 888   88 888o88       
 {M}888      o 888o   o888 888o    88  888   88   8888       
o888ooooo88   88ooo88    888ooo888 o888o o88o    88{P}""")

def _____wait_____():
    os.system("clear")
    _____joeenih_____("")
    os.popen("play-audio gabut/hello.mp3")
    _____joeenih_____(f"                  {H}* Follow github gwe dulu dong:v{P}");time.sleep(1);os.system('xdg-open https://github.com/JoeDevXX2K');time.sleep(1);_____informasi_____()
    
# KONTOL LU BAU
def _____start_____():
    _____jalan2_____(f"  {P}[{M}!{P}] Sedang mengecek {K}username {P}& {K}password {P}anda")   
    
# USERNAME & PASSWORD #
_____user_____ = "joee"
_____pass_____ = "joee123"

# JALAN - JALAN#
def _____jalan_____(s):
        for c in s + "\n":
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.003)
                
# JALAN - JALAN#
def _____jalan2_____(s):
        for c in s + "\n":
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.03)
                
# INFORMASI #
def _____informasi_____():
    os.system("clear")
    _____logo_____()
    _____joeenih_____("")
    _____joeenih_____(f"{P}* IP Anda :{K} {IP}");time.sleep(1)
    _____joeenih_____(f"{P}* Country : {K}{CN}");time.sleep(1)
    _____joeenih_____(f"{P}* Jam     : {K}{_____jam_____}");time.sleep(1)
    _____joeenih_____(f"{P}* Hari    : {K}{_____hari_____}");time.sleep(1)
    _____joeenih_____("") 
    _____jalan_____(f"{P}* Login {P}untuk melanjutkan\n* ketik {H}open {P}untuk mendapatkan user\n* ketik {H}lanjut{P} jika sudah mempunyai {K}username {P}& {K}password{P}")
    print("")
    _____joeeggwp_____ = _____joeeganz_____(f"* choose : {H}")
    if _____joeeggwp_____ in (""):
      _____jalan2_____(f"{P}* jangan {M}kosong{P}");time.sleep(2);_____informasi_____()
    if _____joeeggwp_____ in ("open","Open","OPEN"):
      _____jalan2_____(f"{P}* anda akan di arahkan ke {H}website {P}untuk mengambil {H}username {P}&{H} password{P}");os.system('xdg-open https://raw.githubusercontent.com/Bot-joe/token/main/user%20%26%20pass.txt');time.sleep(2);_____informasi_____()
    elif _____joeeggwp_____ in ("lanjut","Lanjut","LANJUT"):
        _____jalan2_____(f"{P}* Please Wait....");time.sleep(2);_____masuk_____()
    else:
        _____jalan2_____(f"{P}* pilihan anda {M}salah{P} ");time.sleep(2);_____informasi_____()
                     
# PEMBERSIH #               
def _____clear_____():
    os.system("clear")

# MENU LOGIN #
def _____masuk_____():
        time.sleep(0.5)
        _____clear_____()
        _____logo_____()
        _____joeenih_____("")
        _____joeeusername_____ = input(f"  {P}[{H}•{P}] Username :{H} ")
        _____joeepassword_____ = getpass.getpass(f"  {P}[{H}•{P}] Password : {H}");_____start_____();time.sleep(3)
        if _____joeeusername_____ == _____user_____ and _____joeepassword_____ == _____pass_____:
                _____jalan2_____(f"\n  {P}[{H}✓{P}] Login {H}Successful{P}");time.sleep(2);_____masuk_____()
                print()
        else:
                _____jalan2_____(f"\n  {P}[{M}X{P}] Login {M}Failed{P}");time.sleep(2);exit()

                _____informasi_____()

if __name__=="__main__":
	_____wait_____()

"""
   Follow Github Aing Mang

"""
