from metrics.utils.sentiment_test import predict_sentiment

# sadness_map = {
#     "grief": "sadness",
#     "sorrow": "sadness",
#     "sad": "sadness",
#     "sadness": "sadness",
#     "melancholy": "sadness",
#     "despair": "sadness",
#     "misery": "sadness",
#     "gloom": "sadness",
#     "unhappy": "sadness",
#     "mourn": "sadness",
#     "anguish": "sadness",
#     "heartache": "sadness",
#     "woe": "sadness",
#     "desolation": "sadness",
#     "unhappiness": "sadness",
#     "dejection": "sadness",
#     "downheartedness": "sadness",
#     "mourning": "sadness",
#     "regret": "sadness",
#     "lamentation": "sadness",
#     "melancholia": "sadness",
#     "blues": "sadness",
#     "despondency": "sadness",
#     "heaviness": "sadness",
#     "forlornness": "sadness",
#     "pain": "sadness",
#     "bitterness": "sadness",
#     "remorse": "sadness",
#     "heartbreak": "sadness",
#     "heartbreakingache": "sadness",
#     "dolefulness": "sadness",
#     "hopelessness": "sadness",
#     "pessimism": "sadness",
#     "melancholic": "sadness",
#     "discontent": "sadness",
#     "affliction": "sadness",
#     "depress": "sadness",
#     "tears": "sadness",
#     "lugubriousness": "sadness",
#     "dolor": "sadness",
#     "disheartenment": "sadness",
#     "disconsolateness": "sadness",
#     "lament": "sadness",
#     "downcast": "sadness",
#     "mournfulness": "sadness",
#     "low spirits": "sadness",
#     "weariness": "sadness",
#     "tristfulness": "sadness",
#     "somberness": "sadness",
#     "tristesse": "sadness",
#     "plaintiveness": "sadness",
#     "depressed": "sadness",
#     "heartbroken": "sadness",
#     "mournful": "sadness",
#     "pessimistic": "sadness",
#     "somber": "sadness",
#     "sorrowful": "sadness",
#     "sorry": "sadness",
#     "bereaved": "sadness",
#     "blue": "sadness",
#     "cheerless": "sadness",
#     "dejected": "sadness",
#     "despairing": "sadness",
#     "despondent": "sadness",
#     "disconsolate": "sadness",
#     "distressed": "sadness",
#     "doleful": "sadness",
#     "down": "sadness",
#     "forlorn": "sadness",
#     "gloomy": "sadness",
#     "glum": "sadness",
#     "grief-stricken": "sadness",
#     "grieved": "sadness",
#     "heartsick": "sadness",
#     "heavy-hearted": "sadness",
#     "hurting": "sadness",
#     "inconsolable": "sadness",
#     "low": "sadness",
#     "low-spirited": "sadness",
#     "morose": "sadness",
#     "pensive": "sadness",
#     "wistful": "sadness",
# }

# sadness_int_map ={
#     525: "sadness",
#     684: "sadness",
#     312: "sadness",
#     753: "sadness",
#     1068: "sadness",
#     744: "sadness",
#     665: "sadness",
#     542: "sadness",
#     773: "sadness",
#     561: "sadness",
#     751: "sadness",
#     933: "sadness",
#     331: "sadness",
#     1074: "sadness",
#     1198: "sadness",
#     949: "sadness",
#     1614: "sadness",
#     879: "sadness",
#     649: "sadness",
#     1180: "sadness",
#     1149: "sadness",
#     539: "sadness",
#     966: "sadness",
#     1211: "sadness",
#     424: "sadness",
#     1091: "sadness",
#     765: "sadness",
#     1049: "sadness",
#     1768: "sadness",
#     1188: "sadness",
#     1308: "sadness",
#     986: "sadness",
#     1151: "sadness",
#     1083: "sadness",
#     1055: "sadness",
#     758: "sadness",
#     543: "sadness",
#     1546: "sadness",
#     544: "sadness",
#     1499: "sadness",
#     1729: "sadness",
#     641: "sadness",
#     867: "sadness",
#     1329: "sadness",
#     1152: "sadness",
#     977: "sadness",
#     1334: "sadness",
#     1089: "sadness",
#     998: "sadness",
#     1413: "sadness",
#     959: "sadness",
#     1173: "sadness",
#     888: "sadness",
#     1197: "sadness",
#     648: "sadness",
#     1011: "sadness",
#     575: "sadness",
#     830: "sadness",
#     958: "sadness",
#     824: "sadness",
#     1062: "sadness",
#     1076: "sadness",
#     1288: "sadness",
#     1082: "sadness",
#     747: "sadness",
#     440: "sadness",
#     770: "sadness",
#     663: "sadness",
#     437: "sadness",
#     1437: "sadness",
#     742: "sadness",
#     1319: "sadness",
#     769: "sadness",
#     1273: "sadness",
#     338: "sadness",
#     1251: "sadness",
#     661: "sadness",
#     762: "sadness",
#     782: "sadness",
# }
# common_suffixes = ["ing", "ful", "ed", "ly", "ness", "s"]

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
      
# def check_word_in_sadness(s):
#     words=split_words(s)
#     value=0
#     for w in words:
      
#       value=convert_interger_sum_value_of_indivual_index_of_string(w)
#       if value in sadness_int_map:
#         return "sad"
      
#     return "not sad"

def check_sadness_sentiment(texts):
    sentiment = predict_sentiment(texts)  # Predict sentiment for the list of texts
    # print(sentiment)
    # print(f"Text: {texts}\nSentiment: {sentiment}\n")
    
    if sentiment[0] in ["Very Negative", "Negative", "Neutral"]:
        return "sad"
    elif sentiment[0] in ["Positive", "Very Positive"]:
        return "not sad"
      
