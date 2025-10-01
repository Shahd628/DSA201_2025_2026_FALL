top_scorers = [
      ["11 goal(s)", "Sebastien Haller", "Ajax"],
      ["8 goal(s)", "Mohamed Salah", "Liverpool"],
      ["14 goal(s)", "Karim Benzema", "Real Madrid"],
      ["7 goal(s)", "Christopher Nkunku", "Leipzig"],
      ["13 goal(s)", "Robert Lewandowski", "Bayern Munich"]
]

allGoals = []
for sublist in top_scorers:
    cur_goal = int(sublist[0].replace(" goal(s)", ""))
    allGoals.append(cur_goal)

maxGoal = max(allGoals)

for sublist in top_scorers:
    cur_goal = int(sublist[0].replace(" goal(s)", ""))
    if cur_goal == maxGoal:
        print(sublist[1], "-", sublist[2])