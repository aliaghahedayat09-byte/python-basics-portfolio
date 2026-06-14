# greeting with users
greeting =input("Greeting: ").strip().lower()
# say to start with specific letter
if greeting.startswith("hello"):
    print("$0")

elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
