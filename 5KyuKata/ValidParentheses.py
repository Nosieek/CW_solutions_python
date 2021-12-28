def valid_parentheses(string):
    stos = []
    if string.count(')') != string.count('('):
        return False
    for parent in string:
        if parent.isalpha():
            continue
        elif parent == '(':
            stos.append(parent)
        elif parent == ')':
            if not stos:
                return False
            if stos[len(stos)-1] == '(':
                stos.remove('(')
    if not stos:
        return True


print(valid_parentheses('    gf-(()((())))'))