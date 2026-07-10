# def fund_max_value_list(some_list):
#     max_element = some_list[0]
#     lenght = len(some_list)
#     for element in range(1,lenght):
#         if some_list[element] > max_element:
#             max_element = some_list[element]
#     return max_element
# list_number = [30,40,50,23,56]
# fund_value_in_list = fund_max_value_list(list_number)
# print(fund_value_in_list)

def found_capitalise_letter(some_string):

    capitalize_letter = None
    for ch in some_string:
        if ch.upper() == ch and ch != " ":
            capitalize_letter = ch
            break
    
    if capitalize_letter == None:
        return "no capitalize no found"
    else:
        return "found"+" "+capitalize_letter
r=found_capitalise_letter("H are you")
print(r)




