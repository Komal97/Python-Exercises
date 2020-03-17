import re


# Phone number validation
phn = "412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}", phn):
    print("It is a phone  number")
 
    
# Full name validation
name = "Komal Bansal"
if re.search("\w{2,20}\s\w{2,20}", name):
    print("Full name is valid")
    

# Email validation
email = "sk@aol.com md@.com @seo.com dc@.com"
print("Email matches: ", re.findall("[\w._%+-]{1,20}@[\w.]{2,20}.[a-zA-Z]{2,3}", email))