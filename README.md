# Python-Algorithms
Algorithm for File Updates in Python (Google Project)

### Project description
My company has tasked me with handling Identity and Access Management (IAM) security and regularly updating a file that identifies the employees who can access restricted personal patient records. Access is restricted by IP addresses on an “allow list”, however there is a “remove list” for any IP addresses that should no longer have authorization to the file. I have created an algorithm to automate this process of updating and removing IP addresses from this file.

### Open the file that contains the allow list
First I assign the file name to a variable.

<img width="285" alt="Screen Shot 2024-02-16 at 1 05 28 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/a774c6ef-9dba-4e83-8dbe-41aa805a3124">

Next I open this file using a `with` statement to ensure the file only remains open while inside this statement for my use. 

<img width="272" alt="Screen Shot 2024-02-16 at 1 08 32 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/059493f3-46cd-477f-bc07-b8be51ca25c9">

The parameters of the `open()` function indicates the file to import as well as what I want to do with this file, in this case the `“r”` allows me to read the file.

### Read the file contents
To read the file contents I use the `read()` method on the variable `file` created by the `open` function. This method reads the file contents and converts the output into a string which I have saved into a variable named `ip_addresses`.

<img width="468" alt="Screen Shot 2024-02-16 at 1 09 09 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/fba1e3ba-4e27-46e7-9fff-e41ce0d98030">

### Convert the string into a list
To make it easier to work with the file content I converted this string into a list using the `split()` method and saved it as the same variable of `ip_addresses`.

<img width="468" alt="Screen Shot 2024-02-16 at 1 09 43 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/679849af-28f4-411b-8601-40e4de055393">

### Iterate through the remove list
I need to iterate through the list I have created to work with each item separately. To do this I use a `for` loop which iterates through each item in the `ip_addresses` list and saves it to the `element` variable while in the `for` loop.

<img width="294" alt="Screen Shot 2024-02-16 at 1 10 11 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/ec89aa15-e300-4a1f-8c71-222e8d6fbb13">

### Remove IP addresses that are on the remove list
Any IP addresses on the `remove_list` then need to be removed from the `ip_addresses` list which was created from the “allow list” 

<img width="500" alt="Screen Shot 2024-02-16 at 1 12 04 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/a4f89f4b-3d5b-4fa3-8fe6-ba8bd225bde5">

To do this I use the `for` loop to iterate through each element in the `ip_addresses` list and using a conditional `if` statement to check if any IP addresses are also in the `remove_list`. If they do appear in the `remove_list` they are taken out using the `remove()` method.

<img width="366" alt="Screen Shot 2024-02-16 at 1 12 40 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/e8da4919-8b09-436f-a97e-e0e93c17a585">

### Update the file with the revised list of IP addresses 
Finally the “allow list” needs to be updated after being revised. The list first needs to be converted back to a string using the `join()` method. This method takes all items from an iterable and joins them into one string. I used “” to specify the items should be separated by a space.

<img width="467" alt="Screen Shot 2024-02-16 at 1 13 02 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/599ee77e-1370-4d55-944c-ceb5667f0126">

Now with the revised `ip_addresses` back as a string it can be written back into the original file replacing the content. Using a `with` statement I again `open()` the file this time using the `“w”` argument to write into the file as opposed to reading it.

<img width="398" alt="Screen Shot 2024-02-16 at 1 13 47 PM" src="https://github.com/jwsummers/Python-Algorithms/assets/22925230/9932589d-d537-4ad0-9f55-1eade424069b">


Using the `write()` method with the `ip_addresses` argument the revised content is written into the original file without the IP addresses that no longer have access.

### Summary

I was able to create an algorithm automating the process of removing IP addresses that no longer have access to a restricted file. I opened the `“allow_list”` file and read the contents. Then converted that content from a string into a list so it could be iterated through in a `for` loop. Using the given `remove_list` which contained the IP addresses that no longer have access to the file I created a conditional `if` statement to check for any IP addresses in the list that matched ones from the `remove_list`. After removing these, the file was updated with the revised content by using the `join()` method to convert the list back to a string and the `write()` method to replace the contents of the `“allow_list”` file.





