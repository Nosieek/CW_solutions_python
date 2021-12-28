def convert_lambda_to_def(string):
    string = string.replace(' = lambda ', ':')
    name_f, argv , result = string.split(":")
    pattern = 'def {}({}):\n    return {}'
    return pattern.format(name_f, argv, result)

print(convert_lambda_to_def("act = lambda h: h + ' ' + 'i'"))
#def func(a):\n    return a * 2
'def func(a):\n    return a * 2'
'def func(a):\n    return a * 2'