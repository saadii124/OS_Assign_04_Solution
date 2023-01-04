import threading

# Global variable to store the input string
input_str = ""

# Thread to take input from the user
def input_thread():
  global input_str
  try:
    input_str = input("Enter an input thread string: ")
  except Exception as e:
    print("Exception in input thread:", e)

# Thread to reverse the string
def reverse_thread():
  global input_str
  try:
    print("The reversed thread string: ", input_str[::-1])
  except Exception as e:
    print("Exception in reverse thread:", e)

# Thread to capitalize the string
def capital_thread():
  global input_str
  try:
    print("The capitalized thread string: ", input_str.upper())
  except Exception as e:
    print("Exception in capital thread:", e)

# Thread to shift the characters of the string
def shift_thread():
  global input_str
  try:
    shifted_str = ""
    for ch in input_str:
      shifted_str += chr(ord(ch) + 2)
    print("The shifted thread string: ", shifted_str)
  except Exception as e:
    print("Exception in shift thread:", e)

# Create and start the threads
input_t = threading.Thread(target=input_thread)
reverse_t = threading.Thread(target=reverse_thread)
capital_t = threading.Thread(target=capital_thread)
shift_t = threading.Thread(target=shift_thread)

input_t.start()
input_t.join()

reverse_t.start()
capital_t.start()
shift_t.start()

# Wait for all threads to finish
reverse_t.join()
capital_t.join()
shift_t.join()
