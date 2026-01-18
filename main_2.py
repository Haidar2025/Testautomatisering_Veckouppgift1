# ===================================
# Veckouppgift 1 - Section 2
# Code Review Exercise
# ===================================

# Original buggy code (commented out):
# x = 100  # biljettpris
# y = 200  # pengar på fickan
# print("Det blir " + (y - x) " kronor över.")
# z = y - x / 2
# print("Varye person får " + z)

# Fixed code with better variable names:
print("--- Biljett beräkning ---")
biljettpris = 100
pengar_pa_fickan = 200

# Fix 1 & 3: Use str() to convert numbers to strings
pengar_over = pengar_pa_fickan - biljettpris
print("Det blir " + str(pengar_over) + " kronor över.")

# Fix 2: Use parentheses to get correct order of operations
per_person = (pengar_pa_fickan - biljettpris) / 2
print("Varje person får " + str(per_person) + " kronor.")
