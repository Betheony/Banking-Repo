while True:
  try:
    ans = int(input("Hello, how old are you? (type stop to end)   \n"))
    ans = int(ans)
    break
  except ValueError:
    print('You can only put a number.')
    
if ans < 18:
    ans = input("Go do your homework! \n")
elif ans >= 18 and ans < 50:
  ans = input("How is your life? \n") 
elif ans >= 50 and ans < 100:
  ans = input("Do you have grandkids? \n") 
else:
  ans = input("Woah you're old. How is life? \n") 
while ans != "stop":
  ans =  input("Sounds alright.\n")