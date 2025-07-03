##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime
import pandas
import random
today = datetime.datetime.now()
today_tuple = (today.month , today.day)
birthday_data = pandas.read_csv("C:/Users/shruti/python tutorial/new_folder/100days/day32/birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for(index,data_row) in birthday_data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"C:/Users/shruti/python tutorial/new_folder/100days/day32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        my_email= "appbrewery97@gmail.com"
        password="jwrj qwse puhd skkt"
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject : Happy Birthday!\n\n{content}") 



