class Item:
    def __init__(self,value, weight):
        self.value = value
        self.weight = weight
        
def fractional_knapsack(capacity,items):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    
    final_value = 0.0
    
    for item in items:
        
        # Full item
        if item.weight <= capacity:
            capacity -= item.weight
            final_value += item.value
            
        # Fractional part
        else:
            final_value += item.value * (capacity / item.weight)
            break
        
    return final_value
            

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    items = []
    
    for _ in range(n):
        value = float(input("Enter value of item: "))
        weight = float(input("Enter weight of item: "))
        items.append(Item(value, weight))
        
    capacity = float(input("Enter capacity of knapsack: "))
    
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack = {max_value}")