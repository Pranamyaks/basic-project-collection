def shpppingBillGenerator(filename):
    grand_total=0
    with open(filename,'r') as file:
        for line in file:
            data=line.split()
            item=data[0]
            quantity=int(data[1])
            price=int(data[2])
            total=quantity*price
            grand_total+=total
            print(f"{item}-{quantity}*{price}={total}")
        print(f"Total Bill:{grand_total}")        
        
shpppingBillGenerator("shop.txt")        
