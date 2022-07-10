company_name = 'Thecleverprogrammer, inc.'
company_address = '144 Kalka ji.'
company_city = 'New Delhi'

product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 598.99
product3_name, product3_price = 'Monitor', 156.89

print(50*"*")

print(f"\t\t{company_name}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

print(50*"=")

print(f"\tProduct Name\tProduct Price")
print(f"\t{product1_name}\t\t{product1_price}")
print(f"\t{product2_name}\t{product2_price}")
print(f"\t{product3_name}\t\t{product3_price}")

print(50*"=")

print(f"\t\t\tTotal")
print(f"\t\t\t{product1_price+product2_price+product3_price}")

print(50*"=")

print(f"\n\tThanks for shopping with us today!\n")
print(50*"*")

with open("Create an Invoice/Invoice.txt","w") as data_file:
    data_file.write(50*"*")

    data_file.write(f"\n\t\t{company_name}")
    data_file.write(f"\n\t\t{company_address}")
    data_file.write(f"\n\t\t{company_city}\n")

    data_file.write(50*"=")

    data_file.write(f"\n\tProduct Name\tProduct Price")
    data_file.write(f"\n\t{product1_name}\t\t{product1_price}")
    data_file.write(f"\n\t{product2_name}\t{product2_price}")
    data_file.write(f"\n\t{product3_name}\t\t{product3_price}\n")

    data_file.write(50*"=")

    data_file.write(f"\n\t\t\tTotal")
    data_file.write(f"\n\t\t\t{product1_price+product2_price+product3_price}\n")

    data_file.write(50*"=")

    data_file.write(f"\n\n\tThanks for shopping with us today!\n\n")
    data_file.write(50*"*")

