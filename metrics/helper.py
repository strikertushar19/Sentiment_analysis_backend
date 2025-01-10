def convert_map_key_value_to_integer_and_return_new_map(maptoconvert):
  int_map = {}
  for i, j in maptoconvert.items():
    key_sum = 0
    for z in i:
        key_sum += ord(z)  # ord() gives the ASCII value of a character

    value_sum = 0
    for z in j:
        value_sum += ord(z)  # ord() gives the ASCII value of a character

    int_map.update({key_sum: value_sum})

