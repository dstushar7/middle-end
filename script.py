from frontEnd import SearchItems
from backEnd import OracleOperations

item_list = 'numbers.txt'
whatToSearch = 'msisdn' 
linkXPath = '/html/body/div/nav[2]/div/div[1]/div/ul/li[2]/a'
credentialPath= 'creds.json'
tagSearch = 'td'
db_credentials_path = 'db_config_main.json'
oracle_client_dir = r"C:\Users\dabobroto.sarkar\Downloads\instantclient-basic-windows.x64-21.8.0.0.0dbru\instantclient_21_8"



profile_check = SearchItems(item_list,
                    whatToSearch,
                    credentialPath,
                    linkXPath,
                    tagSearch)

numbers = profile_check.search_initiator()

# To Solve issue
oracle_db = OracleOperations(db_credentials_path,
                            oracle_client_dir)

for msisdn in numbers:
    query = "INSERT INTO TBL_BIOMETRIC_TEMP(MSISDN,STATUS) VALUES ("+str(msisdn)+",  '1')"
    oracle_db.execute_query(query)
