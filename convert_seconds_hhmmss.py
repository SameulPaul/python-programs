    timeinsec = int(input("Enter Time in Seconds: "))

    hh = timeinsec//3600
    remainingseconds = timeinsec%3600
    mm = remainingseconds//60
    ss = remainingseconds%60

    print("Time in hh mm ss is: ", hh, "Hours,", mm, "Minutes and", ss, "Seconds")
