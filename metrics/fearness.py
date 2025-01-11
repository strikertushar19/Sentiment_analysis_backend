from metrics.utils.sentiment_test import predict_sentiment

# fear_words = {
#     "fear": "fear",
#     "afraid": "fear",
#     "alarmed": "fear",
#     "anxious": "fear",
#     "apprehensive": "fear",
#     "cautious": "fear",
#     "concerned": "fear",
#     "cowardly": "fear",
#     "dismayed": "fear",
#     "distressed": "fear",
#     "dreadful": "fear",
#     "fearful": "fear",
#     "frightened": "fear",
#     "hesitant": "fear",
#     "horrified": "fear",
#     "intimidated": "fear",
#     "jittery": "fear",
#     "nervous": "fear",
#     "panicked": "fear",
#     "petrified": "fear",
#     "scared": "fear",
#     "shaken": "fear",
#     "shy": "fear",
#     "spooked": "fear",
#     "startled": "fear",
#     "terrified": "fear",
#     "timid": "fear",
#     "troubled": "fear",
#     "uneasy": "fear",
#     "unnerved": "fear",
#     "vulnerable": "fear",
#     "wary": "fear",
#     "worried": "fear",
#     "alarm": "fear",
#     "angst": "fear",
#     "dread": "fear",
#     "horror": "fear",
#     "panic": "fear",
#     "terror": "fear",
#     "trepidation": "fear",
#     "phobic": "fear",
# }

# fear_int={
#     414: "fearness",
#     615: "fearness",
#     726: "fearness",
#     775: "fearness",
#     1290: "fearness",
#     877: "fearness",
#     945: "fearness",
#     869: "fearness",
#     848: "fearness",
#     1082: "fearness",
#     839: "fearness",
#     741: "fearness",
#     1056: "fearness",
#     864: "fearness",
#     956: "fearness",
#     1164: "fearness",
#     779: "fearness",
#     786: "fearness",
#     831: "fearness",
#     626: "fearness",
#     634: "fearness",
#     340: "fearness",
#     757: "fearness",
#     867: "fearness",
#     958: "fearness",
#     535: "fearness",
#     865: "fearness",
#     661: "fearness",
#     871: "fearness",
#     1072: "fearness",
#     451: "fearness",
#     764: "fearness",
#     525: "fearness",
#     541: "fearness",
#     512: "fearness",
#     668: "fearness",
#     523: "fearness",
#     670: "fearness",
#     1187: "fearness",
#     629: "fearness",
# }
# common_suffixes = ["ing", "ful", "ly", "ness", "s"]

# def preprocess_word(word):
#     """Remove common suffixes from the word."""
#     for suffix in common_suffixes:
#         if word.endswith(suffix):
#             return word[: -len(suffix)]
#     return word


# def split_words(s):
#   words=s.split()
#   return words

# def convert_interger_sum_value_of_indivual_index_of_string(s):
#       s=s.lower()
#       value_sum=0
#       for z in s:
#         value_sum += ord(z)  
#       return value_sum
      

     
# def check_fearness(s):
#     words=split_words(s)
#     value=0
#     for w in words:
#       w=preprocess_word(w)
#       value=convert_interger_sum_value_of_indivual_index_of_string(w)
#       if value in fear_int:
#         return "fear"
      
#     return "no fear"
def check_fearness_sentiment(texts):
    sentiment = predict_sentiment(texts)  # Predict sentiment for the list of texts
    # print(sentiment)
    # print(f"Text: {texts}\nSentiment: {sentiment}\n")
    
    if sentiment[0] in ["Very Negative", "Negative", "Neutral"]:
        return "fear"
    elif sentiment[0] in ["Positive", "Very Positive"]:
        return "no fear"
      
