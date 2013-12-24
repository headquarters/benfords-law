#!/usr/bin/env python
import dataset

# connecting to a SQLite database
db = dataset.connect('sqlite:///benfordslaw.db')

# table: frequencies_for_documents(one, two, three, four, five, six, seven, eight, nine, none)
frequencies_for_documents_table = db['frequencies_for_documents']

# table: frequencies_for_links(one, two, three, four, five, six, seven, eight, nine, none)
frequencies_for_links_table = db['frequencies_for_links']

# table: frequencies_for_scripts(one, two, three, four, five, six, seven, eight, nine, none)
frequencies_for_scripts_table = db['frequencies_for_scripts']

# table: frequencies_for_images(one, two, three, four, five, six, seven, eight, nine, none)
frequencies_for_images_table = db['frequencies_for_images']

websites = list(db['website'].all())
links = list(db['asset'].find(type="link"))
scripts = list(db['asset'].find(type="script"))
images = list(db['asset'].find(type="image"))

# gotta be a better way to do this...maybe as a class that maintains these integer counts?
def convert_string_int_to_name(int_as_string):
    if int_as_string == "1":
        return "one"
    elif int_as_string == "2":
        return "two"
    elif int_as_string == "3":
        return "three"
    elif int_as_string == "4":
        return "four"
    elif int_as_string == "5":
        return "five"
    elif int_as_string == "6":
        return "six"
    elif int_as_string == "7":
        return "seven"
    elif int_as_string == "8":
        return "eight"
    elif int_as_string == "9":
        return "nine"
    else:
        # throwing out "0" since it isn't usually a leading digit in base 10
        # and it means an asset was 0 bytes, which means something didn't download properly
        return "none"

def calc_frequencies(dictionary, count):
    # compensate for Python flooring integer division results...why, Python, why?
    count = float(count)
    for key in dictionary:
        dictionary[key] = round((dictionary[key] / count) * 100, 2)

# Warning: the following lines are extremely anti-DRY

# base "template" for dictionary to copy to temp_counts for each run through
integer_counts = dict(one=0, two=0, three=0, four=0, five=0, six=0, seven=0, eight=0, nine=0, none=0)

temp_counts = integer_counts.copy()

count = 0;

for website in websites:
    doc_size = website['doc_size']    
    doc_size_as_string = str(doc_size)    
    # only concerned with leading digits for Benford's Law
    dict_key = convert_string_int_to_name(doc_size_as_string[0])    
    temp_counts[dict_key] += 1
    if dict_key != "none":
        count += 1
    
calc_frequencies(temp_counts, count)

print "Doc count: " + str(count)

frequencies_for_documents_table.insert(temp_counts)

count = 0
temp_counts = integer_counts.copy()

for link in links:
    file_size = link['file_size']
    file_size_as_string = str(file_size)    
    dict_key = convert_string_int_to_name(file_size_as_string[0])    
    temp_counts[dict_key] += 1
    if dict_key != "none":
        count += 1

calc_frequencies(temp_counts, count)

print "Link count: " + str(count)

frequencies_for_links_table.insert(temp_counts)

count = 0
temp_counts = integer_counts.copy()

for image in images:
    file_size = image['file_size']
    if file_size == 43:
        continue
    file_size_as_string = str(file_size)    
    dict_key = convert_string_int_to_name(file_size_as_string[0])    
    temp_counts[dict_key] += 1
    if dict_key != "none":
        count += 1
    
calc_frequencies(temp_counts, count)

print "Image count: " + str(count)

frequencies_for_images_table.insert(temp_counts)

count = 0    
temp_counts = integer_counts.copy()

for script in scripts:
    file_size = script['file_size']
    file_size_as_string = str(file_size)    
    dict_key = convert_string_int_to_name(file_size_as_string[0])    
    temp_counts[dict_key] += 1
    if dict_key != "none":
        count += 1
        
calc_frequencies(temp_counts, count)
    
print "Script count: " + str(count)

frequencies_for_scripts_table.insert(temp_counts)

print "All done."

    
