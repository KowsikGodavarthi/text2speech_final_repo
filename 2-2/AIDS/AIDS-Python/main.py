print("HI...I am Student advisor chat bot..")
name=str(input("May I know your name \n"))
print("Thank you ",name)
print("I am here to explore you about the core courses required for specializations offered by KL University CSE Department ")
print("Here are the specializations offered by K L university CSE departmant: ")
while(1):
    print("\n\n\n1. Software Modeling and DevOps\n2. Internet of Things\n3. Cloud and edge computing\n4. Graphics, gaming and UI design")
    print("5. Cyber security and Blockchain Technology\n6. Artificial Intelligence and Intelligence Process Automation")
    print("7. Data Scaience and Big Data Analytics\n8. Computer Communications\n9. Exit")
    choice=int(input("Enter your choice....\n"))
    if choice==1:
        print("\n\n\nMathematical Programming and Software Engineering")
    elif choice==2:
        print("\n\n\nComputer Networks and Security and Operating Systems")
    elif choice==3:
        print("\n\n\nDBMS and Computer Networks and Security")
    elif choice==4:
        print("\n\n\nAdvance Object Oriented Programming and Software Engineering")
    elif choice==5:
        print("\n\n\nAdvance Object Oriented Programming and Computer Networks and Security")
    elif choice==6:
        print("\n\n\nAI for DS and Operating Systems")
    elif choice==7:
        print("\n\n\nAI for DS and DBMS")
    elif choice==8:
        print("\n\n\nOperating Systems and Computer Networks and Security")
    else:
        break
else:
    print("Invalid Output\n")
