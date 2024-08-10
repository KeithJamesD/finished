def calculate_average():
    scores = []
    n = int(input("How many scores do you have?: \n"))
    for i in range(n):
        score = input("What was your score?: \n")
        scores.append(int(score))
    average = sum(scores) / n
    return average

average_score = calculate_average()
print(f"Average score is {average_score}.")