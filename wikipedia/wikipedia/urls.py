from urlparse import urljoin

url = ["/dummyhead"]
newurl = urljoin("http://crap.com", url[0])
print newurl
