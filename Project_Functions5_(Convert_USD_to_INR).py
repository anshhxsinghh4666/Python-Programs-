# WAF to convert USD to INR. (1USD = 84.04INR)

def USD(n):
    INR=n*84.04
    print("Amount in INR: ", INR)
    # OR
    print(n, "USD=" , INR, "INR" )
    return INR

USD(10) #10USD in INR

# OR (Without using function)

USD = float(input("Enter the amount in USD: "))
INR = USD * 84.04
print("Amount in INR: ", INR)

