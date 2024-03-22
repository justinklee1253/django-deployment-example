from django import template

register = template.Library() #registers custom tags/filters

@register.filter(name='cut') #

def cut(value, arg): #value from context dictionary
    """
    This cuts out all values of "arg" from the string!
    Cuts out anything placed as a parameter.
    """
    return value.replace(arg, '') #replaces "arg" in the string with empty space?

register.filter('cut', cut) #first parameter is string you use to call the function for template tag,
                            # 2nd one is call to the function