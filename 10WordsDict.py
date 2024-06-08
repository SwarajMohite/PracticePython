# Simple Dictonary of ten common hard words...
# make by Swaraj
dic={"Belie" : "To give a false representation to misrepresent", "Arrant" : "Complete and wholly" ,"Untoward" : "Inconvenient", "Byzantine ": "Complex and intricate", "Conciliate" : "To make peace with","Equivocate" : "To speak vaguely or with the intention of misleading someone", "Truculent" : "Have a fierce or savage nature" , "Diatribe" : "A verbal attack against a person", "Quisling" : "A traitor", "Artless" : "without cunning or deceit "}
word=input("Note: Enter first letter capital\nTry WORDS \nBelie \t Arrant \t Untoward \t Byzantine \t Conciliate \t Equivocate \t Truculent \t Diatribe \t Quisling \n Copy above word and type below\n Enter the word: ")
if(word!=dic): {
  print("Sorry! The Word is not in the Dictonary...")
}
else : {
print("Meaning of",word, "is ",dic[word])
}
