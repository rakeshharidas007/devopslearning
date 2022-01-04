from calc2 import action

hra=13000
lta=3000
basic=6000
qvp=8000
tax=1000
allowance=action(lta, hra, '+')
gross_sal=action(allowance, basic, '+')
net_sal=action(gross_sal, tax, '-')
print(f"your net salary is only {net_sal}")