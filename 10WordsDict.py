# Simple Dictionary of ten common hard words...
# made by Swaraj
dic = {
    "Belie": "To give a false representation to misrepresent",
    "Arrant": "Complete and wholly",
    "Untoward": "Inconvenient",
    "Byzantine": "Complex and intricate",
    "Conciliate": "To make peace with",
    "Equivocate": "To speak vaguely or with the intention of misleading someone",
    "Truculent": "Have a fierce or savage nature",
    "Diatribe": "A verbal attack against a person",
    "Quisling": "A traitor",
    "Artless": "Without cunning or deceit"
}

word = input("Note: Enter first letter capital\nTry WORDS \nBelie \t Arrant \t Untoward \t Byzantine \t Conciliate \t Equivocate \t Truculent \t Diatribe \t Quisling \t Artless\nCopy above word and type below\nEnter the word: ")

if word in dic:
    print("Meaning of", word, "is", dic[word])
else:
    print("Sorry! The Word is not in the Dictionary...")
