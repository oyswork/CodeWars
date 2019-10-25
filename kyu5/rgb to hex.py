""" The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3 """

def rgb(r, g, b):
    arr = [int(r),int(g),int(b)]
    arr = [ 0 if element < 0 else 255 if element > 255 else element for element in arr]
    arr = [str(hex(element))[2:].upper() for element in arr]
    arr = ''.join(['0'+str(element) if len(element) == 1 else element for element in arr])
    return arr
rgb(148, 0, 211)

""" 
This is a good solution:
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
    And this:
    def rgb(r, g, b): 
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]]) 
"""