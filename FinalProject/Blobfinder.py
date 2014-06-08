import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from StringIO import StringIO

#Creating blob class and implementing parameters
class Blob(): 
    
    def __init__(self): 
        #construct an empty blob
        self.blob_location = []
        self._mass = 0
        
    def add(self, i, j): 
        #add a pixel at location (i,j) to the blob
        self.blob_location.append((i,j));
        
    def mass(self): 
        #return number of pixels added, which equals the blob's mass
        self._mass = len(self.blob_location)
        return self._mass
    
    def distanceTo(self, b): 
        #return distance between centers of masses of this blob and blob b
        #using the round function to make estimates go to 4 decimal places
        distance = round(((b.center_of_mass[0] - self.center_of_mass[0])**2) 
                               + ((b.center_of_mass[1] - self.center_of_mass[1])**2)
                              **0.5, 4)
        return self.distance

    def centerOfMass(self): 
        #return touples of x,y values
        x = 0
        y = 0
        for location in self.blob_location:
            x += location[0]
            y += location[1]
        xave = float(x)/len(self.blob_location)
        yave = float(y)/len(self.blob_location)
        self.centerOfMass = [xave, yave]
        return [xave, yave]
    
    
def monochrome(picture, tau): #taken from counting stars tour
    """loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold 
    tau"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= tau: 
                temp[x,y] = black
            else:
                temp[x,y] = white
                
def count(picture, counter, list_of_blobs): 
    """Scan the image top to bottom and left to right using a nested loop. 
    When black pixel is found, incriment the count, then call the fill 
    function to fill in all the pixels conected to that one. Pixels are then
    put into the blob in the fill function."""
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    xsize, ysize = picture.size
    temp = picture.load()
    list_of_blobs = []
    blob_count = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK: 
                list_of_blobs.append(fill(temp, xsize, ysize, x, y))
    return list_of_blobs
    
def fill(picture, xsize, ysize, xstart, ystart):
    """keep a list of pixels that need to be looked at, but haven't 
    yet been filled in - a list of the (x,y) coordinates of pixels that 
    are neighbors of ones we have already examined.  Keep looping until 
    there's nothing left in this list"""
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    queue = [(xstart,ystart)]
    blobB = Blob()
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            #adds red points to the blob in question
            blobB.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
    return blobB
                
    
def BlobFinder(picture, tau):
    '''find all blobs in the picture using the luminance threshold tau'''
    list_of_blobs = []
    float(tau)
    monochrome(picture, tau)
    list_of_more_blobs = count(picture, fill, list_of_blobs)
    
    return list_of_more_blobs

def countBeads(P, bloblist):
    '''return the number of beads with >= P pixels'''
    countable_blobs = []
    for b in bloblist: 
        x = b.mass()
        if x >= P: 
            countable_blobs.append(b)
    return len(countable_blobs)
    

def getBeads(P, blobs):
    '''return all beads with >= P pixels'''
    countable_blobs = []
    for b in countable_blobs: 
        x = b.mass()
        if x >= P:
            countable_blobs.append(b)
    return countable_blobs