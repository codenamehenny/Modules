# Task 1: Custom Module with Aliases 
#Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). 
# In your main script, import this module using an alias and utilize its functions.

import text_utils as utils

string = input("Enter a string: ").strip()
reversed_string = utils.reverse_string(string)
capitalized_string = utils.capitalize_string(string)
print(f"Reversed string is '{reversed_string}' and capitalized string is '{capitalized_string}'")
