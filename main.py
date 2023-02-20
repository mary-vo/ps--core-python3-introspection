i=7
print(int)
print(type(type(i)))

# Determines if its first argument is a subclass of the second
# Second argument can be a single class
# or it can be a tuple of classes
print(issubclass(type, object))
print(type(object))


# Use dir to print attribute and method names for an instance
a = 42
print(dir(a))

#Retrive attribute objects using getattru function
print(getattr(a, 'denominator'))
print(a.denominator)

# Introspect scopes
print(globals())
globals()['tau'] = 6.283185
print(tau)


def report_scope(arg):
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)
print(report_scope(42))


