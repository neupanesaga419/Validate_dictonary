valid_rule = {
    "name":{
        "type":str,
        "max_len":100,
        "min_len":20
        },
    "age":{
        "type":int,
        "max_value":50,
        "min_value":16,
    }
}

data_dict = {"name":"sagar Neupane ","age":45}


def validate_string(key,data_dict, valid_rule):

    if valid_rule[key].get("min_len") and valid_rule[key].get("max_len"):
        return valid_rule[key]["min_len"] < len(data_dict[key]) < valid_rule[key]["max_len"]
    
    elif valid_rule[key].get("min_len"):
        return  valid_rule[key]["min_len"] < len(data_dict[key])

    elif valid_rule[key].get("max_len"):
        return  valid_rule[key]["max_len"] > len(data_dict[key])

    else:
        return True

def validate_int(key,data_dict, valid_rule):
    if valid_rule[key].get("max_value") and valid_rule[key].get("min_value"):
        return valid_rule[key]["min_value"] < data_dict[key] < valid_rule[key]["max_value"]
    
    elif valid_rule[key].get("max_value"):
        return valid_rule[key]["max_value"] < data_dict[key]

    elif valid_rule[key].get("max_value"):
        return valid_rule[key]["max_value"] > data_dict[key]
    else:
        return True


def validate_dict(data_dict, valid_rule):
    valid = True
    
    for key in valid_rule:
        if data_dict.get(key):
            if valid_rule[key]["type"] == type(data_dict[key]):
                if type(data_dict[key]) == str:
                    valid = valid and validate_string(key,data_dict, valid_rule)
                
                if type(data_dict[key]) == int:
                    valid = valid and validate_int(key,data_dict, valid_rule)
        
        else:
            valid = False
            break

    return valid

print(validate_dict(data_dict, valid_rule))


    
