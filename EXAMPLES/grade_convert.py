# def score_to_letter(grade):
#     if grade < 60:
#         return "F"
#     elif grade < 70:
#         return "D"
#     elif grade < 80:
#         return "C"
#     elif grade < 90:
#         return "B"
#     else:
#         return "A"

# works the same as the top function due to the return keyword
def score_to_letter(grade):
    if grade < 60:
        return "F"
    if grade < 70:
        return "D"
    if grade < 80:
        return "C"
    if grade < 90:
        return "B"
    return "A"

    

print(score_to_letter(95))
print(score_to_letter(30))