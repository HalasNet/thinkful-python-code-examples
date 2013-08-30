
def func():
    return []


def bad_defaults(a=[]):
    a.append('something')
    return a


def bad_defaults2(a=func()):
    a.append('something')
    return a


def good_defaults(a=None):
    a = a or []  # Perhaps more correct: a = a if a is not None else []
    a.append('something')
    return a

print "\nprint bad_defaults():", bad_defaults()
print "print bad_defaults():", bad_defaults()
print "print bad_defaults():", bad_defaults()
print "print bad_defaults(['more']):", bad_defaults(['more'])

print "\nprint bad_defaults2():", bad_defaults2()
print "print bad_defaults2():", bad_defaults2()
print "print bad_defaults2():", bad_defaults2()
print "print bad_defaults2(['more']):", bad_defaults2(['more'])

print "\nprint good_defaults():", good_defaults()
print "print good_defaults():", good_defaults()
print "print good_defaults():", good_defaults()
print "print good_defaults(['more']):", good_defaults(['more'])

