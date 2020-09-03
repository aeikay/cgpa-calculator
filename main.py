# CGPA calculator sample program for ECE Students #
# Enter the number of semesters completed and give the sgpa of corresponding semesters #
# CGPA will be outputted #
# uses pyttsx3 TTS library - works offline#


import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', 150 )

engine.say("Hello there, welcome to C G P A calculator, Please enter your name")
engine.runAndWait()


name = input("Enter your name : ")


engine.say("Enter the number of semesters completed")
engine.runAndWait()


num = int(input("Enter the number of semesters completed:"))
i = 0
arr = []
for i in range(num):
    arr.append(input("Enter your sgpa of " + str(i+1) + "th" + " sem : "))

def cgpaCalculator(arr):
        credits = [17,17,21,22,23,22,22,22]
        creditTotal = 0
        summ = 0
        for i in range(num):
                  summ += float(credits[i]* float(arr[i]))
                  creditTotal += credits[i]

        cgpa = summ/creditTotal
        
        # Taking the output and converting to speech


        string =  "{:.2f}".format(cgpa)
        my_dict = {'0': ' zero ', '1': ' one ', '2': ' two ', '3': ' three ', '4': ' four ', '5': ' five ', '6': ' six ', '7': ' seven ', '8': ' eight ', '9': ' nine ','.':' point '}
        for item in string:
            if item in my_dict.keys():
                  result = string.replace(item, my_dict[item])

        engine.say("Your  C G P A is "+ result)
        engine.runAndWait()
        print("Your CGPA is " + string)
        string = float(string)

        if string < 7.5:
            engine.say("You have to improve ," + name +  ", keep up the spirit, All the best")
            engine.runAndWait()
        elif string >= 7.5:
            engine.say("keep up the good work ," + name + "  All the best")
            engine.runAndWait()
        

        
cgpaCalculator(arr)