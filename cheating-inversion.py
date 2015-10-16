def sort_and_count(li, c=0):
    if len(li) < 2: return li, c
    m = len(li) / 2
    l, cl = sort_and_count(li[:m], c)
    r, cr = sort_and_count(li[m:], c)
    return merge(l, r, cl + cr)

def merge(l, r, c):
    result = []
    print l, r
    while l and r:
        s = l if l[0] <= r[0] else r
        result.append(s.pop(0))
        if s == r: c += len(l)
    result.extend(l if l else r)
    return result, c


unsorted_li = []
with open('IntegerArray2.txt', 'r') as f:
    for line in f.readlines():
        unsorted_li.append(line)

sorted_li, count = sort_and_count(unsorted_li)

print count         # 22
