import json
def contains_complex_object(data):
    """Recursively check if the parsed JSON data contains complex objects."""
    if isinstance(data,dict):
        for value in data.values():
            if isinstance(value,(dict,list)):
                return True
            if contains_complex_object(value):
                return True
    elif isinstance(data,list):
        for item in data:
            if isinstance(item,(dict,list)):
                return True
            if contains_complex_object(item):
                return True
    return False
json_strings=['{"name":"Anand","age":20}','{"name": "Minnu", "address": {"city": "Rjy", "zip": 533103}}',  
    '{"students": ["Divitha", "Minnu", "Vincy"]}',                  
    '{"id": 1, "value": null}']
for js in json_strings:
    try:
        data=json.loads(js)
        if contains_complex_object(data):
            print(f"JSON :{js} ->contains complex objects")
        else:
            print(f"JSON :{js} ->contains simple objects")
    except json.JSONDecodeError:
        print(f"Invalid JSON:{js}")
