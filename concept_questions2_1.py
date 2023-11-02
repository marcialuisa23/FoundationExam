# question 2.1
   # 2.1    Write a function that takes in an input and checks to see if it’s an
   #           isogram. The function should return True or False. 
             
   #           An isogram is a word where no letter is repeated.
   #           Examples include:
# "isogram"
# "uncopyrightable"
# “ambidextrously”

def is_isogram(word):

    # set has no repeated characters, if length is different it is an isogram
    return len(word) > 0 and len(word) == len(set(word.lower()))

