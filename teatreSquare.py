import math

def teatreSquare(length,width,flag):
    result = math.ceil(length/flag)*math.ceil(width/flag)
    print(result)