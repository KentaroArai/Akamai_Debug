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

base_url = r"http://downloadcenter.samsung.com/content/SW/201211/20121129051929115/Samsung_USB_Driver_for_Mobile_Phones_v1.5.14.0.exe"

for debug_header in debug_headers:
    header = {"Pragma" : debug_header}
    request = urllib2.Request(base_url, headers=header)
    response = urllib2.urlopen(request)
    print debug_header

    response_headers = response.info()

    #print response_headers

    for response_header in response_headers:
        if "x-" in response_header and not "x-powered-by" in response_header:
            print response_header, response_headers.getheader(response_header)

    print ''