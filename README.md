# Python-Algorithms
Algorithm for File Updates in Python (Google Project)

### Project description
My company has tasked me with handling Identity and Access Management (IAM) security and regularly updating a file that identifies the employees who can access restricted personal patient records. Access is restricted by IP addresses on an “allow list”, however there is a “remove list” for any IP addresses that should no longer have authorization to the file. I have created an algorithm to automate this process of updating and removing IP addresses from this file.

### Open the file that contains the allow list
First I assign the file name to a variable.

```
# Assign `import_file` to the name of the file`

import_file = "allow_list.txt"
```
Next I open this file using a `with` statement to ensure the file only remains open while inside this statement for my use. 

```
# First line of `with` statement

with open(import_file, "r") as file:
```
The parameters of the `open()` function indicates the file to import as well as what I want to do with this file, in this case the `“r”` allows me to read the file.

### Read the file contents
To read the file contents I use the `read()` method on the variable `file` created by the `open` function. This method reads the file contents and converts the output into a string which I have saved into a variable named `ip_addresses`.

```
# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

  ip_addresses = file.read()
```

### Convert the string into a list
To make it easier to work with the file content I converted this string into a list using the `split()` method and saved it as the same variable of `ip_addresses`.

```
# Use `.split()` to convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()
```

### Iterate through the remove list
I need to iterate through the list I have created to work with each item separately. To do this I use a `for` loop which iterates through each item in the `ip_addresses` list and saves it to the `element` variable while in the `for` loop.

```
# Build iterative statement
# Name loop variable `element'
# Loop through `ip_addresses`

for element in ip_addresses:
```
### Remove IP addresses that are on the remove list
Any IP addresses on the `remove_list` then need to be removed from the `ip_addresses` list which was created from the “allow list” 

```
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
```
To do this I use the `for` loop to iterate through each element in the `ip_addresses` list and using a conditional `if` statement to check if any IP addresses are also in the `remove_list`. If they do appear in the `remove_list` they are taken out using the `remove()` method.

```
# Build conditional statement
# If current element is in the `remove_list`,

if element in remove_list:

  # then current element should be removed from `ip_addresses`

  ip_addresses.remove(element)
```

### Update the file with the revised list of IP addresses 
Finally the “allow list” needs to be updated after being revised. The list first needs to be converted back to a string using the `join()` method. This method takes all items from an iterable and joins them into one string. I used “” to specify the items should be separated by a space.

```
# Convert `ip_addresses` back to a string so that it may be written to a text file

ip_addresses = " ".join(ip_addresses)
```

Now with the revised `ip_addresses` back as a string it can be written back into the original file replacing the content. Using a `with` statement I again `open()` the file this time using the `“w”` argument to write into the file as opposed to reading it.

```
# Build `with` statement to rewrite the original file

with open(import_file, "w")as file:

  # Rewrite the file, replacing its content with `ip_addresses`

  file.write(ip_addresses)
```


Using the `write()` method with the `ip_addresses` argument the revised content is written into the original file without the IP addresses that no longer have access.

### Summary

I was able to create an algorithm automating the process of removing IP addresses that no longer have access to a restricted file. I opened the `“allow_list”` file and read the contents. Then converted that content from a string into a list so it could be iterated through in a `for` loop. Using the given `remove_list` which contained the IP addresses that no longer have access to the file I created a conditional `if` statement to check for any IP addresses in the list that matched ones from the `remove_list`. After removing these, the file was updated with the revised content by using the `join()` method to convert the list back to a string and the `write()` method to replace the contents of the `“allow_list”` file.





