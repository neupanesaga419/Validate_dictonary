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

data_dict = {"name":"Mero","age":55}


def validate_string(key,data_dict, valid_rule):

    if valid_rule[key].get("min_len") and valid_rule[key].get("max_len"):
        if  valid_rule[key]["min_len"] < len(data_dict[key]) < valid_rule[key]["max_len"]:
            return True
        else:
            return False
    
    elif valid_rule[key].get("min_len"):
        if  valid_rule[key]["min_len"] < len(data_dict[key]):
            return True
        else:
            return False

    elif valid_rule[key].get("max_len"):
        if  valid_rule[key]["max_len"] > len(data_dict[key]):
            return True
        else:
            return False
    else:
        return True

def validate_int(key,data_dict, valid_rule):
    if valid_rule[key].get("max_value") and valid_rule[key].get("min_value"):
        if  valid_rule[key]["min_value"] < data_dict[key] < valid_rule[key]["max_value"]:
            return True
        else:
           return False
    
    elif valid_rule[key].get("max_value"):
        if  valid_rule[key]["max_value"] < data_dict[key]:
            return True
        else:
            return False

    elif valid_rule[key].get("max_value"):
        if  valid_rule[key]["max_value"] > data_dict[key]:
            return True
        else:
            return False
    else:
        return True


def validate_dict(data_dict, valid_rule):
    valid = True
    for key in data_dict:
        if valid_rule.get(key):
            if valid_rule[key]["type"] == type(data_dict[key]):
                if type(data_dict[key]) == str:
                   valid = valid and validate_string(key,data_dict, valid_rule)
                
                if type(data_dict[key]) == int:
                    valid = valid and validate_int(key,data_dict, valid_rule)

    return valid



print(validate_dict(data_dict, valid_rule))


    
