log_file = open("um-server-01.txt") #opens the server file


def sales_reports(log_file): # creates a function named sales_reports
    for line in log_file: # loops through each line in the um-server file
        line = line.rstrip() # rstrip method removes all of the extra spaces on the right side of the string.
        day = line[0:3] # this line sets the day = to the first 3 letters in the line
        if day == "Mon":# checks if the first 3 letters = Tue, I changed it to Mon
            print(line)# only prints out for every line that is from a tuesday. Now it only shows the reports for Monday.

sales_reports(log_file) #runs the function