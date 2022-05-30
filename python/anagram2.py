# Don't forget to run the tests (and create some of your own)
#run the character match code as a sub-function within the greater function anagram, calling it on all the words in the array
#from character_match import is_character_match

def is_character_match(string1, string2):
    str1_arr = sorted(list(string1.lower()))
    str2_arr = sorted(list(string2.lower()))
    for i,x in enumerate(str1_arr) :
        if str1_arr[i] != str2_arr[i]:
            return False
    return True

def anagrams_for(word, list_of_words):
	match_list = []
	for x in list_of_words:
		if is_character_match(word,x):
			match_list.append(x)
			#print(x,match_list)
	return match_list
	

#print(anagrams_for("threads",["threads", "trashed", "hardest", "hatreds", "hounds"]))
		# your code here
