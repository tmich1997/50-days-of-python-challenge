# Day 29, Middle Figure

def middle_figure(a, b):
    c = a + b
    d = c.replace(' ', '')
    combined = (a + b)

    if len(d) % 2 == 0:
        return "no middle figure"
    else:
        middle_index = len(d) // 2
        return d[middle_index]

    

first = "make love"
second = "not wars"

func_call = middle_figure(first, second)
print(func_call)