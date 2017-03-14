# -*-encoding: utf-8-*-

#def forloop(current, max, bodyfunc, mutator, *bodyfunc_args):
#    if current < max:
#        bodyfunc(bodyfunc_args)
#        forloop(mutator(current), max, bodyfunc, mutator, bodyfunc_args)
#        
#def forloop(current, max, bodyfunc, mutator, *bodyfunc_args):
#    if current < max:
#        bodyfunc(*bodyfunc_args)
#        forloop(mutator(current), max, bodyfunc, mutator, *bodyfunc_args)
#        

def forloop(current, max, body_func, mutator, *body_func_args):
    if current < max:
        body_func(current, *body_func_args)
        forloop(mutator(current), max, body_func, mutator, *body_func_args)

for_ = forloop

def if_else(condition, thenbody, elsebody):
    if condition():
        thenbody()
    else:
        elsebody()

class CondObj(object):
    def __init__(self, condition):
        self.condition = self.__check_and_eval_condition(condition)
        self.__state = 1
        self.__prev = 'if'
        self.__is_exec = False

    def __check_and_eval_condition(self, condition):
        eval_cond = None
        if hasattr(condition, '__call__'):
            eval_cond = condition()
        elif isinstance(condition, bool) or \
             hasattr(condition, '__bool__') or \
             hasattr(condition, '__len__'):
            eval_cond = condition
        else:
            raise Exception('Condition must be type bool or function return bool type')
        return eval_cond

    def __check_sequence(self, prev):
        return True if self.__prev == prev else False
        
    def __check_callable(self, obj):
        return True if hasattr(obj, '__call__') else False

    def then_(self, thenbody, *args):
        if (not self.__check_sequence('if') and \
            not self.__check_sequence('elif')):
            raise Exception("Before then must be if")
        # Если условие истина и не было исполнения функции раньше
        if self.condition and not self.__is_exec:
            thenbody(*args)
            self.__is_exec = True

        self.__state += 1
        self.__prev = 'then'

        return self

    def elif_(self, condition):
        if not self.__check_sequence('then'):
            raise Exception('Before elif must be then')
        
        self.condition = self.__check_and_eval_condition(condition)
        self.__state += 1
        self.__prev = 'elif'

        return self

    def else_(self, elsebody, *args):
        if not self.__check_sequence('then'):
            return Exception('Before elif must be then')

        if not self.__is_exec:
            elsebody(*args)
            self.__is_exec = True

        self.__state += 1
        self.__prev = 'else'

        return None

    то = then_
    иначе_если = elif_
    иначе = else_

def if_(condition):
    condObj = CondObj(condition)
    return condObj

если = if_




#-----------------------------------------
a = 'параметр из замыкания'
если(False).\
    то(print, "если правда").\
иначе_если(False).\
    то(print, "иначе если правда").\
иначе(lambda x, y, z: print(x, y, z, a), "иначе", 'проверка', "аргументов")


if_else(lambda: True, lambda: print(a), lambda: print('Другое сообщение'))

если([]).\
    то(lambda: print('test1')).\
иначе_если(lambda: True).\
    то(lambda: print('test2')).\
иначе(lambda: print('test3'))

"""
a = 42

if_(lambda: a == 42)\
    .then_(lambda: print('a equal {}'.format(a)))\
    .else_(lambda: print('a not equal 42'))


if_(a == 43)\
    .then_(lambda: print('a = 43'))\
.elif_(a == 44)\
    .then_(lambda: print('a == 44'))\
.else_(lambda: print('a == {}'.format(a)))


ifelse(lambda: a == 42, 
    lambda: print('a = {}'.format(42)), 
lambda: print('not 42'))
"""


def append(l1, l2):
    if not l1:
        return l2
    if l2:
        l1.append(l2[0])
        append(l1, l2[1:])
    return l1