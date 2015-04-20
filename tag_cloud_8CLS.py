__author__ = 'tvsamartha'

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts


spam_input_file = open("space_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'space_tagcloud.png', size=(1000, 700), fontname='Neucha')
###

notspam_input_file = open("hardware_output.txt", "r")
text_data = str(notspam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'hardware_tagcloud.png', size=(1000, 700), fontname='Neucha')
###


spam_input_file = open("baseball_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'baseball_tagcloud.png', size=(1000, 700), fontname='Neucha')
###

spam_input_file = open("windows_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=100)

create_tag_image(tags, 'windows_tagcloud.png', size=(1000, 700), fontname='Neucha')
###

spam_input_file = open("politics_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'politics_tagcloud.png', size=(1000, 700), fontname='Neucha')
####


spam_input_file = open("forsale_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=100)

create_tag_image(tags, 'forsale_tagcloud.png', size=(1000, 700), fontname='Neucha')
###


spam_input_file = open("hockey_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'hockey_tagcloud.png', size=(1000, 700), fontname='Neucha')
###

spam_input_file = open("graphics_output.txt", "r")
text_data = str(spam_input_file.readlines())

input_data = text_data.split("\n")
final_str = ""

for line in input_data:
    final_str+=line+" "

tags = make_tags(get_tag_counts(final_str), maxsize=120)

create_tag_image(tags, 'graphics_tagcloud.png', size=(1000, 700),fontname='Neucha')







