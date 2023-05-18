def mean_fargs(arg1, arg2, arg3):
    return (arg1 + arg2 + arg3) / 3

def mean_largs(*numbers):
    sum = 0
    for arg in numbers:
        sum += arg

    return sum / len(numbers)

def mean_kwargs(**named_numbers):
    sum = 0
    for key in named_numbers:
        sum += named_numbers[key]

    return sum / len(named_numbers)

def use_callback_with_arg_1_2_3_as_formal_arguments(callback):
    return callback(1, 2, 3)

def use_callback_with_arg_1_2_3_as_linear_arguments(callback):
    args = (1, 2, 3)
    return callback(*args)

def use_callback_with_keyword_arguments_containing_bob_key(callback, bob_value):
    kwargs = {"bob": bob_value}
    return callback(**kwargs)
