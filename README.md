# Paste-Hunter
! Hunt those Pastes ! 

### What is PasteHunter ?
PasteHunter is an automated tool to fetch pastes from pastebin to find leaked information, credentials, or any sensitive data which are already crawled by Google.

### So why I created pastehunter ?
So one day while playing with google dorks I ended up searching this particular dork  ```site:pastebin.com intext:some-juicy-info``` From the results I learnt that I can really pull up interesting data from pastebin ( urls, emails, credentials , and many more ) . I found some of my organizational information from there and I reported them to the incident response team. So I thought why dont I automate it ? Well thats the story behind it.

<b> Disclaimer </b>

<b>The author is not responsible if this tool is misused. For educational, awareness or any ethical purpose related use only!</b>

Installation
```
pip3 install -r requirements.txt
```
Usage : ```python3 app.py```
```
mkdir raw
python3 app.py

Starting digging google to find juicy information about site:pastebin.com+intext:smtp.sendgrid.net
Fetching contents of https://pastebin.com/3YrF06Nj
Fetching contents of https://pastebin.com/Vt9viAd9
Fetching contents of https://pastebin.com/87Qsrtni
Fetching contents of https://pastebin.com/Trm7GDXa
Fetching contents of https://pastebin.com/xd0vZqVq
Fetching contents of https://pastebin.com/wq747Fup
Fetching contents of https://pastebin.com/zCGmyqf2
Fetching contents of https://pastebin.com/ggYbteWH
Fetching contents of https://pastebin.com/KT0EErWQ
Fetching contents of https://pastebin.com/btJgmdZE

The pastes will be stored in the raw/ directory
```
