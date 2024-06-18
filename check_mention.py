# A Program to check whether the user is mentioned in any post or not 

# Accepting info from user
name=input("Enter name: ")
post=input("Paste the post here: ")

# Checking the mention
if(name.lower() in post.lower()):
    print(f"Dear {name} ,\n\tYou have been mentioned in the post : \n",post)
else :
    print(f"Sorry! {name},\n\tyou haven't been mentioned in the post ")
