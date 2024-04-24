# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Assign `remove_list` to a list of IP addresses that are no longer allowed access to restricted information
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build iterative statement to loop through `ip_addresses` and remove restricted IP addresses
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)

# Rewrite original file with updated data
with open(import_file, "w")as file:
    file.write(ip_addresses)
