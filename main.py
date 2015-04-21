#/usr/bin/env python

import urllib2

debug_headers = ("akamai-x-cache-on",
                 "akamai-x-cache-remote-on",
                 "akamai-x-check-cacheable",
                 "akamai-x-get-cache-key",
                 "akamai-x-get-extracted-values",
                 "akamai-x-get-nonces",
                 "akamai-x-get-ssl-client-session-id",
                 "akamai-x-get-true-cache-key",
                 "akamai-x-serial-no")

# This is test use
base_url = r"http://downloadcenter.samsung.com/content/SW/201211/20121129051929115/Samsung_USB_Driver_for_Mobile_Phones_v1.5.14.0.exe"


request = urllib2.Request(base_url)
request_headers = ""

for debug_header in debug_headers:
    request_headers = request_headers + "," + debug_header

request.add_header("Pragma", request_headers[1:])
response = urllib2.urlopen(request)
response_headers = response.info()

for response_header in response_headers:
    if "x-" in response_header and not "x-powered-by" in response_header:
        print response_header, response_headers.getheader(response_header)