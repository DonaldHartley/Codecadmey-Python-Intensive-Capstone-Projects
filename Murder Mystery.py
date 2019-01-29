murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a 'walk'. A 'walk' with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."

def get_avg_sentence_len (text):
    '''
    This function takes a single text string and returns the average sentence lenght as an integer
    '''
    
    lst_of_sentc = []
    total_len = 0
    avg_len = 0
    
    #replacing other punctuation with '.' and spliting text into sentences
    text = text.replace('?','.').replace('!','.').split('.')
    
    #stripping extra spaces and skipping empty strings from the end of the text
    #created by the split method
    for sentence in text:
        if sentence == "":
            pass
        else:
            lst_of_sentc.append(sentence.strip())
    
    #get the sentence length of the text
    num_of_sentc = len(lst_of_sentc)
    
    #get the word length of each sentence
    for sentence in lst_of_sentc:
        total_len += len(sentence.split(' '))
    
    #calculate the average
    avg_len = total_len // num_of_sentc
    
    return avg_len

def prepare_text(text):
    '''
    this function takes a single text string and returns a list of the words in lowercase
    preserving the difference between words like "its" and "it's"
    '''
    
    punct = ['.', ',', '?', '!', '"', ':', ';']
    
    #replaces the punctuation marks with an empty string ''
    for mark in punct:
        text = text.replace(mark, '')
        
    #drops all words to lowercase and splits the string
    word_lst = text.lower().split(' ')
    
    return word_lst

def build_frequency_table(corpus):
    '''
    takes a list of words and returns a dictionary
    with the count of each unique word as 'word':count
    '''
    
    frequency_table = {}
    
    #this uses set to find the list of unique words and count each instance
    #then save the word:count pair in the dictionary
    for word in set(corpus):
        frequency_table[word] = corpus.count(word)
    
    return frequency_table

def ngram_creator(text_lst):
    '''
    this function takes an ordered list of words and returns the list as 
    two word pairs from that order ex. ['a', 'c', 'b', 'd'] would return
    ['a c', 'c b', 'b d']
    '''
    
    ngram_lst = []
    
    #this uses i as the iterator and index value to join the words into pairs
    #-1 is used to ensure that the last pair is not a single word
    for i in range(0,len(text_lst)-1): 
        temp = text_lst[i] + ' ' + text_lst[i+1]
        ngram_lst.append(temp)
        
    return ngram_lst
    
class TextSample:
    '''
    This is the class definition to prepair a text sample for analysis
    this requires two arguments 
    1 a long string to be evaluated
    2 the name of the author
    '''
    
    def __init__(self, text, author):
        self.raw_text = text #this stores the raw text to be used later as needed
        self.author = author #this stores the authors name as a string
        
        #this stores the average sentence length as an integer
        self.average_sentence_length = get_avg_sentence_len(self.raw_text)
        
        #this stores a list of the words from the raw_text in order
        self.prepared_text = prepare_text(self.raw_text)
        
        #this stores a dictionary of the set of unique words in the text and their count in the raw_text
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        
        #this stores a dictionary of the set of unique two word pairs and their count in the raw_text
        self.ngram_frequency = build_frequency_table(ngram_creator(self.prepared_text))
        
    def __repr__(self):
        return "The author {self.author} writes with an avgrage sentence length of {self.average_sentence_length} words.".format(**locals())

def frequency_comparison(dict1, dict2):
    '''
    this function takes two dictionarys of word:count pairs and counts the number of mutual appearences
    against the number total appearences (inclusive) 
    ex. 'bath':2 and 'bath':7 >> 2 would be added to mutual, and 7 to the total
    if the appearences are == then the value is added to both
    additionally if a word does not appear in both dictionarys the value is added to the total
    finally this function returns the mutual/total appearences as a float to represent the 
    percentage similarity between the two dictionarys
    '''
    
    appearances = 0
    mutual_appearances = 0
    similarity = 0
    
    for key in dict1.keys(): 
        if key in dict2.keys():
            #this compairs the value of the shared keys and store the values appropriately
            if dict1[key] >= dict2[key]: 
                mutual_appearances += dict2[key]
                appearances += dict1[key]
            elif dict1[key] < dict2[key]:
                mutual_appearances += dict1[key]
                appearances += dict2[key]
        elif key not in dict2.keys(): #checks for keys not in dict2
            appearances += dict1[key]
            
    for key in dict2.keys(): #checks for keys not in dict1
        if key not in dict1.keys():
            appearances += dict2[key]
    
    #this calculates the similarity as a float
    similarity = mutual_appearances/appearances
    
    return similarity

def percent_difference(num1, num2):
    '''
    this function calcualtes the percent difference as
    absolute difference / average size
    and returns it as a float
    '''
    
    return abs(num1-num2)/((num1+num2)/2)

def find_text_similarity(txt1, txt2):
    '''
    this function takes two TextSample Class' and prints the 
    sentence length, word frequency, and ngram similaritys as % to two decimal places
    it also prints and returns the total avergage similarity
    '''
    
    #this calculates the % difference of the sentence length of the avegrage sentence lengths of the two classes
    sentence_length_difference = percent_difference(txt1.average_sentence_length ,txt2.average_sentence_length)
    
    #this converts the difference to smiliarity of sentence length as a % to two decimal places
    sentence_length_similarity = round(abs(1 - sentence_length_difference)*100,2)
    
    #this calculates the similarity of word use frequency as a % to two decimal places
    word_frequency_similarity = round(frequency_comparison(txt1.word_count_frequency, txt2.word_count_frequency)*100,2)
    
    #this calculates the similarity of ngram use frequency as a % to two decimal places
    ngram_similarity = round(frequency_comparison(txt1.ngram_frequency, txt2.ngram_frequency)*100,2)
    
    #this averages the similarity of sentence length, word frequency, and ngram frequency
    total_similarity_avg = (sentence_length_similarity + word_frequency_similarity + ngram_similarity)/3
    
    #this calculates the average similarity as a % to two decimal places
    total_similarity_percentage = round(total_similarity_avg,2)
    
    #these are the print statements for convienent review
    print ("Sentence length similarity: {sentence_length_similarity}% \nWord frequency similarity: {word_frequency_similarity}% \nNgram similarity: {ngram_similarity}%".format(**locals()))
    print ("{txt1.author}'s writing similarity to the {txt2.author}'s letter is {total_similarity_percentage}%\n".format(**locals()))
    
    return total_similarity_percentage
    
murderer_sample = TextSample(murder_note, 'murderer')
lily_sample = TextSample(lily_trebuchet_intro, 'Lily Trebuchet')
myrtle_sample = TextSample(myrtle_beech_intro, 'Myrtle Beech')
gregg_sample = TextSample(gregg_t_fishy_intro, 'Gregg T Fishy')

find_text_similarity(lily_sample, murderer_sample)
find_text_similarity(myrtle_sample, murderer_sample)
find_text_similarity(gregg_sample, murderer_sample)

#need a function to return the person with the highest match percentage
