valid_rule = {
    "name":{
        "type":str,
        "max":100,
        "min":20
        },
    "age":{
        "type":int,
        "max":50,
        "min":16,
    }
}

data_dict = {"name":"sagar Neupane","age":17}


def validate_max_min(key,data_dict, valid_rule):
    if type(data_dict[key]) == str:
        data = len(data_dict[key])

    if type(data_dict[key]) == int:
        data = data_dict[key]

    if valid_rule[key].get("min") and valid_rule[key].get("max"):
        return valid_rule[key]["min"] < data < valid_rule[key]["max"]
    
    elif valid_rule[key].get("min"):
        return  valid_rule[key]["min"] < data

    elif valid_rule[key].get("max"):
        return  valid_rule[key]["max"] > data

    else:
        return True

# def validate_int(key,data_dict, valid_rule):
#     if valid_rule[key].get("max_value") and valid_rule[key].get("min_value"):
#         return valid_rule[key]["min_value"] < data_dict[key] < valid_rule[key]["max_value"]
    
#     elif valid_rule[key].get("max_value"):
#         return valid_rule[key]["max_value"] < data_dict[key]

#     elif valid_rule[key].get("max_value"):
#         return valid_rule[key]["max_value"] > data_dict[key]
#     else:
#         return True


def validate_dict(data_dict, valid_rule):
    valid = True
    
    for key in valid_rule:
        if data_dict.get(key):
            if valid_rule[key]["type"] == type(data_dict[key]):
                valid = valid and validate_max_min(key, data_dict, valid_rule)
        
        else:
            valid = False
            break

    return valid

print(validate_dict(data_dict, valid_rule))


    
