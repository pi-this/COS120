def age_group_linear_way(age):
    if age < 13:
        result = "child"
    if age > 12 and age < 20:
        result = "teen"
    if age > 19:
        result = "adult"
    return result

"""
def age_group(age):
    if age < 13:
        result = "child"
    if age > 12 and age < 20:
        result = "teen"
    if age > 20:
        result = "adult"
    return result
    
# don't know what result is if age is == 20
"""

def age_group2(age):
    if age < 13:
        result = "child"
    else:
        if age < 20:
            result = "teen"
        else:
            result = "adult"
    return result


def age_group3(age):
    if age < 13:
        result = "child"
    elif age < 20:
        result = "teen"
    else:
        result = "adult"
    return result

def test_age_group():
    for age in [-1, 2, 12, 13, 14, 17.2, 19, 20, 22, 50, 80]:
        print(age, age_group3(age))


