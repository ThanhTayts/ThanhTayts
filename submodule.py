def email_process(email):
    email_username = email[0:email.index('@')]
    email_domain = email[email.index('@')+1:]
    return [email_username,email_domain]

def print_email(email_username, email_domain):
    print(f"User name is {email_username} , Domain is {email_domain}")



def main():
    email = input("please enter your email address: ").strip()
    email_username, email_domain = email_process(email)
    print_email(email_username, email_domain)

# main()
if __name__ == "__main__": 
    main()
