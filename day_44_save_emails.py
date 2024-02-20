import csv

def save_emails():
    file_name = "save_emails.csv"

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['email'])

        while True:
            input_email = input("Enter your email address to SAVE or type 'done' to finish: ")

            if input_email == "done":
                print("Saved emails")
                break
            else:
                writer.writerow([input_email])

def open_emails(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)

save_emails()
open_emails('save_emails.csv')
