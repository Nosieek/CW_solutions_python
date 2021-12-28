def validate_code(code):
    return True if str(code).startswith(('1', '2', '3')) else False


print(validate_code(348))
