# from faker import Faker
# fake = Faker('en_US')
# # print(fake)
import shutil
import re

def get_content(location):
    with open(location, "r") as file:
        content = file.read()
        return content

def write_to_file(data, path):
    result = ""
    for item in data:
        result += item + "\n"
    with open(path, "w") as new_file:
        new_file.write(result)


def find_phone_numbers(content):
    phone_pattern = r"[0-9-+x.()]{7,}"
    phone_numbers = []

    numbers = re.findall(phone_pattern, content)
    for number in numbers:
        number = number.replace(".", "").replace("-", "").replace("(", "").replace(")", "")
        if len(number) == 10:
            number = number[:3] + "-" + number[3:6] + "-" + number[6:]
        phone_numbers.append(number)

    phone_numbers = list(set(phone_numbers))
    phone_numbers.sort()
    return phone_numbers

def find_emails(content):
    email_pattern = r"\S+@\S+"
    emails = re.findall(email_pattern, content)
    emails = list(set(emails))
    emails.sort()
    return emails

if __name__ == "__main__":
  content  = get_content("data/potential-contacts.txt")
  phone_numbers = find_phone_numbers(content)
  emails = find_emails(content)
  write_to_file(emails, "data/emails.txt")
  write_to_file(phone_numbers, "data/phone_numbers.txt")