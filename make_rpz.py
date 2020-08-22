from __future__ import print_function
import urllib2  # the lib that handles the url stuff


def load_config (filename, array):
   file = open (filename, "r")
   content = file.read()
   array = content.split("\n")
   file.close()
   array=filter(None,array)
   return array

target_url=[]
whitelist=[]
target_url=load_config ('config.rpz', target_url)
whitelist=load_config ('whitelist.rpz', whitelist)

zone_template = """$TTL    604800
@       IN      SOA     localhost.local. hostmaster.local. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      localhost.local.
@       IN      A       127.0.0.1
@       IN      AAAA    ::1
;
"""

print (zone_template)

for url in target_url:
     data = urllib2.urlopen(url) # it's a file like object and works just like a file
     for line in data: # files are iterable
            if not line.startswith('#') and not line.startswith("\n") and line.strip() not in whitelist:
                regel1 = line.rstrip() + " IN CNAME .\n"
                regel2 = "*." + line.rstrip() + " IN CNAME .\n"
                print (regel1, end="")
                print (regel2, end='')

