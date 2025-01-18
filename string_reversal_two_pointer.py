# String Reversal Using the Two-Pointer Technique
# This technique is efficient as it avoids the overhead of creating new strings during reversal,
# unlike using string concatenation or append methods. It works by swapping characters
# within the same list, making it optimal for in-place modifications.

# Time Complexity: O(n) - Each character is processed once.
# Space Complexity: O(n) - A list is created to store the characters.

def reverse(input_string):
    """
    Reverses a given string using the two-pointer technique.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """

    # Strings in Python are immutable, so we convert the string to a list for swapping
    input_str = list(input_string)

    # Initialize pointers at the start and end of the list
    left, right = 0, len(input_str) - 1

    # Swap characters until pointers meet in the middle
    while left < right:
        # Swap characters at the left and right pointers
        input_str[left], input_str[right] = input_str[right], input_str[left]

        # Move pointers closer to the center
        left += 1
        right -= 1

    # Convert the modified list back into a string and return it
    return ''.join(input_str)

# Prompt the user for input and display the reversed string
ip = input("Enter the string to be reversed: ")
print(f"Reversed String: {reverse(ip)}")
