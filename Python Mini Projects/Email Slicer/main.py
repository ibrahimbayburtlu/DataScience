email = input("Enter your Email:").strip()

userName = email[:email.index("@")]
domainName = email[email.index("@")+1:]

format = f"Your user name is {userName} and your domain is {domainName}"
print(format)

