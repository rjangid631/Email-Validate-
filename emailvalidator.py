import re
import dns.resolver


def is_valid_email(email):
    # Define a regular expression for a valid email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the regular expression
    if not re.match(email_regex, email):
        return False

    # Split the email address to get the domainr
    _, domain = email.split('@')

    # Check if the domain has valid DNS records
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except dns.resolver.NXDOMAIN:
        return False


if __name__ == "__main__":
    # Example usage
    email_to_check = input("Enter an email address: ")

    if is_valid_email(email_to_check):
        print(f"{email_to_check} is a valid email address.")
    else:
        print(f"{email_to_check} is not a valid email address.")
