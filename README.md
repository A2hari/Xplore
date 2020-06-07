# Xplore
![GitHub](https://img.shields.io/badge/Version-1.2-blue)
![GitHub](https://img.shields.io/badge/Platform-Unix%20%7C%20Linux-brightgreen)
![GitHub](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.8%2B-orange)

## Introduction
Information Gathering is one of the most important phase in the penetration testing, and Google dorks has its own identification mark in the information gathering. Google dorking multiple queries for findinding a companies/website juicy information is very boring task,time consuming and difficult task. Here is a solution for that, **Xplore** an advanced google dork search tool. **Xplore** is coded in such a way it browsers queries in a random pattern making bot pattern detection difficult.I built this project keeping easy use, time, and security in mind. Xplore is more powerful with the combination of [GHDB](https://www.exploit-db.com/google-hacking-database)

Lazy to update the the google-dorks manually... Don't worry we are working on it and we will update it soon. stay tuned to this project for further updates and information 
## Install

The install process is same for all the platforms. The installation process is very easy 

<h3>1. Clone Repository</h3>

> git clone https://github.com/A2hari/Xplore.git

<h3>2. Change Directory</h3>

> cd Xplore

<h3>3. Install Requirements </h3>

> pip3 install -r requirements.txt

<h3>4. Run </h3>

> python3 xplore.py

Tada... You successfully run Xplore in your systen

## Platform
**Xplore** supports all the platforms and all the devices where python 3.8 runs so it is a platfom independent project

## Usage
Usage of Xplore is very simple. No Complex knowledge of google dorks is need. 
<h4> Here are the steps for using this Software</h4>

1. Add the google dorks form ghdb to the google-dork.txt and save it.

![google-dorks](https://user-images.githubusercontent.com/40531762/82412148-bc19d880-9a90-11ea-926c-de53327357f8.png)

Don't panic if you dont find 'google-dorks.txt' just run the script it creates one for you

2. run the script it asks for dork/url, Here you can give your target website dork 
![dork](https://user-images.githubusercontent.com/40531762/82413423-eec4d080-9a92-11ea-876d-2b48f483fb2b.png)

![dork2](https://user-images.githubusercontent.com/40531762/82413476-09974500-9a93-11ea-8d68-3c886e79474a.png)

Feeling that the software is working slow. we wantnedly made the software slow to avoid pattern detection and protect you from ip block. if you block your ip read Warnings and error.

3. Wanna save the results in a text file we do that for you after the script executed you find a file named loot.txt on the directory in that file the report will be autometically saved.

Note: For every scan the loot.txt will be deleted and created newly so please after the scan cut or copy file and store it before scan data is lost

## Errors & Warnings
1. If you found the folling error
```
>> [+] /Input/google-dorks.txt is empty add some dorks in  file to use the tool
>> [+] Read the documentation from https://github.com/A2hari/Xplore 
```
This error occures if the `google-dork.txt` file  is empty or if `google-dork.txt` went missing. if went missing no problem the script autometicall generates one if you run the script. to avoid this error add some google dorks form [ghdb](https://www.exploit-db.com/google-hacking-database) or your own dorks. This solves the error.

2. If you found The following error
```
[+] Fetching results for the dork =>  inurl:"index.php?option=com_fabrik"
[+] Fetching results using tld => vu

[+] Hmmmmm............
[+] looks like we stepped on google captcha
[+] browse google.vu in your browser and type any dork if found captcha solve it to unblock your ip 
[+] For help browse https://github.com/A2hari/Xplore and read readme.md
[+] trying using another tld

 
[+] Fetching results for the dork =>  inurl:"index.php?option=com_fabrik"
[+] Fetching results using tld => sc

[+] Hmmm.......... 
[+] check your internet connection... and google.scin your browser
[+] Looks like we stepped on google captcha
[+] Google is blocking requests form this ip 
[+] Dont panic we are here to slove this
[+] solve the captcha manually solves this error refer Xplore github page
[+} For help browse https://github.com/A2hari/Xplore
[+] Try re-running the script for the dork =>  inurl:"index.php?option=com_fabrik"

```
Here are the following reasons for getting this error

<h4>1. Google Captcha :-</h4>
If Xplore hit with a google captcha or if google block your ip address you find this error. If you even don't have active internet connection you have this error. 
<br>
Ip block by google...! Dont panic it's just a google captcha. we have a solution it's a temporary block go to the google websie using the tld where your ip is blocked or hit with captcha. 
 `EX: If i got this error on google.com.uk` Navigate to google.com.uk in your browser and search anything using google dork
 if google captcha appeares solve it else leave your ip will be free form that tld after few minutes
 <h4>2. Internet Connection</h4>
 check weather you have stable Internet connection or not..

## Support
 
<a href="https://www.buymeacoffee.com/hari" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


you can also donate bat tokens... :)
