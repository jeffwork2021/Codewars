# Complete the function/method so that it returns the url with anything after # 
# the anchor (#) removed.
# Examples
#
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"
def remove_url_anchor(url):
    a = url.find('#')
    return url[:a] if a>=0 else url

    


print(remove_url_anchor("www.codewars.com#about"))
