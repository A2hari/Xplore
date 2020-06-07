from googlesearch import search
import os
import argparse
from http import cookiejar
import requests
import random
import time

version = 1.2

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

current_dir = os.getcwd()
tld_file = os.path.join(current_dir, "bin/tld.txt")  # Setting the path location for tld file.
logo_load_loc = os.path.join(current_dir, "bin/logo")
random_logo = random.choice(os.listdir(logo_load_loc))
random_logo_file = os.path.join(logo_load_loc, random_logo)  # select random file from the bin/logo directory
os.system('cat ' + random_logo_file)  # code for printing the logo
print("\n")
print("                         Version %.1f\n" % (version))
experience_time = [1, 2, 3]
PAUSE = [3, 4, 5, 6, 7, 8, 9]
s = requests.Session()
s.cookies.set_policy(BlockAll())

def random_tld():  # select a random tld
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
        print("[+] download the tld.txt file from the our github project repository and paste it in " + current_dir + "/bin/")

def google_search(file, dk, out):
    if(file==""):
        g_dork=[""]
    else:
        g_dork = open(file)
    for i in g_dork:
        count=0
        flag=0
        while (count <= 6 and flag != 1):
            TLD = random_tld()
            query = dk + " " + i
            print(query)
            pause_set = 2
            output = open(out, "a")
            print("\n[+] Fetching results for the dork => " + query)
            print("[+] Fetching results using tld => " + TLD)
            output.write("\n[+] Fetching results for the dork => " + query + "\n")
            output.write("[+] Fetching results using tld => " + TLD + "\n \n")
            try:
                for results in search(query, tld=TLD, num=10, stop=10, pause=pause_set):
                    pause_set = random.choice(PAUSE)
                    print(results)
                    output.write(results + "\n")
                flag = 1
            except:
                print("\n[+] Hmmmmm............")
                output.write("\n[+] Hmmmmm............")
                print("[+] looks like we stepped on google captcha")
                output.write("[+] looks like we stepped on google captcha")
                print("[+] trying using another tld")
                count+=1
            if(count == 6):
                print("\n[+] Hmmmmm............")
                output.write("\n[+] Hmmmmm............")
                print("[+] looks like we were by google captcha multiple times")
                output.write("[+] looks like we were by google captcha multiple times")
                print("[+] Try after some time or browse google using the blocked tld and solve google captcha")
                output.write("[+] Try after some time or browse google using the blocked tld and solve google captcha")
                print("[+] For help browse https://github.com/A2hari/Xplore and read readme.md")
                output.write("[+] For help browse https://github.com/A2hari/Xplore")
            output.close()
        print("\n-------------------------------------------------------------------------")
        output.write("\n-------------------------------------------------------------------------")
    g_dork.close()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="File with manually entered dorks")
parser.add_argument("-o", "--output", type=str, help="Output file name")
args = parser.parse_args()
if(args.file is not None):
    output = open(args.output, "w")
    output.close()

if (args.output is None):  # non empty parameter pass
    print("[+] Please Specify -o or --output for saving output file")
    print("[+] For help press -h or --help")
    print("[+] Read the documentation from https://github.com/A2hari/Xplore for more help")
    exit()
if(args.file is not None):
    try:
        if (os.stat(args.file).st_size == 0):
            print("\n[+] " + args.file + " is empty ")
            print("[+] Read the documentation from https://github.com/A2hari/Xplore for more help")
            exit()
    except FileNotFoundError:
        print("[+] No such file or directory :" + args.file)
        print("[+] Read the documentation from https://github.com/A2hari/Xplore for more help")
        exit()

dork = input("Enter the target url/file dork : ")
if (args.file is not None):
    google_search(args.file, dork ,args.output)
else:
    google_search("", dork ,args.output)
