from random import randint
import math
def isPalindrome(s):
    return s == s[::-1]

def generateSet(n):
    array = []
    if n%2 == 0:
        for i in range (int(n/2)):
            x = randint(1,9)
            array.append(x)
            array.append(x)
    if n%2 == 1:
        for i in range (int((n-1)/2)):
            
            x = randint(1,9)
            array.append(x)
            array.append(x)
        x = randint(1,9)
        array.append(x)
    return array

def makePalindrome(array,n):
    tempArray = []
    for i in array:
        tempArray.append(i)
    newArray = []
    for i in range(n):
        index = randint(0,n-1)
        newArray.append(tempArray[index]) 
        tempArray.pop(index)
        n -= 1
    return newArray

def testPalindrome(array,n,yes):
    newArray= makePalindrome(array,n)
    if isPalindrome(newArray):
        yes += 1
    return yes

def experimentalProbability(array,yes):
    yes = testPalindrome(array,n,yes)
    return yes

def theoreticalProbability(array,n):
    dX,hdX = 1,1
    dupes = [0 for i in range(9)]
    halfDupes = [0 for i in range(9)]
    for i in array:
        dupes[i-1] += 1
    for i in array:
        halfDupes[i-1] = int(dupes[i-1]/2)
    halfDupes = [math.factorial(i) for i in halfDupes]
    for i in halfDupes:
        hdX *= i
    palindromes = math.factorial(int(n/2))/hdX
    dupes = [math.factorial(i) for i in dupes]
    for i in dupes:
        dX *= i
    permutations = math.factorial(int(n))/dX
    probability = palindromes/permutations
    return probability

def yes():
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    for i in range(65610):
        array = generateSet(n)
        dupes = [0 for i in range(9)]
        for i in array:
            dupes[i-1] += 1    
        if 3 in dupes:
            three += 1
        if 4 in dupes:
            four += 1
        if 5 in dupes:
            five += 1
        if 2 in dupes:
            two += 1
        if 6 in dupes:
            six += 1
        if 7 in dupes:
            seven += 1
        if 8 in dupes:
            eight += 1
    print(two,three,four,five,six,seven,eight)

n = 5
yes = 0
testAmt = 100000
for i in range(testAmt):
    Set = generateSet(n)
    yes = experimentalProbability(Set,yes)
#tp = theoreticalProbability(Set,n)
print(f"Exp. = {yes/testAmt} Theo. = {0}")

<div class="container-fluid" style ="width:100vw;display:block;white-space:nowrap;background-image:url(tile1.png);background-repeat:no-repeat;padding:0px;position:relative;z-index: 1">
  <div id="project-track" class="container-fluid" style="top:110px;position:relative;z-index: 2">
      <h1 id="heading-font">Choose Your Project Track</h1>
          <div class="project-track-button" style="position:relative;white-space: nowrap;display:inline-block;left:225px;margin-right:275px;">
              <p class="project-track-text" style="">HEALTH</p>
              <img src="beating-heart.svg" style="margin-left:5%;">
          </div>
          <div class="project-track-button" style="position:relative;white-space: nowrap;display:inline-block;margin-right:50px;top:7px;">
              <p class="project-track-text" style="left:50%">SOCIAL GOOD</p>
              <img src="scales.svg" style="margin-left:5%;">
          </div> 
          <div class="project-track-button" style="position:relative;white-space: nowrap;display:inline-block;top:36px;">
              <p class="project-track-text">RURAL<br>DEVELOPMENT</p>
              <img src="rural-graph.svg" style="margin-left:5%;">
          </div>     
      <div class="flex-container" style="margin-left:40px;margin-top:75px;width: 1782px;height: 137px;background: rgba(217, 217, 217, 0.6);border-radius: 20px;">
          <p id="project-FAQ" style="margin-top: 20px;">
          <img src="info-mark.svg" style="margin-left:30px;margin-right:10px">
          Each of the following 3 tracks will have no-code alternatives, the pitch competition tracks, where participants submit a 5-minute pitch video.<br>
          <span style="margin-left:70px;">Check out</span>
          <a href="#FAQ" style="color:black;">FAQ Section</a>
          for more info!
          </p>
      </div>
  </div>
</div>