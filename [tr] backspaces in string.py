def clean_string(s):
    donusturulmus_string = ""
    for i in s:
        if i == "#":
            if len(donusturulmus_string) == 0:
                donusturulmus_string = ""
            else:
                donusturulmus_string = donusturulmus_string[0:len(donusturulmus_string)-1]
        else:
            donusturulmus_string = donusturulmus_string + i
        
    return donusturulmus_string
