from PyRatBox import *
from PyRatEllipsoid import PyRatEllipsoid
from PyRatRay import PyRatRay
from PyRatCylinder import PyRatCylinder
from PyRatFacet import PyRatFacet
from PyRatSpheroid import PyRatSpheroid
from PyRatDisk import PyRatDisk
from PyRatPlane import PyRatPlane
from PyRatObjParser import PyRatObjParser
try:
  import pp
except:
  pass
import numpy as np

def main():
  '''
  Test code
  '''
  filename = 'PyRat/spheresTest/HET01_DIS_UNI_NIR_20/HET01_DIS_UNI_NIR_20.obj'
  p = PyRatObjParser(filename,reportingFrequency=100,verbose=True)

if __name__ == "__main__":
    main()
