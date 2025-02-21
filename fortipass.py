import random

password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890aabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:"

length_password=int(input("Enter the length of the password:"))

x="".join(random.sample(password,length_password))

print(f"Your Password is {x}")