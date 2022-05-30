def is_character_match(string1, string2):
    str1_arr = sorted(list(string1.lower()))
    str2_arr = sorted(list(string2.lower()))
    for i,x in enumerate(str1_arr) :
        if str1_arr[i] != str2_arr[i]:
            return False
    return True