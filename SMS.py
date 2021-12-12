import urllib      # URL functions
import urllib2     # URL functions
 
# Set YOUR TextLocal username
username = "Object detected"
 
# Set YOUR unique API hash (NOT API Key)
# It is available from the docs page
# https://control.txtlocal.co.uk/docs/
apihash = '1234567890abcdefghijklmnopqrstuvwxyz1234'
 
# Set a sender name.
# Sender name must alphanumeric and 
# between 3 and 11 characters in length.
sender = 'RPiSpy'
 
# Set flag to 1 to simulate sending
# This saves your credits while you are
# testing your code.
# To send real message set this flag to 0
test_flag = 1
 
# Set the phone number you wish to send
# message to.
# The first 2 digits are the country code.
# 44 is the country code for the UK
# Multiple numbers can be specified if required
# e.g. numbers = ('447xxx123456','447xxx654321')
numbers = ('447xxx123456')
 
# Define your message
message = 'AN object detected at______'
 
#-----------------------------------------
# No need to edit anything below this line
#-----------------------------------------
 
values = {'test'    : test_flag,
          'username': username,
          'hash'    : apihash,
          'message' : message,
          'sender'  : sender,
          'numbers' : numbers }
 
url = 'https://api.txtlocal.com/send/'
 
postdata = urllib.urlencode(values)
req = urllib2.Request(url, postdata)
 
print('Attempt to send SMS ...')
 
try:
  response = urllib2.urlopen(req)
  response_url = response.geturl()
  if response_url==url:
    print('SMS sent!')
except urllib2.URLError, e:
  print('Send failed!')
  print(e.reason)

