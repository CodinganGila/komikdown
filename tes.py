import re
import os
import time
import glob
import requests
from pypdf import *
from fpdf import FPDF
from bs4 import BeautifulSoup 


"""
DONE: Remove PDF and IMG from they each folder.
DONE: Name the output after the comic and assign with chapter.
TODO: Speed up the download process.
TODO: Add menu.
        1. Account.
        2. Hot Update.
        3. Bookmark.
        4. Search Comic.
TODO: Neat the code with PEP8.
TODO: Add explaination with comment.
TODO: Incoperate new tehnique.
TODO: Hide PDF and IMG folder.
TODO: Ask user for desired path ouput.
TODO: Done.
"""

def clearScreen():
    os.system("clear")
    ...

def testing(link: str):
    req = requests.get(link).text
    soup = BeautifulSoup(req, 'html5lib')
    return soup
    ...

def scrape(link: str, args):
    for tes in testing(link).select(f"{args}"):
        # print(tes.text)
        lir = tes.text
        return lir
        ...
    ...

def scrape_genres(link: str, args):
    for tes in testing(link).select(f"{args}"):
        print(tes.text, end=" ")
        ...
    ...

def download_chapters(ch,link):
    time.sleep(5)
    print(f"Donwloading part of {ch.index(link)}", end="", flush=True)
    img = requests.get(link, headers=header).content
    if not os.path.exists('./img'):
        os.mkdir('./img')
        file = os.path.join('./img', f'img{ch.index(link)}.jpg')
        with open(file, 'wb') as f:
            f.write(img)
            print(f"\rDonwloading part of {ch.index(link)}.jpg Done..")
    elif os.path.exists('./img'):
        file = os.path.join('./img', f'img{ch.index(link)}.jpg')
        with open(file, 'wb') as f:
            f.write(img)
            print(f"\rDownloading part of {ch.index(link)} Done..")

def remove_file(files):
    file = glob.glob(files)
    for f in file:
        os.remove(f)

def pdf_mergers(input):
    merger = PdfMerger()
    for i in os.listdir('./pdf'):
        merger.append(f"./pdf/img{os.listdir('./pdf').index(i)}.pdf")
    merger.write(f'{input}.pdf')
    merger.close()
    

clearScreen()

infosClass = [
        "h1.heading",
        "div.d-cell-small.value.authors",
        ['.genres .text_0'],
        "div.d-cell-small.value.status.ongoing",
        "div.d-cell-small.value.new_chap",
        ".d-cell-small.value.updateAt",
        ".summary p"
        ]

infoDesc = [
    "Alt name(s):",
    "Author(s) / Artist(s):",
    "Genres:",
    "Status:",
    "Latest chapter(s):",
    "Update at:",
    f"Description: \n"
    ]


header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Host' : 'mangakatana.com',
    'Referer' : 'https://mangakatana.com/',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : 'PHPSESSID=nbtm1alu0dadgtu34aqtapmmh4; sgn_token=AvPYSvwU7YstEzVYYO%2Fe6E0r5ekQT63BgXkLEpgENHuK6YC%2BENwY4Gg5ouLO88USE05QNITlENTyw7rzg4OnxQ%3D%3D; hb_insticator_uid=29dc97f1-9e54-4226-821f-f0095e119a1d; AdskeeperStorage=%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2Fmangakatana.com%2F%22%2C%22svsds%22%3A30%7D%2C%22C1448428%22%3A%7B%22page%22%3A1%2C%22time%22%3A1684835441507%7D%2C%22C1468109%22%3A%7B%22page%22%3A1%2C%22time%22%3A1685002831627%7D%2C%22C1468108%22%3A%7B%22page%22%3A7%2C%22time%22%3A1685008088017%7D%7D; page_loaded={"25479_c1":1,"25951_c216":1,"24816_c29":20,"19588_c73":13,"25803_c129":2,"26083_c87":71}; atk99=2'
}

mangaName = []
dataID = []
links = []
genres = []
info = []
linkComic = []



res = testing("https://mangakatana.com")

remove_file('img/*')
remove_file('pdf/*')

while True:

    for name,data in zip(res.select("#hot_update .uk-container.uk-container-center .title"),res.select("#hot_update .uk-container.uk-container-center div[data-id]")):
        resD = name.text
        resClean = resD.lstrip()
        mangaName.append(resClean)
        dataID.append(data["data-id"])
        ...
    
    for link in res.select("#hot_update .uk-container.uk-container-center .title a"):
       links.append(link["href"])
       ...
        
    for key,(name,data) in enumerate(zip(mangaName, dataID)):
       print(f"{key+1}. {name}", flush=True)
       ...
    
    choice = int(input("choose manga: "))-1
    if choice < len(mangaName):
        menuRes = testing(links[choice])
        #print(testing(menuRes))

        clearScreen()

        for key, value in zip(infoDesc,infosClass):
            
            ...

        for infos in infosClass:
            if isinstance (infos, list):
                for items in menuRes.select(infos[0]):
                    genres.append(items.text)
            else:
                for items in menuRes.select(infos):
                    info.append(items.text)
                    ...

        info_result = info[:2] + [genres] + info[2:]
        for nameDesc, descDesc in zip(infoDesc,info_result):
            if isinstance (descDesc, list):
                genre_str = " | ".join(descDesc)
                print(f"{nameDesc} {genre_str}")
            else:
                print(f"{nameDesc} {descDesc}")


        for link in menuRes.select(".chapters .chapter a"):
            linkComic.append(link["href"])

            reversedList = linkComic[::-1]
            #linkComic.reverse()

        choice = int(input("choose chapter to downloaded: "))

        clearScreen()


        if choice < len(reversedList):

            soup = testing(reversedList[int(choice)-1])

            token =  r"https://i1\.mangakatana\.com/token/\S+"
            #token =  re.compile(r"https://i1\.mangakatana\.com/token/\S+")

            chapter = []

            for script in soup.select('script[type="text/javascript"]', text=token):
                    res = str(script.string)
                    #print(res)
                    match = re.findall(token, res)
                    #print(match)
                    #match = re.findall(token, script.text)
                    
                    for link in match:
                        if match:
                            link = re.sub(r"https://i1.mangakatana.com/token/6bd2cf928010764658p98%3At%3A732.459p29-7c160w%3Ao%3A0q8%3A9q4458009o0/0.jpg',];", '', link)
                            tes = re.sub(r'];function', '', link)
                            chapter.append(tes)

        
        if os.path.exists('./pdf'):
                pass
        else:
                os.mkdir('./pdf')
            
        chapter = chapter[-1]
        chapter = chapter.split(',')
        chapter = [str(item).replace('"', '') for item in chapter if str(item)]
        clean_chapters = []
        for link in chapter:
                link = link.replace("'", '')
                clean_chapters.append(link)
        for link in clean_chapters:
            if not os.path.isfile(f'./img/img{clean_chapters.index(link)}.jpg'):
                    download_chapters(clean_chapters, link)
                    pdf = FPDF(unit='mm')
                    pdf.add_page()
                    pdf.image(f'./img/img{clean_chapters.index(link)}.jpg',x=0, y=0, w=210,h=297)
                    pdf.output(f'./pdf/img{clean_chapters.index(link)}.pdf','F')
                    pdf_mergers(f"{info_result[0]} {choice}")
            else:
                    pdf = FPDF(unit='mm')
                    pdf.add_page()
                    pdf.image(f'./img/img{clean_chapters.index(link)}.jpg',x=0, y=0, w=210,h=297)
                    pdf.output(f'./pdf/img{clean_chapters.index(link)}.pdf','F')

    # Clearing the files
    remove_file('img/*')       
    remove_file('pdf/*')       


        #link_download = input(f"\nenter chapter: ")
        #print(link_download)

    break

    ...

    

