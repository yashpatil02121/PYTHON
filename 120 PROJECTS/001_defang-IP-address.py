# https://medium.com/coders-camp/120-python-projects-with-source-code-c913bb95bab8


# defang-> prevent user from clicking the malicious links
# eg-> http is replaced by hxxp

# def ip_address(address):
#     new_address=""
#     split_address=address.split(".")
#     separator="[.]"
#     new_address=separator.join(split_address)
#     return new_address
# ipaddress = ip_address("1.1.2.3")
# print(ipaddress)

def ip_address(address):
   new_address=address.replace(".","..")
   return new_address
ipaddress=ip_address("1.2.3.4")
print(ipaddress)