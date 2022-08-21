def list_return():
    list_of_things = ["Mango", "Banana"]
    # list_of_things = []
    if len(list_of_things) > 0:
        return list_of_things
    else:
        # print(list_of_things)
        return None


# print(list_return())


def check_emply_list():
    if list_return() is not None:
        # print(list_return())
        return list_return()


print(check_emply_list())

