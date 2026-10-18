def xyz_there(str):
    skip_count = 0
    for i in range(len(str)):
        if skip_count > 0:
            skip_count -= 1
            continue
        if str[i] == ".":
            skip_count = 1
            continue
        
        if str[i:i+3] == "xyz":
            return True
        
    return False

