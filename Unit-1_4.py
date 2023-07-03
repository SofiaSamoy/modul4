def polindrom (str):
    str_rev = str[::-1]
    if str == str_rev:
        print('True')
    else:
        print('False')

polindrom ('lkjhhjkl')
polindrom ('asdfgh')