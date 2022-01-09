from submodule import email_process,print_email


def main():
    emails = ['thanhtay@gmail.com','yoututu@tv.dev','xnxn@69.com']
    for email in emails:
        user_name, email_domain = email_process(email)
        print_email(user_name,email_domain)



if __name__ == "__main__":
    main()