
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
"address@example.com"
__status__ = "Production" # Planning, Analysis, Design, Production, Testing, Deployment, and Maintenance
# ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
### Import libraries
# Data representation & manipulation
import numpy as np # Fundament
import pandas # for working with data set; has functions for analyzing, cleaning, exploring, and manipulating data.
import matplotlib.pyplot as plt # a comprehensive library for creating static, animated, and interactive visualizations in Python
import seaborn as sns # data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
# Machine Learning & Deep learning
import sklearn # build ML models and it is not recommended to use it for reading, manipulating and summarizing data as there are better frameworks available for the purpose. 
    #It is open source and released under BSD license.
import tensorflow as tf # an open-source library for numerical computation, large-scale machine learning, deep learning, and other statistical and predictive analytics workloads
#a high-level, open-source Python API for building and training deep learning models, known for being user-friendly, modular, and fast to prototype. 

import tensorflow as tf; 
from tensorflow.python.keras.layers import Input, Dense     #It serves as an interface for backend engines like TensorFlow, JAX, or PyTorch, allowing users to build complex neural networks with minimal code.

import torch #  an open-source machine learning framework that is known for its flexibility, ease of use, and performance in modern AI applications, especiall Computer Vision applications

def main():
    print("Hello World!\n"+ __author__+ "\n"+ __copyright__)

if __name__ == "__main__":
    main()