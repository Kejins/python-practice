def time(seconds):
    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    remain = seconds
    print(f"That can be simplified to {hours} hours {minutes} minutes and {seconds} seconds")

conversion = int(input("Enter how many seconds you'd like to convert: "))
time(conversion)
