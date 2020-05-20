from googlesearch import search
import os
from http import cookiejar
import requests
import random
import time

version = 1.1

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

def random_tld():  # a function to check the tld working weather all the tld's are working or need to be edited
    try:
        r_lines = open(tld_file).read().splitlines()
        tld_sel = random.choice(r_lines)
        return tld_sel
    except:
        print("\n")
        print("[+] loooks like you lost data in tld.txt file or file may be missing")
        time.sleep(random.choice(experience_time))
        print("[+] don't panic we are here to solve.")
        time.sleep(random.choice(experience_time))
        print("[+] download the tld.txt file from the our github project repository and paste it in "+current_dir+"/bin/")

current_dir = os.getcwd()
dork = open("google-dorks.txt","a")   # by any chance the dork file get deleted then, this line of code create one file of same name.
dork.close()
output = open('loot.txt',"w")
output.close()

tld_file = os.path.join(current_dir, "bin/tld.txt")   # Setting the path location for tld file.
logo_load_loc = os.path.join(current_dir,"bin/logo")
random_logo = random.choice(os.listdir(logo_load_loc))
random_logo_file = os.path.join(logo_load_loc,random_logo)        #select random file from the bin/logo directory
os.system(('type '+ random_logo_file) if os.name == 'nt' else ('cat ' + random_logo_file))  # code for printing the logo
print("\n")
print("                         Version %.1f"%(version))
experience_time = [1, 2, 3]
PAUSE = [ 3, 4, 5, 6, 7, 8, 9]
inital_pause = [5, 6, 7, 8, 9, 10]
s = requests.Session()
s.cookies.set_policy(BlockAll())

if (os.stat("google-dorks.txt").st_size == 0):
    time.sleep(random.choice(experience_time))
    print("\n[+] /Input/google-dorks.txt is empty add some dorks in  file to use the tool")
    print("[+] Read the documentation from https://github.com/A2hari/Xplore ")
    exit()

url = input("[+] Entet the dork/url ->  ")
g_dork = open("google-dorks.txt", "r")
for i in g_dork:
    TLD = random_tld()
    query = url + " " + i
    pause_set = random.choice(inital_pause)
    output = open("loot.txt","a")
    print("\n \n[+] Fetching results for the dork => " + query)
    print("[+] Fetching results using tld => " + TLD )
    output.write("\n[+] Fetching results for the dork => " + query+"\n")
    output.write("[+] Fetching results using tld => " + TLD + "\n \n")

    try:
        for results in search(query, tld= TLD, num=10, stop=10, pause=pause_set):
            pause_set = random.choice(PAUSE)
            print(results)
            output.write(results+"\n")

    except:
        print("\n[+] Hmmmmm............")
        output.write("\n[+] Hmmmmm............")
        print("[+] looks like we stepped on google captcha")
        output.write("[+] looks like we stepped on google captcha")
        print("[+] browse google."+TLD+" in your browser and type any dork if found captcha solve it to unblock your ip ")
        output.write("[+] browse google."+TLD+" in your browser and type any dork if found captcha solve it to unblock your ip ")
        print("[+] For help browse https://github.com/A2hari/Xplore and read readme.md")
        output.write("[+] For help browse https://github.com/A2hari/Xplore")
        print("[+] trying using another tld")
        TLD = random_tld()
        pause_set = random.choice(inital_pause)
        print("\n \n[+] Fetching results for the dork => " + query)
        print("[+] Fetching results using tld => " + TLD)
        output.write("\n[+] Fetching results for the dork => " + query + "\n")
        output.write("[+] Fetching results using tld => " + TLD + "\n \n")

        try:
            for results in search(query, tld= TLD, num=10, stop=10, pause=pause_set):
                pause_set = random.choice(PAUSE)
                print(results)
                output.write(results+"\n")
        except:
            print("\n[+] Hmmm.......... ")
            output.write("\n[+] Hmmm.......... " + "\n")
            time.sleep(1)
            print("[+] check your internet connection... and google." + TLD + "in your browser")
            output.write("[+] check your internet connection... and google." + TLD +"in your browser" +"\n")
            time.sleep(1)
            print("[+] Looks like we stepped on google captcha")
            output.write("[+] Looks like we stepped on google captcha" + "\n")
            time.sleep(1)
            print("[+] Google is blocking requests form this ip ")
            output.write("[+] Google is blocking requests form this ip " + "\n")
            time.sleep(1)
            print("[+] Dont panic we are here to slove this")
            output.write("[+] Dont panic we are here to slove this" + "\n")
            time.sleep(1)
            print("[+] solve the captcha manually solves this error refer Xplore github page")
            output.write("[+] solve the captcha manually solves this error refer Xplore github page" + "\n")
            print("[+} For help browse https://github.com/A2hari/Xplore")
            output.write("[+} For help browse https://github.com/A2hari/Xplore")
            time.sleep(1)
            print("[+] Try re-running the script for the dork => "+ query)
            output.write("[+] Try re-running the script for the dork => "+ query + "\n")
g_dork.close()
output.close()
