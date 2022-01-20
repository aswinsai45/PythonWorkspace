emailID = tuple()
user = tuple()
domain = tuple()

n = int(input("How many emailID ids you want to enter?: "))
for i in range(0, n):
    email = input("Enter the Email(s) here: ")

    emailID = emailID + (email,)

    split = email.split("@")
    user = user + (split[0],)
    domain = domain + (split[1],)

print("\nEmails: ")
print(emailID)

print("\nUsers:")
print(user)

print("\ndomains:")
print(domain)
