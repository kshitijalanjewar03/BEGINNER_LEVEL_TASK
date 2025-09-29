total_jumping_jacks = 100
set_size = 10
completed = 0

while completed < total_jumping_jacks:
    print(f"\nPerform {set_size} jumping jacks.")
    completed += set_size
    
    # Ask if tired
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        elif skip in ['no', 'n']:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks are remaining.")
            # Continue the loop without breaking
        else:
            print("Invalid response, continuing workout.")
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks are remaining.")
            
    elif tired in ['no', 'n']:
        remaining = total_jumping_jacks - completed
        if remaining > 0:
            print(f"{remaining} jumping jacks are remaining.")
        else:
            print("Congratulations! You completed the workout.")
            break
    else:
        print("Invalid response, continuing workout.")
        remaining = total_jumping_jacks - completed
        if remaining > 0:
            print(f"{remaining} jumping jacks are remaining.")
        else:
            print("Congratulations! You completed the workout.")
            break

else:
    # This else runs if the while loop completes normally (not broken)
    print("Congratulations! You completed the workout.")
