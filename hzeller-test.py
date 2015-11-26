#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import time

rows = 16
chains = 1
parallel = 2
myMatrix = RGBMatrix(rows, chains, parallel)
myMatrix.Fill(255, 0, 0)
time.sleep(5)
myMatrix.Clear()