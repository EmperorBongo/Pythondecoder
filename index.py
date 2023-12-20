# This problem has been solved!
# You'll get a detailed solution from a subject matter expert that helps you learn core concepts.

# See answer
# User Prompt/ QUESTION TO BE ANSWERED

# I need a function called decode(message_file) that can read in an encoded message from a .txt file and return the decoded version as a string.

# Here's an example of what the message_file .txt file will look like:

# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you

# As you can see, each word is associated with a number. Imagine you ordered all those numbers from smallest to biggest and arranged them into a pyramid. Each line of the pyramid includes one more number than the line before it:

# 1
# 2 3
# 4 5 6

# The numbers at the end of each line (1, 3 and 6) correspond to the words that are part of the message. You should ignore all the other words. So for the example input file above, the message words are:

# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers"


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
 
    word_map = {int(line.split()[0]): line.split()[1] for line in lines}
    message = []
    line_end = 1
 
    while line_end in word_map:
        message.append(word_map[line_end])
        line_end = line_end * (line_end + 1) // 2
 
    return ' '.join(message)

print (decode('code.txt'))


message_file = 'message_file.txt'
decoded_message = decode(message_file)
print(decoded_message)







