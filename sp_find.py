import phonenumbers 
from phonenumbers import carrier 
from phonenumbers import geocoder
num = input('Input Phone Number along with Country code [Eg: +889876543210 (88-country code)] \n')
number = phonenumbers.parse(num, "CH")


def location():
    i = geocoder.description_for_number(number, "en")
    print('LOCATION : ' , i )
    

def sp():
    j = carrier.name_for_number(number, "en")
    print('SERVICE_PROVIDER : ' , j )


location()
sp()
