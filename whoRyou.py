import requests
import argparse
from colorama import Fore, Style

EkataApiKey = ""
numVerifyKey = ""

def ekata(number):
    url = "https://api.ekata.com/3.1/phone?api_key=" + EkataApiKey + "&phone=" + number
    info = requests.get(url).json()
    carrier = info['carrier']
    name = info['belongs_to']['name']
    phoneNum = info['phone_number']
    address = info['current_addresses'][0]['street_line_1']
    if address == None:
        address = Fore.RED + "no address found"
    city = info['current_addresses'][0]['city']
    stateCode = info['current_addresses'][0]['state_code']
    postCode = info['current_addresses'][0]['postal_code']
    countryCode = info['current_addresses'][0]['country_code']
    lat = info['current_addresses'][0]['lat_long']['latitude']
    lon = info['current_addresses'][0]['lat_long']['longitude']
    accuracy = info['current_addresses'][0]['lat_long']['accuracy']
    return carrier, name, phoneNum, address, city, stateCode, postCode, countryCode, lat, lon, accuracy

def numVerify(number):
    url = 'http://apilayer.net/api/validate?access_key=' + numVerifyKey + '&number=' + number
    numInfo = requests.get(url).json()
    numCountry = numInfo['country_name']
    numLoc = numInfo['location']
    numCarr = numInfo['carrier']
    numType = numInfo['line_type']
    numType = numInfo['number']
    numValid = numInfo['valid']
    return numCountry, numLoc, numCarr, numType, numValid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="specify number to search [7025555555]")
    args = parser.parse_args()
    number = args.number
    
    carrier, name, phoneNum, address, city, stateCode, postCode, countryCode, lat, lon, accuracy = ekata(number)
    phoneNum = phoneNum.replace('+', '')
    numCountry, numLoc, numCarr, numType, numValid = numVerify(phoneNum)

    
    #print(Fore.YELLOW + "[!] Fetching Data For " + phoneNum)
    print(Fore.BLUE + Style.BRIGHT + "[*] Running NumVerify Scan..")
    print(Fore.CYAN + "[*] Extracting Device Information..")
    if numValid == True:
        #print(Fore.YELLOW + "[!] Valid Phone Number")
        print(Fore.GREEN + "[+] Country: " + numCountry)
        print(Fore.GREEN + "[$] Location: " + numLoc)
        print(Fore.GREEN + "[+] Carrier: " + numCarr)
        print(Fore.GREEN + "[$] Line Type: " + numType)
    else:
        print(Fore.RED + "[-] Invalid Number..")


    print(Fore.BLUE + "[*] Running Ekata Scan.. ")
    print(Fore.GREEN + "[$] Phone Number: " + phoneNum)
    print(Fore.GREEN + "[$] Country Code: " + countryCode)
    print(Fore.GREEN + "[$] City, State: " + city + ", " + stateCode)
    print(Fore.GREEN + "[$] Postal Code: " + postCode)

    print(Fore.MAGENTA + "[!] Personal Information..")
    print(Fore.MAGENTA + "[#] Owner Found: " + name)
    print(Fore.MAGENTA + "[#] Current Address: " + str(address) + ", " + city + ", " + str(stateCode) + " " + str(postCode))
    print(Fore.MAGENTA + "[+] Accuracy: " + accuracy)

    print(Fore.BLUE + "[+] External Suggestions..")
    print(Fore.CYAN + "[?] https://www.idcaller.com/trace.php?phone=" + phoneNum)
    print(Fore.CYAN + "[?] https://m.usa-numbers.com/" + number)
    print(Fore.CYAN + "[?] https://usatelnumber.com/us-number/" + number)
    print(Fore.CYAN + "[?] https://www.numberguru.com/lp/d8937f/2/loading?aff_sub=sb_btn&phone=" + number)
    print(Fore.CYAN + "[?] https://www.searchpeoplefree.com/phone-lookup/" + number)
    print(Fore.CYAN + "[?] https://www.phone.instantcheckmate.com/search?affid=1207&campid=3441&mdm=affiliate&src=VBDA&sid=&s1=Banner&origin=rp&traffic[source]=VBDA&traffic[medium]=affiliate&traffic[campaign]=Banner:&traffic[term]=RPL&traffic[content]=&traffic[funnel]=rpl&phone=" + phoneNum[2:])

    dork_1 = 'https://www.google.com/search?q=intext' + phoneNum[2:] + '&start=0'
    dork_2 = 'https://www.google.com/search?q=allintext:' + phoneNum + '&start=0'

    print(Fore.BLUE + "[*] Google Dork Suggestions..")
    print(Fore.CYAN + "[?] " + dork_1)

    print(Fore.CYAN + "[?] " + dork_2)

if __name__=='__main__':
	main()
