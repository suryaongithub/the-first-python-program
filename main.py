import json as j
from xmlrpc.client import boolean

insert_text_in_file=False

with open("./cache/main.json","r") as file:
    global data
    data=file.read()
    file.close()


if '{"array":[' in data:
    insert_text_in_file=True

if insert_text_in_file==True:
    with open("./cache/main.json",'w') as file:
        file.write("{\"array\":[]}")
        file.close

if data.__len__()>0:
    data = data[:-2]


type_of_action = input("do you want to add an element : ")

if type_of_action=="yes":
    
    name = input("your name : ")
    grade = input("your class : ")
    hobby = input("your hobbies : ")
    
    additional_data = """{}
    "Name":{},
    "Class":{},
    "Hobbies":{}
    {}
    """

    name = '"' + name + '"'
    grade = '"' + grade + '"'
    hobby = '"' + hobby + '"'
    
    additional_data = additional_data.format('{',name,grade,hobby,'}')
    insert_comma=False
    with open("./cache/main.json","r") as file:
        if "," in file.read():
            insert_comma="true"
        else:
            insert_comma=False
            

            

with open("./cache/main.json","w") as file:
    if insert_comma == "true":
        file.write(data+"," + additional_data + "]"+"}")
        file.close
    else:
        file.write(data+additional_data+']'+'}')
        file.close
