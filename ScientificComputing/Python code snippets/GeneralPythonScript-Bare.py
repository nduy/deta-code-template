
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

# Function definition    
def my_function():
 print(f"Hello World!")
 return (True);
class Parent:
    hair_color = "brown"
    speaks = ["English"]
    def __init__(self, name, age, skin_color):
        self.name = name
        self.age = age
        self.skin_color = skin_color


class Child(Parent):
    hair_color = "purple"
    def __init__(self):
        super().__init__()
        self.speaks = Parent.speaks + ["German"] #Inherit from parent
    

def main():
    print("Hello World!\n"+ __author__+ "\n"+ __copyright__)

if __name__ == "__main__":
    main()
    my_function()
    tom = Parent("Tom",40,"yellow")
    jerry= Child(tom)
    print(jerry.speaks);
    #print("Program completed!");
    
