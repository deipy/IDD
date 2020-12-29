import requests
import webbrowser
import shutil
from os import walk
from colorama import Fore

it=0
input_filepath=""
output_filepath=""

key = "4a895550-02c6-40db-9ba9-0a4936684d43"

def banner() : 
    print(Fore.RED+" (   (    (    ")
    print(Fore.YELLOW+" )\ ))\ ) )\ )  ")
    print(Fore.YELLOW+"(()/(()/((()/(  ")
    print(Fore.YELLOW+" /(_)/(_))/(_))")
    print(Fore.WHITE+"(_))(_))_(_))_  ")
    print(Fore.RED+"|_ _||   \|   \ ")
    print(Fore.RED+" | | | |) | |) | ")
    print(Fore.RED+"|___||___/|___/ ")
    print(Fore.RED+"        by Deipy")

def ConvertImage(path_in, path_out, count):
    req = requests.post("https://api.deepai.org/api/deepdream", files={'image':open(path_in, 'rb')},headers={'api-key':key})
    try :
        url = req.json()["output_url"]
        r = requests.get(url, stream = True)
        r.raw.decode_content = True
        with open(path_out+"IDP_TEMP_"+str(count)+".png", "wb") as f:
            shutil.copyfileobj(r.raw, f)
        return "IT : "+str(count)+" Done."
    except KeyError :
        print("Server did not respond properly : "+req.json())
        return "ERR"
    
def script() :
    banner()
    print("\n"+Fore.RED+"[?]"+Fore.YELLOW+" How many iterations ? ", end="")
    count = int(input())
    it = count
    print("\n"+Fore.RED+"[?]"+Fore.YELLOW+" Source image filepath : ", end="")
    input_filepath = str(input())
    print("\n"+Fore.RED+"[?]"+Fore.YELLOW+" Source image name : ", end="")
    img_name = str(input())
    print("\n"+Fore.RED+"[?]"+Fore.YELLOW+" Output image filepath : ", end="")
    out_filepath = str(input())
    status = ConvertImage(input_filepath+img_name, out_filepath, 0)
    for i in range(1, it-1):
        print("converting img :"+str(i-1))
        ConvertImage(out_filepath+"IDP_TEMP_"+str(i-1)+".png", out_filepath, i)
script()
