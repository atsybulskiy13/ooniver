import re
# flake8: noqa
my_string = '''
Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru
'''

result = re.findall(r'[\b\w-]*[^ \s\W]', my_string)

print(result)
