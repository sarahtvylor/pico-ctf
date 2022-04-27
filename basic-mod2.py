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
        value = pow(int(value), -1, 41)

        if value < 27:
            value += 64
            decoded_msg.append(chr(value))
        elif value == 37:
            decoded_msg.append("_")
        else:
            decoded_msg.append(str(value-27))
    return decoded_msg


print(get_flag(decode_message("104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377")))
