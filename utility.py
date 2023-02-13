import json

def take_data_from_json(elementPath,*args):
    f = open(elementPath)
    data = json.load(f)
    f.close()
    return (data[arg] for arg in args)



def output_json_incorporate(filename,exists,notExist):
        json_output = {
            'Exists' : exists,
            "Don't Exist" : list(notExist)
        }
        with open(filename, "w") as outfile:
            outfile.write(json.dumps(json_output))



def getting_search_element(elementPath):
    f = open(elementPath)
    elementPath = list()
    for line in f:
        element = line.rstrip("\n").replace(" ","")
        elementPath.append(element)
    f.close()
    return elementPath
