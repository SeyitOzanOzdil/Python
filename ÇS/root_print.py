def root_print(tree):
    for root in tree:
        if type(root) != type([]):
            print root
        else:
            root_print(root)
