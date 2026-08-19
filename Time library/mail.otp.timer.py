import random
import smtplib
import time

# User email input
user_email = input("Enter your email: ")

# OTP generate
otp = random.randint(100000, 999999)

# OTP validity (seconds)
otp_validity = 120
start_time = time.time()

# Sender details
sender_email = "Your_email_id"
sender_password = "Your_app_password"

# Email message
message = f"Subject: OTP Verification\n\nYour OTP is: {otp}\nValid for 30 seconds."

# Send email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, user_email, message)
server.quit()

print("OTP sent!✅\n It is valid for 30 seconds ⏱")

# User OTP input
user_otp = int(input("Enter OTP: "))

# Check time difference
current_time = time.time()

if current_time - start_time <= otp_validity:
    if user_otp == otp:
        print("OTP Verified ✅")
    else:
        print("Invalid OTP ❌")
else:
    print("OTP Expired ⛔")
