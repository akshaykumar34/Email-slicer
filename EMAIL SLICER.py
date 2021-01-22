email=input("What is the email address:").strip()
user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "Your email is {} and your username is {} and domain is {}".format(email,user,domain)
print(output)