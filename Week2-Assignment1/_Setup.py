#%# imports

import os, sys

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import random
import seaborn as sns
import time
from statistics import mean

codePath = os.path.abspath('.')

projPath = os.path.dirname(codePath)

assignmentPath = os.path.join(projPath, "Week2-Assignment1")

dataPath = os.path.join(assignmentPath, "Data")
rawDataFilePath = os.path.join(dataPath, "Fish.csv")
print(rawDataFilePath)