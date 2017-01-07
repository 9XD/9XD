import re


def split_tags(tags_text):
    # re.split('a, b c,d', param) -> result: ['a','b','c','d']
    tag_split_regex = ',\s|,|\s'
    return re.split(tag_split_regex, tags_text)
