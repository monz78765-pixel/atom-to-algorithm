atoms = float(input("Enter starting number of atoms: "))
half_life = float(input("Enter half-life in years: "))
periods = int(input("Enter number of half-lives: "))
print("\nHalf-lives passed | Remaining atoms")
print("----------------------------------")
for n in range(periods+1):
    remaining= atoms * (0.5 ** n)
     print(f"{n:<17} | {remaining:.2f}")
