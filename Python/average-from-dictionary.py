# Taken from https://github.com/snietzsche/interview-prompts
#
#Write a Python script that calculates each student's average score using the below dictionary as the source of the input data:
#
# Example: $ ./script.py
# Sally: 88
# Grace: 89
# Tom: 90
# data = {"Tom":{"tests":{"2021-02-01":89,"2021-02-17":76,"2021-03-20":98,"2021-04-12":100,"2021-05-04":87}},"Sally":{"tests":{"2021-02-01":87,"2021-02-17":94,"2021-03-20":98,"2021-04-12":78,"2021-05-04":84}},"Grace":{"tests":{"2021-02-01":97,"2021-02-17":88,"2021-03-20":98,"2021-04-12":82,"2021-05-04":83}}}

data = {"Tom":{"tests":{"2021-02-01":89,"2021-02-17":76,"2021-03-20":98,"2021-04-12":100,"2021-05-04":87}},"Sally":{"tests":{"2021-02-01":87,"2021-02-17":94,"2021-03-20":98,"2021-04-12":78,"2021-05-04":84}},"Grace":{"tests":{"2021-02-01":97,"2021-02-17":88,"2021-03-20":98,"2021-04-12":82,"2021-05-04":83}}}

for student in data:
    scores = data[student]["tests"]
    print("Student: {} Average: {}".format(student, sum(scores.values())/len(scores.keys())))
    
