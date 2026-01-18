# ===================================
# Veckouppgift 1 - Section 3
# Variables and Data Types
# ===================================

# --- Part 1a: Input and convert to integer ---
print("--- Del 1a: Ett heltal ---")
tal1 = input("Skriv in ett heltal: ")
tal1 = int(tal1)  # Convert string to integer
print("Du skrev in: " + str(tal1))

# --- Part 1b: Sum of two integers ---
print("\n--- Del 1b: Summa av två heltal ---")
tal2 = input("Skriv in ett annat heltal: ")
tal2 = int(tal2)  # Convert string to integer
summa = tal1 + tal2
print("Summan av " + str(tal1) + " och " + str(tal2) + " är: " + str(summa))

# --- Part 2a: Jacket discount calculator (fixed percentage) ---
print("\n--- Del 2a: Jacka på rea (75% av originalpris) ---")
pris = 2000  # Original price in kronor
rea_procent = 75.0  # Percentage of original price you pay
slut_pris = pris * rea_procent / 100
print("Originalpris: " + str(pris) + " kr")
print("Du betalar " + str(rea_procent) + "% av priset")
print("Slutpris: " + str(slut_pris) + " kr")

# --- Part 2b: User inputs discount percentage ---
print("\n--- Del 2b: Jacka på rea (användaren väljer rabatt) ---")
rabatt_procent = float(input("Hur många procent rabatt? (t.ex. 10 för 10% rabatt): "))
rabatt_belopp = pris * rabatt_procent / 100
slutpris = pris - rabatt_belopp
print("Originalpris: " + str(pris) + " kr")
print("Rabatt: " + str(rabatt_procent) + "% vilket är " + str(rabatt_belopp) + " kr")
print("Du betalar: " + str(slutpris) + " kr")
