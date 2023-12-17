def list_items(aList):
    for index, item in enumerate(aList):
        if index < (len(aList)-1):
            print(item, end=', ')
        else:
            print('and ' + item)


spam = ['apple', 'bananas', 'tofu', 'cats']
spam2 = []
#list_items(spam)
list_items(['non'])