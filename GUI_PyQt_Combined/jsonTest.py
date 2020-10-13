import json

with open("GUI_PyQt_Combined/Settings/settings_MASTER.json") as json_file:
    data = json.load(json_file)
    
    print("Root_Directory" in data)