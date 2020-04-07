import webbrowser

# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)

# for i in range(10):
#     print(1,2,3, sep=';',end= '')

chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.python.org")