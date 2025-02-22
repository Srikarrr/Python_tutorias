def create_list():
    return []


def add_element(mylist,element):
    mylist.append(element)
    return mylist


def remove_element(mylist,element):
    for ele in mylist:
         if(ele == element):
               mylist.remove(element)
