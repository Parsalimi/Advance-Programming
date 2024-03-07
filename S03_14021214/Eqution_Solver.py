from os import system
system('cls')


class main():
    #Equtions = [[5, '+', 10], [10, 'x', 20], [20, 'x', 5], [5, '/', 2.5], [2.5, '+', 10]]
    Equtions = [[5],['+'],[10],['x'],[20],['x'],[5],['/'],['2.5'],['+'],[10]]

print(main.Equtions)
for index, sub_eq in enumerate(main.Equtions):
    if sub_eq == "x":
        answer = main.Equtions[index-1] * main.Equtions[index+1]
# for index, sub_eq in enumerate(main.Equtions):
#     if sub_eq[1] == "x":
#         answer = sub_eq[0] * sub_eq[2]
#         main.Equtions.remove(sub_eq)
#         main.Equtions.insert(index, [0,answer,0])
#         if index >= 1:
#             main.Equtions[index-1][2] = answer
#             main.Equtions[index+1][0] = answer
        
#     elif sub_eq[1] == "/":
#         answer = sub_eq[0] / sub_eq[2]
#         main.Equtions.remove(sub_eq)
#         main.Equtions.insert(index, [0,answer,0])
#         if index >= 1:
#             main.Equtions[index-1][2] = answer
#             main.Equtions[index+1][0] = answer

# f_index = 0
# for sub_eq in main.Equtions:
#     if sub_eq[0] == 0 and sub_eq[2] == 0:
#         main.Equtions[0][2] = sub_eq[1]

print(main.Equtions)