# URL Regex

import re

a = re.match('Pr', 'Programe Facil')
print(a.group())
a = re.match('Py', 'Python')
a = re.match('[pP]y', 'Python')
a = re.match('[a-zA-Z]y', 'Python')

a = re.findall('[a-zA-Z]y', 'Python jython Programe Facil')
a = re.findall('[a-zA-Z] [a-zA-Z]', 'Python jython 10')
a = re.findall('[a-zA-Z] [a-zA-Z]+', 'Python jython')
a = re.findall('[a-zA-Z] [a-zA-Z]{1,3}', 'Python jython')
a = re.findall('\w+', 'Python jython')

print(a)


print(re.search(r'^teste[a-z]{2}$', 'testess'))

end = 'www.site.com/clientes/1'
print(re.search(r'clientes/\d+$', end))

print(re.split(r'clientes/(?P<id>\d+)', end))

print(re.split(r'(clientes)/(?P<id>\d+)', end))