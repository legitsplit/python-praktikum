# Zusammenarbeit mit folgenden Teilnehmern:
def isPermutation(list1, list2):
    if len(list1) != len(list2):
        return False

    variable_list = []
    for i in range(len(list1)):
        variable_list.append(list1[i])

    for i in range(len(list2)):
        found = False
        for j in range(len(variable_list)):
            if list2[i] == variable_list[j]:
                found = True
                del variable_list[j]
                break
        if not found:
            return False
    return True