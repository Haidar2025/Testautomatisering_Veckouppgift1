# ===================================
# Veckouppgift 1 - Section 4
# Advanced Exercises
# ===================================

import math
from datetime import datetime, timedelta

# --- Exercise 1a: Travel time Stockholm to Göteborg (in hours) ---
print("--- Övning 1a: Restid Stockholm-Göteborg (i timmar) ---")
avstand = 470  # km
hastighet = float(input("Hur fort ska du köra? (km/h): "))
tid_timmar = avstand / hastighet
print("Det tar " + str(tid_timmar) + " timmar att köra från Stockholm till Göteborg.")

# --- Exercise 1b: Travel time in minutes ---
print("\n--- Övning 1b: Restid i minuter ---")
tid_minuter = tid_timmar * 60
print("Det tar " + str(tid_minuter) + " minuter att köra från Stockholm till Göteborg.")

# --- Exercise 1c: Travel time in hours and minutes ---
print("\n--- Övning 1c: Restid i timmar och minuter ---")
hela_timmar = int(tid_timmar)  # Get whole hours using int() which rounds down
resterande_minuter = int((tid_timmar - hela_timmar) * 60)
print("Det tar " + str(hela_timmar) + " timmar och " + str(resterande_minuter) + " minuter.")

# Alternative method using // and %:
total_minuter = int(avstand / hastighet * 60)
timmar = total_minuter // 60  # Integer division
minuter = total_minuter % 60   # Modulo (remainder)
print("Alternativ beräkning: " + str(timmar) + " timmar och " + str(minuter) + " minuter.")

# --- Exercise 2: Pythagoras' theorem (hypotenuse) ---
print("\n--- Övning 2: Pythagoras sats (hypotenusa) ---")
sida_a = float(input("Ange längden på första sidan: "))
sida_b = float(input("Ange längden på andra sidan: "))
hypotenusa = math.sqrt(sida_a**2 + sida_b**2)
print("Hypotenusan är: " + str(hypotenusa))
print("\nTestdata: Om du anger 3 och 4, ska svaret bli 5.0")

# --- Exercise 3a: Today's date ---
print("\n--- Övning 3a: Dagens datum ---")
idag = datetime.now()
print("Dagens datum är: " + idag.strftime("%Y-%m-%d"))
print("Eller på svenska: " + idag.strftime("%d/%m/%Y"))

# --- Exercise 3b: Date in 7 days ---
print("\n--- Övning 3b: Datum om 7 dagar ---")
om_sju_dagar = idag + timedelta(days=7)
print("Om 7 dagar är det: " + om_sju_dagar.strftime("%Y-%m-%d"))
print("Eller på svenska: " + om_sju_dagar.strftime("%d/%m/%Y"))
