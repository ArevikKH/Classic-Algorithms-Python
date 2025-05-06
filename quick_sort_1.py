def quick_sort(list_):
    if len( list_)<=1:
        return list_
    el =list_[0]
    left = list(filter(lambda x: x < el, list_))
    center =list(i for i in list_ if i == el)
    right = list(filter(lambda x: x>el, list_))
    return quick_sort(left)+center+ quick_sort(right)


arr1 = [64, 34, 25, 12, 22, 11, 90]

print(quick_sort(arr1))
