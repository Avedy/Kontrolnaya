def isSublist(larger, smaller):
    if smaller[0] == larger[2]:
        return True
    else:
        return False


print(isSublist([4,7,2],[2]))