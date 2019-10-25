""" Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, 
a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, 
which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time. """


#year = 31536000s
#day = 86400s
#hour = 3600s
#minute = 60s
from functools import reduce
def format_duration(seconds):
    years = seconds//31536000
    seconds = seconds - 31536000*years
    days = seconds//86400
    seconds = seconds - 86400*days
    hours = seconds//3600
    seconds = seconds - 3600*hours
    minutes = seconds//60
    seconds = seconds - 60*minutes  
    how_many = {'years':years,'days':days,'hours':hours,'minutes':minutes,'seconds':seconds}
    if sum(how_many.values()) == 0:
        print('now')
    else:
        karl = []
        how_many = {k:v for k,v in how_many.items() if v != 0}
        how_many = list(zip(how_many.values(), how_many.keys()))
        for cell in how_many:
            karl.append(list(cell))
        del how_many
        for cell in karl:
            cell[0] = str(cell[0])
            if cell[0] == '1':
                cell[1] = cell[1][:-1]
        if len(karl) == 2:
            karl[0] = karl[0]+['and']
        elif len(karl) == 1:
            pass
        else:

            karl[:-2] = [item + [','] for item in karl][:-2]

            karl[-2] = karl[-2] + ['and']

        karl = reduce(lambda x,y: x+y, karl)
        karl = ' '.join(karl)
        karl = karl.replace(' ,', ',')

        print(karl)

format_duration(103665)

""" YOU IDIOT!!!! This is a good solution:
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0] """
