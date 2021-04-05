#convert input to phone nmber format
#to get timezone for phone number
import phonenumbers
from phonenumbers import timezone 

ph_no = phonenumbers.parse("+923096161117")#parsing string to ph.no.

#this will print the country code and national number.
print(ph_no)

tz = timezone.time_zones_for_number(ph_no)#give the time zone for the parsed ph.no.

print(tz)