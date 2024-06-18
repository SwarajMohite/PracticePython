# A Program to detect A SPAM Message

# Common Keywords of Spam Messages
Spam_msg_keyword1="Make a lot of money"
Spam_msg_keyword2="Send OTP"
Spam_msg_keyword3="Buy now"
Spam_msg_keyword4="click this"
Spam_msg_keyword5="Free"

# Accept the message from the user
print("Paste the message you have received here: ")
my_msg=input()

# Checking if it is Spam or not
if(Spam_msg_keyword1 in my_msg or Spam_msg_keyword2 in my_msg or Spam_msg_keyword3 in my_msg or Spam_msg_keyword4 in my_msg or Spam_msg_keyword5 in my_msg):
    print("Alert! You have recieved a spam message \n \tDon't click on any link there\n\tAlso don't share OTP and bank details to any one\n Stay Alert")
else:
    print("You are safe!\n\t You haven't received spam message \n \tStay Alter \t Stay Positive :)")

