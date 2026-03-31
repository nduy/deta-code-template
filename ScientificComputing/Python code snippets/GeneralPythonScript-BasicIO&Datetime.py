
#!/usr/bin/env python3

"""MyScript.py: Description of what The program does."""
### Project Key Info
__author__      = "DDNg"
__copyright__   = "Copyright 2009, Planet Earth"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "address@example.com"
__status__ = "Production" # Planning, Analysis, Design, Production, Testing, Deployment, and Maintenance
__initialisation_date__ = "Jan 1,2001"
__estimated_complete_date__ = "June 6, 2001"
# ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
from datetime import datetime
now = datetime.now()
# Function definition    
def my_function():
 name = input("Enter your name: ")
 print(f"Hello, {name}!")
 return (True)


def main():
    print("Hello World!\n"+ __author__+ "\n"+ __copyright__)

if __name__ == "__main__":
    main()
    my_function()
    print("Program completed at "+ str(now));
    
