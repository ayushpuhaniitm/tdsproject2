# Importing necessary libraries
import streamlit as st

# Function to find the largest number among three
def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

# Streamlit app
def main():
    # Set the title and description
    st.title("Largest Number Finder")
    st.write("Enter three numbers, and we'll find the largest one!")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:", min_value=float('-inf'), max_value=float('inf'), step=1.0)
    num2 = st.number_input("Enter the second number:", min_value=float('-inf'), max_value=float('inf'), step=1.0)
    num3 = st.number_input("Enter the third number:", min_value=float('-inf'), max_value=float('inf'), step=1.0)

    # Find the largest number using the function
    largest_number = find_largest_number(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
