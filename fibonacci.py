print(f"Welcome to Fibonacci series")
print(f"Please enter the  range below")
b=int(input("--> "))
fibonacci_series = []
def fibonacci_logic(count):
    series=[]
    series.insert(0,0)
    series.insert(1,1)
    for i in range(2,count):
             series.insert(i,int(series[i-1])+ int(series[i-2]))
    return (series)

fibonacci_series=fibonacci_logic(b)
print(fibonacci_series)