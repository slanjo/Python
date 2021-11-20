################### Scope ####################

enemies = 1

def increase_enemies():
# In Python we can use globals 
# enemies = 2
# We Cannot however modify a global below line will not work
#  enemies += 1
  print(f"enemies inside function: {enemies}")
#We CAN however return the modified global variable
  return enemies + 5
print(f"Modified global variable: {increase_enemies()}")
print(f"enemies outside function: {enemies}")
def drink_potion():
  potion_strength = 2
  print(potion_strength)
drink_potion()

for _ in range(5):
  print("Looping")