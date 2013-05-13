import re
list = ['a', 'bb', 'ccc', '*.eeeee' ]
print [i for i in list if not re.search('\*', i)]
