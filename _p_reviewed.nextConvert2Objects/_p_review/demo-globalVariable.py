
def spam():
    global eggs #eggs refer to the global variable, so dont create a local variable
    #modification is affected globally in program
    eggs ='spam'

eggs = 'sgge'
spam()
print(eggs)
