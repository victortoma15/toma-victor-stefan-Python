def count_similarities (*args, **kwargs):
    counter = 0
    for index in args:
        if index in kwargs.values():
            counter = counter + 1
    return counter


print(count_similarities(1, 2, 3, 4, x=1, y=2, z=3, w=5))
