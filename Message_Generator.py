# Made by SWARAJ M.

# taking basic input from the user
name=input("Enter your NAME please:")
age=input("Enter your AGE please:")
date=input("Enter today's DATE please:")

# Basic Message template
message='''Welcome <|name|>,
\tYou have register here on <|date|>
\tYou are now <|age|> years old
Glad to see you here'''

# Basic replacement with name, date and age
print(message.replace("<|name|>",name).replace("<|date|>",date).replace("<|age|>",age))
