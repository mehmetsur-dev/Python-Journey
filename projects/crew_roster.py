# (remove) and (f"{string}")

# 1. Use square brackets [] for a list!
crew = ["Captain", "Pilot", "Engineer", "Medic"]


# 2. Close the quote at the end of the f-string
print(f"The crew member is: {crew[1]}")


# 3. This works now because we used [] above    
crew.append("Scientist")

# 4. Removing the Medic (at index 3) or Pilot (index 1)
crew.remove("Engineer")


# 5. The loop: indent the print and use the 'item' variable
for item in crew:
    print(item)
