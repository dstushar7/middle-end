from frontend import SearchItems

item_list = 'numbers.txt'
whatToSearch = 'msisdn' 
XPath = '/html/body/div/nav[2]/div/div[1]/div/ul/li[2]/a'
credentialPath= 'creds.json'
tagSearch = 'td'


profile_check = SearchItems(item_list,
                    whatToSearch,
                    credentialPath,
                    XPath,
                    tagSearch)

