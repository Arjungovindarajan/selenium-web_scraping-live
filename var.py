import os

# passd = os.environ.get('Gmail_pass')
os.environ['Gmail_pass'] = 'Arjun@123'

for key, value in os.environ.items():
    # if key == ['Gmail_pass']:
    #     print(value)

    print(f'{key}: {value}')
# sender_pass = os.environ.get('Gmail_pass')
# print("Gmail_pass environment variable:", sender_pass)

# print(passd)