inventory = {
    "Banana" : {"Price": 0.70, "Quantity" : 5},
    "Bread" : {"Price" : 1.50 , "Quantity" : 7},
    "Apple" : {"Price" : 0.35 , "Quantity" : 2},
    "Jam" : {"Price" : 3.45 , "Quantity" : 15},
}
def check_low_stock(threshold):
    low = ""
    for item , info in inventory.items():
        if(info["Quantity"] < threshold):
            low += item + " "
    print(low)

check_low_stock(6)