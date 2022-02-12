# import smtplib
# import ssl


# def read_creds():
#     user = passw = receiver = ""
#     with open(".credentials.txt", "r") as f:
#         file = f.readlines()
#         user = file[0].strip()
#         passw = file[1].strip()
#         receiver = file[2].strip()
#     return user, passw, receiver


# port = 465

# sender, password, receiver = read_creds()

# message = """|
# Subject: Peak morning call
# Hello Tim,
# This is your 07.45 morning message 'Hello Peak!'
# Have a good day! :)
# Best regards,
# Joel
# """

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smpt.gmail.com", port, context=context) as server:
#     server.login(sender, password)
#     server.sendmail(sender, receiver, message)

with open("message.txt", "a") as file:
    file.write("Hello Peak!")
    file.close()

print("Hello Peak!!")
