# �������������� ��������� � ����������� �������� �� �����
# �������������� �� ����� �������� ���������.
# ��� ������� �������� ������ ���������� RecursionError: maximum recursion depth exceeded
def reverse(iterator):
    for i in iterator:
        yield from reverse(iterator)
        yield i

def reverse(iterator):
    i = next(iterator)
    yield from reverse(iterator)
    yield i
    
def reverse(iterator):
    i = next(iterator)
    yield reverse(iterator)
    yield i

# ���������� �������� (������� �� ������ � �����), ������ �������������
gen = reverse(iter(range(1, 100))) 
list(gen)

make_list = [i ** 2 for i in range(1, 10)]   # ���������� ��������� � ������
make_generator = (i ** 2 for i in range(1, 10)) # �������� ��� ���������


# ���������� ������ � ������� ��������
def reverse2(arr_in, arr_out):
    if not arr_in:
        return
    el = arr_in.pop(0)
    reverse2(arr_in, arr_out)
    arr_out.append(el)

def reverse2(input_array, output_array):
    if input_array:
        first_element = input_array.pop(0)
        reverse2(input_array, output_array)
        output_array.append(first_element)

# ������� ����������
def my_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

# ���������� ��� ������ (� �������������� �����)
def my_sort(array):
    # ��������� ������� ��� ����� for 
    def forloop(current, max, bodyfunc, mutator, *bodyfunc_args):
        if current < max:
            bodyfunc(current, *bodyfunc_args)
            forloop(mutator(current), max, bodyfunc, mutator, *bodyfunc_args)
    
    def ifelse(condition, thenbody, elsebody):
        if condition():
            thenbody()
        else:
            elsebody()
    
    def inc(x):
        return x + 1

    def change(j, i, array):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

    forloop(1, len(array), 
           lambda i: forloop(0, i, 
                        lambda j: change(j, i, array),
                        inc(j)),
           inc(i))
