def example_function(a, b):
    for i in a:
        for j in b:
            if i == j:
                print('this is a lot of indentation')
    for z in b:
        if z == 0:
            print('which level is this? Is this nested')
