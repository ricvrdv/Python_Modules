'''
Count the days to harvest recursively.
'''

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days_recursion(1, days)

def count_days_recursion(current, last):
    if current > last:
        print("Harvest time!")
        return
    print(f"Day {current}")
    count_days_recursion(current + 1, last)
