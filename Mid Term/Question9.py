# Write a profgram to convert a list of tuple(e.g[(1, 'a'), (2, 'b')]) into a dictionary and then sort the dictionary by its keys.
def convert_and_sort_dict(tuple_list):

    my_dict = dict(tuple_list)

    return dict(sorted(my_dict.items()))

my_list = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_dict = convert_and_sort_dict(my_list)
print(sorted_dict) 