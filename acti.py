import json
import requests


def activity():
    choice = 0

    while choice == 0:
        bored = requests.get("http://www.boredapi.com/api/activity/")
        data = bored.json()
        print("These are activities that you can do:")
        

        print("Activity name:",data["activity"])

        access = float(data["accessibility"])


        if access == 1 and accessArkadaşlar ufak bı düşünce herkese açık bı grup olduğu için hocada burda olmasın ? >= 0.7:
            print("The activity very hard to do")

        elif access >= 0.5 and access < 0.7:
            print("The activity hard but i think you can do this")

        elif access > 0.3 and access < 0.5:
            print("The activity is easy")

        else:
            print("Oh my gush activity very easy")

        print("By the the activity type is:",data["type"])
        print("You can do with ",int(data["participants"]),"person/people")

        choice=int(input(("Do you want to find different activities (0/1)?")))
