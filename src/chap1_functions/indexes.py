def return_sum_of_last_5_numbers_without_using_len(numbers):
    return numbers[-5] + numbers[-4] + numbers[-3] + numbers[-2] + numbers[-1]

def return_sum_of_numbers_3_to_10(numbers):
    return sum(numbers[3:10])

def return_part_of_string_without_using_len(message: str):
    if "before" in message:
        return message[0:message.find("before")]
    elif "after" in message:
        return message[message.find("after") + 5:]
    else:
        return message
