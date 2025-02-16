def adjust_ingredients():
    # Define the original recipe ingredients
    sugar = 1.5
    butter = 1
    flour = 2.75
    original_cookies = 48

    # Ask the user how many cookies they want to make
    desired_cookies = int(input("How many cookies do you want to make? "))

    # Calculate the scaling factor
    scaling_factor = desired_cookies / original_cookies

    # Calculate the adjusted ingredients
    adjusted_sugar = sugar * scaling_factor
    adjusted_butter = butter * scaling_factor
    adjusted_flour = flour * scaling_factor

    # Display the adjusted ingredients
    print(f"For {desired_cookies} cookies, you will need:")
    print(f"{adjusted_sugar:.2f} cups of sugar")
    print(f"{adjusted_butter:.2f} cups of butter")
    print(f"{adjusted_flour:.2f} cups of flour")

# Call the function
adjust_ingredients()


