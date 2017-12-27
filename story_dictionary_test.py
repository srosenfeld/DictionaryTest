story = {0:["Your journey begins.",['a','b','c'],['win','tie','lose'],[1,2,3]]
         }

'''
for q,a in story.items():
    for i in a:
        print(i)

'''

choice = ""
step = 0

def step_story(s):
    print(story[s][0])
    print("What is your choice?")
    while True:
        for i in story[s][1]:
            print(i)
        c = input()

        if c not in story[s][1]:
            print("Please try again")
        else:
            ind=story[s][1].index(c)
            print(story[s][2][ind])
            global choice = story[s][3][ind]
            break

step_story(0)
