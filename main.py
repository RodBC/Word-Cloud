def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    words_filtered = []
    words_count = {}
    
    for words in file_contents.split():
        if words.isalpha() and words.lower() not in uninteresting_words:
            words_filtered.append(words.lower())
            
    for word in words_filtered:
        if word not in words_count:
            words_count[word] = 0
            words_count[word]+=file_contents.split().count(words)
    



    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_count)
    return cloud.to_array()
