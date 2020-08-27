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
        print("{:.2f}".format(cgpa))

cgpaCalculator(arr)

