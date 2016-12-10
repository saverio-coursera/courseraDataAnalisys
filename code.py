__author__ = 'saverio'
# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters={}
for i in range(0,27):
    letters[i]=alphabet[i]


def caesar(message, key):
    coded_message={}
    for i in range(0,len(alphabet)):
        coded_message[alphabet[i]]=(i+key)%len(alphabet)

    # return the encoded message as a single string!
    result=""
    for i in range(0,len(message)):
        result=result+alphabet[coded_message[message[i]]]
    return(result)

message = "hi my name is caesar"
coded_message=caesar(message,3)

decoded_message=caesar(coded_message,-3)
print(message)
print(coded_message)
print(decoded_message)