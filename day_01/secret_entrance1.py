import requests

# loading input from advent of code url

url = "https://adventofcode.com/2025/day/1/input"
cookies = {'session': '53616c7465645f5f1294e894efd04c9ae5fbf8941f8b3e0cf34b8b1690b2c142cb9829bdc720294cde65b0df0d802671b56cef542684142cf0e71b26012f48e8'}

response = requests.get(url, cookies=cookies)
data = response.text

# Save to file
with open('inputs/day01.txt', 'w') as f:
    f.write(data)

print("Input saved to inputs/day01.txt")
print(len(data))

# print(data)