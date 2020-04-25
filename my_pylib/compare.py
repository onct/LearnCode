import requests
import re
from lxml import etree

s ="  n- "
x= re.findall(r"^\s+(.-)\s*",s)
print(len(x))
