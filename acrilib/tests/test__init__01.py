__authors__ = """
arnon sela support@acrisel.com
daniel sela daniel@acrisel.com
"""

import re
text = '''__authors__ = """
       arnon sela support@acrisel.com
       """'''
print(text)
#rec = re.compile(r"^__{meta}__[ ]*=[ ]*(('''(?P<text1>.*?)''')|(\"\"\"(?P<text2>.*?)\"\"\"))".format(meta='authors'))
rec = re.compile(r"^__{meta}__[ ]*=[ ]*(('''(?P<text1>(.*\n*)*?)''')|(\"\"\"(?P<text2>(.*\n*)*?)\"\"\"))".format(meta='authors'))
m = rec.search(text)
print(m.group('text2'))

