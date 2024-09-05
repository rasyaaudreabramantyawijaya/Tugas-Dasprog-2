# Prompt user for input for fun1
user_input = input("Enter T for true or F for false: ").strip().upper()
fun1_result = 1 if user_input == 'T' else 0

# fun2 always returns 1
fun2_result = 1
print("fun2 executed")  # Simulating the output of fun2

# Testing && (logical AND)
print("Testing &&")
if fun1_result and fun2_result:
    print("Test of && complete")

# Testing || (logical OR)
print("Testing ||")
if fun1_result or fun2_result:
    print("Test of || complete")