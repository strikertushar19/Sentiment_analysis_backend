anger_words = {
    "mad": "anger",
    
    "angry": "anger",
    "furious": "anger",
    "rage": "anger",
    "irate": "anger",
    "irritated": "anger",
    "enraged": "anger",
    "annoyed": "anger",
    "mad": "anger",
    "fuming": "anger",
    "livid": "anger",
    "outraged": "anger",
    "wrath": "anger",
    "displeased": "anger",
    "cross": "anger",
    "incensed": "anger",
    "vexed": "anger",
    "frustrated": "anger",
    "exasperated": "anger",
    "upset": "anger",
    "boiling": "anger",
    "heated": "anger",
    "tempestuous": "anger",
    "agitated": "anger",
    "provoked": "anger",
    "resentful": "anger",
    "hostile": "anger",
    "antagonistic": "anger",
    "belligerent": "anger",
    "combative": "anger",
    "sulking": "anger",
    "indignant": "anger",
    "disgruntled": "anger",
    "bitter": "anger",
    "stressed": "anger",
    "madder": "anger",
    "stormy": "anger",
    "irritancy": "anger",
    "huffy": "anger"
}

def convert_map_key_value_to_integer_and_return_new_map(maptoconvert,metric_name):
    int_map = {}
    for i, j in maptoconvert.items():
        key_sum = 0
        for z in i:
            key_sum += ord(z)  # ord() gives the ASCII value of a character

        int_map[key_sum] = metric_name  # Add the calculated key-value pair to the map
    
    return int_map  # Return the entire dictionary after processing all items

print(convert_map_key_value_to_integer_and_return_new_map(anger_words,"angerness"))