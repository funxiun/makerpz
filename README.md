# makerpz
This Python script creates a BIND9 RPZ (Response Policy Zone) file for blocking trackers and advertisment sites.

The output of this script can be redirected to a file to be included in your BIND9 DNS configuration.

For example:

    python make_rpz.py > /etc/bind/db.srpz.local


Expand your named.conf.option file:

    options {
    
    ...
    ...
    ...

    	response-policy { zone "srpz.zone"; };
    };
    
    zone "srpz.zone" {
    type master;
    file "/etc/bind/db.srpz.local";
    allow-query { any; };
    allow-update { none; };
    };

The file config.rpz contains URLs where public blocklists can be found (in PiHole format).
The file whitelist.rpz contains URLs to be excluded from the blocklist.
