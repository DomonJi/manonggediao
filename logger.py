def log(o):
    with open('pylog.log','a') as lg:
        lg.write(repr(o)+'\r\n')
