import os, json
os.system("clear")

fi = open('data.json') 

a = ''
for f in fi:
    a += f.strip()

os.system("clear")
jd = json.loads(a)

for j in jd['data']:
    #if "Computer Networking" in j['title']:
    print(j['title'])
    try:
        stru = j['streaming_url']
        #os.system("youtube-dl " + stru)
        print(stru)
    except:
        pass
    print("----")