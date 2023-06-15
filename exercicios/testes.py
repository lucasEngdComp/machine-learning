input_1 = '10:30'

# input_1 = float(input_1)

# print(type(input_1))
# print('Float Value =', input_1)

def convert(data):
    vals,v = (data.split(':'))
    x = vals*60 + int(v)
    print(x)
    t, hours = divmod(float(vals[0]), 24)
    t,minutes = divmod(float(vals[1]),60)
    minutes = minutes / 60.0
    return hours+minutes




value =convert(input_1)
print(value)