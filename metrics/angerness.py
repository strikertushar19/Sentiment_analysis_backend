from metrics.utils.sentiment_test import predict_sentiment

# anger_words = {
#     "mad": 'anger',
#     "anger": "anger",
#     "angry": "anger",
#     "furious": "anger",
#     "rage": "anger",
#     "irate": "anger",
#     "irritated": "anger",
#     "enraged": "anger",
#     "annoyed": "anger",
#     "mad": "anger",
#     "fuming": "anger",
#     "livid": "anger",
#     "outraged": "anger",
#     "wrath": "anger",
#     "displeased": "anger",
#     "cross": "anger",
#     "incensed": "anger",
#     "vexed": "anger",
#     "frustrated": "anger",
#     "exasperated": "anger",
#     "upset": "anger",
#     "boiling": "anger",
#     "heated": "anger",
#     "tempestuous": "anger",
#     "agitated": "anger",
#     "provoked": "anger",
#     "resentful": "anger",
#     "hostile": "anger",
#     "antagonistic": "anger",
#     "belligerent": "anger",
#     "combative": "anger",
#     "sulking": "anger",
#     "indignant": "anger",
#     "disgruntled": "anger",
#     "bitter": "anger",
#     "stressed": "anger",
#     "madder": "anger",
#     "stormy": "anger",
#     "irritancy": "anger",
#     "huffy": "anger",
# }


# anger_int={
#     306: 'angerness',
#     525: "angerness",
#     545: "angerness",
#     781: "angerness",
#     415: "angerness",
#     533: "angerness",
#     968: "angerness",
#     726: "angerness",
#     750: "angerness",
#     306: "angerness",
#     646: "angerness",
#     536: "angerness",
#     859: "angerness",
#     550: "angerness",
#     1054: "angerness",
#     554: "angerness",
#     841: "angerness",
#     540: "angerness",
#     1092: "angerness",
#     1174: "angerness",
#     561: "angerness",
#     740: "angerness",
#     619: "angerness",
#     1230: "angerness",
#     835: "angerness",
#     874: "angerness",
#     984: "angerness",
#     760: "angerness",
#     1284: "angerness",
#     1165: "angerness",
#     954: "angerness",
#     765: "angerness",
#     956: "angerness",
#     1189: "angerness",
#     650: "angerness",
#     877: "angerness",
#     621: "angerness",
#     686: "angerness",
#     981: "angerness",
#     546: "angerness",
# }
# common_suffixes = ["ing", "ful", "ly", "ness", "s"]


# def preprocess_word(word):
#     """Remove common suffixes from the word."""
#     for suffix in common_suffixes:
#         if word.endswith(suffix):
#             return word[: -len(suffix)]
#     return word


# def split_words(s):
#     words = s.split()
#     return words


# def convert_interger_sum_value_of_indivual_index_of_string(s):
#     s = s.lower()
#     value_sum = 0
#     for z in s:
#         value_sum += ord(z)
#     return value_sum


# def check_angerness(s):
#     words = split_words(s)
#     value = 0
#     for w in words:
#         w = preprocess_word(w)
#         value = convert_interger_sum_value_of_indivual_index_of_string(w)
#         if value in anger_int:
#             return "angry"

#     return "not angry"

def check_angerness_sentiment(texts):
    sentiment = predict_sentiment(texts)  # Predict sentiment for the list of texts
    # print(sentiment)
    # print(f"Text: {texts}\nSentiment: {sentiment}\n")
    
    if sentiment[0] in ["Very Negative", "Negative", "Neutral"]:
        return "angry"
    elif sentiment[0] in ["Positive", "Very Positive"]:
        return "not angry"
      
