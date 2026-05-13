# Day 12 Mastery: Lists, Loops, and Logic
# Date: 2026-05-13
# Goal: Consolidate Tutorial 4 concepts for GitHub portfolio

def main():
    # --- LIST MANIPULATION ---
    # Combining lists using .extend()
    current_stack = ["Python", "VS Code", "GitHub"]
    future_goals = ["APIs", "Backend", "SaaS"]
    current_stack.extend(future_goals)
    
    # Adding items by location with .insert()
    current_stack.insert(0, "Logic Mastery") 
    
    # --- SORTING & MATH ---
    # Sorting alphabetically (Permanent change)
    current_stack.sort()
    
    # Using .pop() to remove and store the first alphabetical item
    first_item = current_stack.pop(0)
    
    # Math operations on a numeric list
    progress_days = [10, 11, 12]
    total_days = sum(progress_days)
    max_day = max(progress_days)

    # --- LOOPING & ENUMERATION ---
    print(f"--- Day {max_day} Progress Report ---")
    print(f"I have studied for a total of {total_days} hours across recent days.\n")
    
    print("Updated Skill Stack:")
    # Using enumerate to show ranking/count
    for rank, skill in enumerate(current_stack, start=1):
        print(f"{rank}. {skill}")

    # --- STRING "GLUE & SCISSORS" ---
    # Joining the list into a single string
    stack_string = " | ".join(current_stack)
    print(f"\nJoined Stack String: {stack_string}")
    
    # Splitting it back into a list
    split_verification = stack_string.split(" | ")
    
    # --- CHECKING MEMBERSHIP ---
    if "Python" in split_verification:
        print("\nVerification: Python is confirmed in the stack! ✅")

if __name__ == "__main__":
    main()