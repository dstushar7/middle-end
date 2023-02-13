from frontEnd import SearchItems

item_list = 'numbers.txt'
whatToSearch = 'msisdn' 
linkXPath = '/html/body/div/nav[2]/div/div[1]/div/ul/li[2]/a'
credentialPath= 'creds.json'
tagSearch = 'td'
db_credentials_path = 'db_config_main.json'


profile_check = SearchItems(item_list,
                    whatToSearch,
                    credentialPath,
                    linkXPath,
                    tagSearch)

profile_check.search_initiator()

