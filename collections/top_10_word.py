import re
from collections import Counter

words = re.findall('\w+', open('top_10_word.py').read().lower())
print Counter(words).most_common(10)
