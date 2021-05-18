def add_time (f, *args, **kwargs):
    import datetime
    def out (*fargs, **fkwargs):
        print (datetime.datetime.now())
        n_f = f (*fargs, **fkwargs)
        return n_f
    return out

def user_adge (name = "Name",adge = "adge"):
    print (f'{name} is {adge} years old')

user_age_with_time = add_time(user_adge)(name = "Name",adge = "adge")

@add_time
def user_adge (name = "Name",adge = "adge"):
    print (f'{name} is {adge} years old')

user_adge ('Anna', 5)
