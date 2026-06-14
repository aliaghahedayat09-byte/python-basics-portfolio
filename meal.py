#ask users for time
def main():
    time = input("What is the time? ")
    hours = convert(time)
    # make condition for each time
    if 7.0 <= hours >= 8.0:
        print("breakfast time")
    elif 12.0 <= hours >= 13.0:
        print("lunch time")
    elif 18.0 <= hours >= 19.0:
        print("dinner time")
    
 #changing to float      
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes= float(minutes)
    return hours + minutes/60





#call the funtion 

main()

