__author__ = 'tvsamartha'

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

spam_input_file = open("spam_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

YOUR_TEXT = "A tag cloud is a visual representation for text data, typically\
used to depict keyword metadata on websites, or to visualize free form text."

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'email_spam_tagcloud.png', size=(1000, 700))


notspam_input_file = open("notspam_output.txt", "r")
text_data = str(notspam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'email_notspam_tagcloud.png', size=(900, 600))
