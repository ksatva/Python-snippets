def spam():
    bacon()
def bacon():
    raise Exception('this is the error message.')

spam()
