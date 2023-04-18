import random

boxes = []
for i in range(5):
    boxes.append(i)

surprise_box = random.choice(boxes)

wins_guess = 0
wins_switch = 0

switch = False
wins_guess = 0
wins_switch = 0

for round in range(100):
    guess = random.choice(boxes)
    
    boxes_left = boxes.copy()
    boxes_left.remove(guess)
    opened_boxes = []
    while len(boxes_left) > 2:
        box_to_open = random.choice(boxes_left)
        boxes_left.remove(box_to_open)
        opened_boxes.append(box_to_open)
        print ('Boxes Left', boxes_left)
    
    if surprise_box in opened_boxes:
        switch = random.choice([True, False])
        if switch:
            guess = boxes_left[0] if boxes_left[0] != surprise_box else boxes_left[1]
    
    if guess == surprise_box:
      wins_guess += 1
    elif switch == True:
      wins_switch += 1

print('Number of Wins by Guessing:', wins_guess) 
print('Number of Wins by Switching:', wins_switch)
