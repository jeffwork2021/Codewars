# Write a function that when given a URL as a string, parses out just the 
# domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
def domain_name(url):
    ptr = url.find("://")
    s = url[ptr+3:] if ptr > -1 else url
    ptr = s.find("/")
    s = s[0:ptr] if ptr > -1 else s
    token = s.split('.')
    return token[1] if token[0] == 'www' else token[0]

    
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com" ))
print(domain_name("www.cnet.com" ))