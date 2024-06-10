def main(name, age, ansSheet):
    score = 0
    questions = [
        "Who is the prime minister of India?\n1. Narendra Modi\t2. Rahul Gandhi\t3. Nitin Gadkari\t4. Draupati Murmuri",
        "Who is the president of India?\n1. Narendra Modi\t2. Rahul Gandhi\t3. Nitish Kumar\t4. Draupati Murmuri",
        "Financial Capital of India?\n1. Delhi\t2. Pune\t3. Mumbai\t4. Gujrat",
        "What is the value of g?\n1. 9.7\n2. 9.8\n3. 8.9\n4. 7.9",
        "Who is the governor of Maharastra?\n1. BhagatSingh Koshyari\t2. Ramesh Bais\t3. Rajnath Singh\t4. Ashwini Vaishnaw",
        "Which state launched a mobile app for navigation on rivers at night and became the first state of India to do this?\n1. Maharastra\t2. Assam\t3. Delhi\t4. Gujarat",
        "World Wetlands Day is celebrated on?\n1. 2 January\t2. 2 February\t3. 22 March\t4. 20 April",
        "The Ahmedabad team of the IPL will be called as _____\n1. Ahmedabad Zenith\t2. Gujarat Titans\t3. Mumbai Indians\t4. Kolkata Knight Riders",
        "Which is the first state to become 'Har Ghar Jal' state in India?\n1. Mumbai\t2. Delhi\t3. Goa\t4. Chennai",
        "Which is the first dam in India?\n1. Kallanai Dam\t2. Khadakvasala Dam\t3. Panshet Dam\t4. Koyana Dam",
    ]

    print("Welcome to Kaun Banega Sasta Ka-roadpati\n")
    print("\nNice to see you here ", name, " at age ", age)
    start = input("\nAre you ready to play the game (y/n): ")
    if start.lower() != 'y':
        print("Goodbye!")
        return 0

    print("\nLet's start the game")
    for i in range(len(questions)):
        print("\nHere is your next question ")
        print(questions[i], "\n")
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == ansSheet[i]:
            score += 1
        else:
            print("Wrong answer! Game over.")
            print("Your final score is: ",score)
            return score

    print("\nCongratulations! You've completed the game.")
    print("Your final score is: ", score)
    if(score>=9):
        print("\nBravo! You are a Genius")
    return score

print("\nWelcome to Kon Banega Sasta Ka-roadpati\n")
Pname = input("\nEnter Player Name: ")
Playage = input("\nEnter Player's age: ")
ansSheet = ["1", "4", "3", "2", "2", "2", "2", "2", "3", "1"]
score = main(Pname, Playage, ansSheet)
