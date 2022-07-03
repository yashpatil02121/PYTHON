from tabulate import tabulate
data= [["Name","Place","Gender"],["Aman","New Delhi","Male"],["Hritika","New Delhi","Female"],["Krishna","UP","Male"]]
print("type 1\n"+tabulate(data))
print("\n\ntype 2\n"+tabulate(data,headers='firstrow'))
print("\n\ntype 3\n"+tabulate(data, headers='firstrow', tablefmt='grid'))
print("\n\ntype 4\n"+tabulate(data, headers='firstrow', tablefmt='fancy_grid'))