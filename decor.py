__author__ = 'patriot'

def decfoo(afootodec):
    def wrapper():
        print "wrapper code before"
        afootodec()
        print "wraper code after"
    return wrapper

@decfoo

def alonefoo():
    print "im a single foo"

alonefoo()

