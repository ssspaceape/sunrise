#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import time

rows = 32
chains = 2
parallel = 1
myMatrix = RGBMatrix(rows, chains, parallel)
myMatrix.Fill(255, 0, 0)
time.sleep(5)
myMatrix.Clear()