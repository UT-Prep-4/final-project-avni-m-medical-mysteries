#Name(s):
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: For my project, I will be building a simulation of a hospital and a patient, where the player, or the doctor, is required to make decisions to cure their patient.
  THE PIECES I NEED TO BUILD: I will need to use print statements, if, else, elif loops, and input statements.
  WHAT I WILL DEMO AT SHOWCASE: Give the audience a chance to play the game themselves.

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''




print("A patient walks into your hospital, with complaints of hyperentilation and chest pain. You have three choices.")
print("Option 1: check their vitals through a heart moniter, blood pressure, and heart rythm.")
print("Option 2: calm the patient down, because they are showing signs of a panic attack")
print("Option 3: Recieve medical history before operating on the patient")
choice1 =input("Option 1, Option 2, or Option 3?")


print() 

if choice1=="1":
  print("Vitals show blood pressure of 110/70, heart rate 125, oxygen levels of 84%.")
  choice1a =input("Either choose to (a1) prepare an ultrasound and emergency medications, or (b1) send the patient back to the waiting room since their condition isn't bad")
  if choice1a=="a1":
    print("You find a strain in the heart, comfirming pulmonary embolism, but blood pressure remains normal.")
    choice2a=input("Next, choose to (c1) use blood thinner to stabilize, or (d1) wait a few minutes for vital sign changes.")
    if choice2a=="1d":
      print("Patient suddenly crashes and loses consciousness. Blood pressure levels drop to 70/40. To help, you grab Clot-Busters. The Clot-Busters attacks the clot, and slices through fibrin web, breaking the clottage down.")
      choice6a=input("After using the clot-busters, you can chose to (1aa) perform neuro checks since the brain could be prone to bleeding, or (1ab) discharge the patient since they seem alright and your job is done.")
      if choice6a=="1aa": 
        print("After a few days, you discharge the patient. You succesfully saved them!")
      if choice6a=="1ab": 
        print("The patient suffered from brain bleeding. You failed to save them.")

  elif choice1a=="b1": 
    print("You failed to save the patient! They had an underlying condition called pulmonary embolism, and without intensive treatment, they suffered fron cardiac arrest")


   
if choice1=="2":
  print("Patient slows breathing, but oxygen levels plummet")
  choice1b =input("Choose to (a2) flood the system with oxygen, (b2) turn off the monitor since stats are incorrect, or (c1) Give anxiety medication")
  if choice1b=="a2":
    print("Patient stabilizes! However, you see that one leg is swollen.")
  choice6a=input("Either (1i) treat the leg with ice or (1j) push a heavy dose of IV blood thinners.")
  if choice6a=="1i":
    print("Patient suffers from cardiovascular collapse. You failed. Rule of thumb: treat in order of airway, breathing, circultation.")
  elif choice6a=="1j":
    print("Vitals don't snap back to normal but they do stabilize. Patient still feels sharp pain in chest.")
    choice4a=input("Either choose to (1k) keep monitoring patient by getting a heart ultrasound, bed rest, and checking for brain bleed or (1l) discharge the pateint since they are stable.")
    if choice4a=="1k":
      print("You save the patient! By monitoring them and discharging after a week, you made sure they were fully okay. Make sure to tell them to follow up with a hermatologist!")
    if choice4a=="1l":
      print("The patient collapses at home due to buildup from a blood clot. They enter obstructive shock.")
      choice5a=input("Either choose to (1z) enter code blue, or (1x) scan for a chest x-ray to see exactly what's wrong.")
      if choice5a=="1z":
       print("You succesfully saved the patient.")
      if choice5a=="1x":
         print("You wasted too much time. You failed to save the patient!")


  if choice1b=="b2":
    print("You failed to save the patient! They had an underlying condition called pulmonary embolism, and without intensive treatment, they suffered fron cardiac arrest")
  elif choice1b=="c1":
    print("The patient collapses due to respiratory faliure and cardiovascular collapse.")
    choice2b =input("Choose to either (1g) provide the drug's anitdote to stop its effects, or (1h) provide IV for the patient.")
    if choice2b=="1g":
      print("The patient wakes up and begins to hyperventilate again, showing low blood pressure levels.")
      choice2c=input("Chose to (1cc) assume it is okay since they calm down quickly, or (1dd) provide blood thinners because you suspect pulmonary embolism.")
      if choice2c=="1cc":
        print("Too late, the patient suffered from obstructive shock. You failed to save the patient.")
      if choice2c=="1dd":
        print("You saved the patient!")
    if choice2b=="1h":
      print("During a regular shock, yes, IV would help. For this patient, the heart's ventricle is already stretched by trying to push blood past a clot from pulmonary embolism. Using IV crushes the left ventricle and causes cardiac arrest.")

'''
option 3 with swollen leg path and blood thinners is completely built below.
'''

if choice1=="3":
  choice1c =input("Next, choose to (a3) ask specific quetsions to find an underlying condition, or (b3) run a physical on the patient.")
  if choice1c=="a3":
    print("You find out that the patient has a previous history of anxiety.")
    choice3a=input("Either choose to (1gh) give anxiety meds to calm down the patient, or (1hg) check their vitals.")
    '''
    vitals path not working
    '''
    if choice3a=="1gh":
      print("The patient collapses due to respiratory faliure and cardiovascular collapse.")
      choice2b =input("Choose to either (1g) provide the drug's anitdote to stop its effects, or (1h) provide IV for the patient.")
      if choice2b=="1g":
       print("The patient wakes up and begins to hyperventilate again, showing low blood pressure levels.")
       choice2c=input("Chose to (1cc) assume it is okay since they calm down quickly, or (1dd) provide blood thinners because you suspect pulmonary embolism.")
       if choice2c=="1cc":
        print("Too late, the patient suffered from obstructive shock. You failed to save the patient.")
       if choice2c=="1dd":
        print("You saved the patient!")
      if choice2b=="1h":
        print("During a regular shock, yes, IV would help. For this patient, the heart's ventricle is already stretched by trying to push blood past a clot from pulmonary embolism. Using IV crushes the left ventricle and causes cardiac arrest.")
  elif choice1c=="b3":
    print("You notice one of the patient's legs are swollen.")
    choice3b=input("Either (1i) treat the leg with ice or (1j) push a heavy dose of IV blood thinners.")
    if choice3b=="1i":
      print("Patient suffers from cardiovascular collapse. You failed. Rule of thumb: treat in order of airway, breathing, circultation.")
    elif choice3b=="1j":
      print("Vitals don't snap back to normal but they do stabilize. Patient still feels sharp pain in chest.")
    choice4a=input("Either choose to (1k) keep monitoring patient by getting a heart ultrasound, bed rest, and checking for brain bleed or (1l) discharge the pateint since they are stable.")
    if choice4a=="1k":
      print("You save the patient! By monitoring them and discharging after a week, you made sure they were fully okay. Make sure to tell them to follow up with a hermatologist!")
    if choice4a=="1l":
      print("The patient collapses at home due to buildup from a blood clot. They enter obstructive shock.")
      choice5a=input("Either choose to (1z) enter code blue, or (1x) scan for a chest x-ray to see exactly what's wrong.")
      if choice5a=="1z":
       print("You succesfully saved the patient.")
      if choice5a=="1x":
         print("You wasted too much time. You failed to save the patient!")
    if choice3a=="1hg":
      print("Vitals show blood pressure of 110/70, heart rate 125, oxygen levels of 84%.")
      choice1a =input("Either choose to (a1) prepare an ultrasound and emergency medications, or (b1) send the patient back to the waiting room since their condition isn't bad")
      if choice1a=="a1":
        print("You find a strain in the heart, comfirming pulmonary embolism, but blood pressure remains normal.")
        choice2a=input("Next, choose to (c1) use blood thinner to stabilize, or (d1) wait a few minutes for vital sign changes.")
        if choice2a=="1d":
          print("Patient suddenly crashes and loses consciousness. Blood pressure levels drop to 70/40. To help, you grab Clot-Busters. The Clot-Busters attacks the clot, and slices through fibrin web, breaking the clottage down.")
          choice6a=input("After using the clot-busters, you can chose to (1aa) perform neuro checks since the brain could be prone to bleeding, or (1ab) discharge the patient since they seem alright and your job is done.")
          if choice6a=="1aa": 
           print("After a few days, you discharge the patient. You succesfully saved them!")
          if choice6a=="1ab": 
            print("The patient suffered from brain bleeding. You failed to save them.")
  elif choice1a=="b1": 
    print("You failed to save the patient! They had an underlying condition called pulmonary embolism, and without intensive treatment, they suffered fron cardiac arrest")

    