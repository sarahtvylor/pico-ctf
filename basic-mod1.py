def get_flag(flag_array):
    '''
        Funtion takes decoded array of chars from message.
        Outputs flag as string.
    '''
    flag = "".join(flag_array)
    return "picoCTF{"+flag+"}"

def decode_message(msg):
    '''
        Function takes encoded message string.
        Outputs array of decoded chars.
    '''
    msg = msg.split(" ")
    decoded_msg = []

    for value in msg:
        value = int(value) % 37
        if value < 26:
            value += 65
            decoded_msg.append(chr(value))
        elif value == 36:
            decoded_msg.append("_")
        else:
            decoded_msg.append(str(value-26))
    return decoded_msg


print(get_flag(decode_message("202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397")))
