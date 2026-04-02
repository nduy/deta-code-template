
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
# Class definition
      

# Function definition    
def my_function():
 print(f"Hello World!")
 
 return (True);


def main():
   # print("Hello World!\n"+ __author__+ "\n"+ __copyright__)

    miles = Dog("Miles", 4, "Jack Russell Terrier")
    buddy = Dog("Buddy", 9, "Dachshund")
    bob= BabyDog(buddy)
    jack = Dog("Jack", 3, "Bulldog")
    jim = Dog("Jim", 5, "Bulldog")
    
    
    ### Test speak:
    print(buddy.speak("Yap"))
    print(jim.speak("Woof"))
    print(jack.speak("Woof"))
    print(bob.speak("Sh!! Woof"))
    
if __name__ == "__main__":
    main()
    my_function()
    print("Program completed!");
    
