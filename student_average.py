# برنامج لحساب معدل علامات طالب
marks = []

num_subjects = int(input("كم عدد المواد؟ "))

for i in range(num_subjects):
    mark = float(input(f"أدخل علامة المادة {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print(f"معدلك هو: {average:.2f}")
if average >= 10:
    print("مبروك! نجحت 🎉")
else:
    print("للأسف، لم تنجح 😔")
