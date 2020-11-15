from googlesearch import search
import os
import argparse
from http import cookiejar
import requests
import random

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

def random_tld(tld_file,current_dir):                                 # select a random tld
    try:
        r_lines = open(tld_file).read().splitlines()
        tld_sel = random.choice(r_lines)
        return tld_sel
    except:
        print("\n")
        print("[+] looks like you lost data in tld.txt file or file may be missing")
        print("[+] don't panic we are here to solve.")
        print("[+] download the tld.txt file from the our github project repository and paste it in " + current_dir + "/bin/ or simply re-clone the project")



def google_search(file, dk, out,tld_file,current_dir):                         #google search function
    if(file==""):
        g_dork=[""]
    else:
        g_dork = open(file)
    for i in g_dork:
        count=0
        flag=0
        while (count <= 6 and flag != 1):
            TLD = random_tld(tld_file,current_dir)
            query = dk + " " + i
            print(query)
            output = open(out, "a")
            print("\n[+] Fetching results for the dork => " + query)
            print("[+] Fetching results using tld => " + TLD)
            output.write("\n[+] Fetching results for the dork => " + query + "\n")
            output.write("[+] Fetching results using tld => " + TLD + "\n \n")
            count+=1                                                                          #This is to ensure to check using 6 different tld if triggered error while search
            try:
                for results in search(query, tld=TLD, num=10, stop=10, pause=random.choice([2, 3, 4])):
                    print(results)
                    output.write(results + "\n")
                flag = 1
            except:
                print("\n[+] Fetching results for the dork => " + query)
                print("[+] Fetching results using tld => " + TLD)
                output.write("\n[+] Fetching results for the dork => " + query + "\n")
                output.write("[+] Fetching results using tld => " + TLD + "\n \n")
                output.close()
        output = open(out, "a")
        print("\n-------------------------------------------------------------------------")
        output.write("\n-------------------------------------------------------------------------")
        output.close()
def main():

    version = 1.3
    current_dir = os.getcwd()

    tld_file = os.path.join(current_dir, "bin/tld.txt")  # Setting the path location for tld file.
    logo_load_loc = os.path.join(current_dir, "bin/logo")
    random_logo = random.choice(os.listdir(logo_load_loc))
    random_logo_file = os.path.join(logo_load_loc, random_logo)  # select random file from the bin/logo directory
    os.system('cat ' + random_logo_file)  # code for printing the logo
    print("\n")
    print("                         Version %.1f\n" % (version))

    s = requests.Session()
    s.cookies.set_policy(BlockAll())

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="File with manually entered dorks")
    parser.add_argument("-o", "--output", type=str, help="Output file name")
    args = parser.parse_args()
    if (args.file is not None):
        output = open(args.output, "w")
        output.close()

    if (args.output is None):  # non empty parameter pass
        print("[+] For help press -h or --help")
        print("[+] Read the documentation from https://github.com/A2hari/Xplore for more help")
        exit()
    if (args.file is not None):
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
        google_search(args.file, dork, args.output,tld_file,current_dir)
    else:
        google_search("", dork, args.output,tld_file,current_dir)

if __name__=="__main__":
    main()