from metrics.utils.sentiment_test import predict_sentiment

# happiness_base_words = {
#     "happy": "happiness",
#     "joy": "happiness",
#     "cheer": "happiness",
#     "delight": "happiness",
#     "merry": "happiness",
#     "radiant": "happiness",
#     "satisfy": "happiness",
#     "smile": "happiness",
#     "sparkle": "happiness",
#     "glee": "happiness",
#     "peace": "happiness",
#     "relax": "happiness",
#     "thank": "happiness",
#     "tranquil": "happiness",
#     "uplift": "happiness",
#     "bright": "happiness",
#     "glow": "happiness",
#     "content": "happiness",
#     "jubilant": "happiness",
#     "ecstatic": "happiness",
# }

# happiness_int = {
#     546: "happiness",
#     338: "happiness",
#     519: "happiness",
#     737: "happiness",
#     559: "happiness",
#     739: "happiness",
#     771: "happiness",
#     538: "happiness",
#     754: "happiness",
#     413: "happiness",
#     510: "happiness",
#     540: "happiness",
#     534: "happiness",
#     880: "happiness",
#     660: "happiness",
#     640: "happiness",
#     441: "happiness",
#     763: "happiness",
#     857: "happiness",
#     848: "happiness",
# }
# common_suffixes = ["ing", "ful", "ed", "ly", "ness", "s"]


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


# def check_happiness(s):
#     words = split_words(s)
#     value = 0
#     for w in words:
#         w = preprocess_word(w)
#         value = convert_interger_sum_value_of_indivual_index_of_string(w)
#         if value in happiness_int:
#             return "happy"

#     return "not happy"


def check_happiness_sentiment(texts):
    sentiment = predict_sentiment(texts)  # Predict sentiment for the list of texts
    # print(sentiment)
    # print(f"Text: {texts}\nSentiment: {sentiment}\n")
    
    if sentiment[0] in ["Very Negative", "Negative", "Neutral"]:
        return "not happy"
    elif sentiment[0] in ["Positive", "Very Positive"]:
        return "happy"
      
    return "not happy"  # Default return value if no happy sentiment is found
