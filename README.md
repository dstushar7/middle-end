# Middle End Module
It's a module that works with selenium in the FrontEnd and can connect to a oracle database in the BackEnd. The frontend part can take an items list and can search for it in the desired URL. 
Whereas, the backend can make operations on a database based on the result we get from the frontend.
There is another file that is the Utility module that will hold some common functions that will be essential for us.


## Instructions :
+ Please install requirements first. Create a virtual environment and execute "pip install -r requirements.txt"

+ Download chromedriver.exe for selenium and add in global path.

+ Download instantclient-basic-windows for oracle client.

+ Two JSON file needs to be created. One for frontend, one for the backend. Data Formats are given below :

    + Credentials file for the URL:
        + creds.json :
    {
        "url" : "https://www.facebook.com",
        "username" : "fieldValue",
        "password" : "password"
    }    

    + Database credentials file:
        + db_config.json :
    {
        "dsn" : "database dsn",
        "username" : "",
        "password" : ""
    }

+ The items that we'll search need to be in a file. Each item in a seperate line. 
    + For Example if we need to search numbers in a website, the numbers need to give in separate lines :
     8801833183694
     8801833183720

# Utility :
The utility file holds some common functions which will be regularly used for different operations
+ take_data_from_json(parameter1, multipleParameters)
    + parameter1 represents a json file path, from which we will take data.
    + After parameter1, we can give multiple parameters into function. We will give the key names as string into the function. The function will return a tuple of datas. If we look at our creds.json file. We will fetch url,username,password by:
        + url, username, password = take_input_from_json('creds.json','url','username','password')

+ output_json(param1,param2,param3)
    + param1 will represent a json file name that will come as an output to show any result.
    + param2 will represent the list that represts existence of the "Searched Item of frontend"
    + param3 will represent the list that represts Non-existence of the "Searched Item in frontend"

+ getting_element_from_file(parameter1)
    + parameter1 will be a string containing a txt file where some elements are given seperated by lines. It will return a list of items.

# Front End :