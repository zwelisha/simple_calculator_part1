def add(*args):
    sum_args = 0
    for num in args:
        sum_args += num
    return sum_args

def multiply(*args):
    args_product = 1
    for num in args:
        args_product *= num
    return args_product
