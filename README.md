# About urlprobe
Urlprobe takes URLs from standard input and echos them back if the HTTP result code matches the one supplied the urlprobe.

# Why use urlprobe?
[tomnomnom](https://twitter.com/tomnomnom) created [httpprobe](https://github.com/tomnomnom/httprobe) for probing if a host uses HTTP(S), filtering out hosts without a website. Urlprobe has a slightly different function, it filters out websites with an unwanted HTTP status code.

# Install
Urlprobe should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running urlprobe, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: urlprobe [-h] [-e] [-r <enable | disable | both>] [-s <status_code>] [-t <seconds>]

Test an URL for a HTTP status code and echo the URL back to standard output if it matches a given status
code.

optional arguments:
  -h, --help            show this help message and exit
  -e, --echoredirect    Show which redirects have been found.
  -r <enable | disable | both>, --redirect <enable | disable | both>
                        'enable' enables 301 redirects, 'disable' disables 301 redirects, 'both' tests for
                        both (doubles the amount of queries!). Defaults to 'enable')
  -s <status_code>, --status <status_code>
                        Only show URLs if this/these HTTP status code(s) are returned. Don't enter a code in
                        300 series as this code points to the destination. Separated status codes with a
                        comma. Defaults to 200.
  -t <seconds>, --timeout <seconds>
                        Defines the maximum time to wait before a connection times out. Defaults to 1 second.
```

# Example
Want to run some domains through [waybackurls](https://github.com/tomnomnom/waybackurls) but only want those URLs that give back HTTP status code 200?
```
cat domains.txt | waybackurls |urlprobe
```

# Contribute?
Do you have some usefull additions to the script, please send in a pull request to help make this script better :)
