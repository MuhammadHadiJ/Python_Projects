import pandas as pd

q1 = input("What is your name? ")
q2 = int(input("What is your age? "))
q3 = input("what is your hobbie? ")
q4 = input("what is your faiourte color? ")
q5 = input("what is your faviorte fruit? ")

list1 = [q1,q2,q3,q4,q5]

q11 = "name"
q22 = "age"
q33 = "hobbie"
q44 = "color"
q55 = "fruit"

col1 = "Qs"
col2 = "As"

list2 = [q11,q22,q33,q44,q55]

data = pd.DataFrame({col1:list2,col2:list1})
data.to_excel('info.xlsx', sheet_name='Info', index=False)
