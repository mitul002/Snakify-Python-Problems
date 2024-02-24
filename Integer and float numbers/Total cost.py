A = int(input("Cost in dollars: "))
B = int(input("Cost in cents: "))
N = int(input("Number of cupcakes: "))

Tot_Cent = A * 100 + B
total_cost_cents = N * Tot_Cent

total_dollars = total_cost_cents // 100
remaining_cents = total_cost_cents % 100

print(total_dollars,remaining_cents)