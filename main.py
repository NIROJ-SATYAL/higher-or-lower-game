import random
import os

game_data=[



        {
            "name:":"katrina kaif",
            "followers:":46,
            "country:":"india"

        }
        ,{
            "name:":"jacqueline fernandez",
            "followers:":48.1,
            "country:":"india"


        },
        {
            "name:":"Akshya kumar",
            "followers:":48.3,
            "country:":"india"

        },
        {

            "name:":"alia bhatt",
            "followers:":50.9,
            "country:":"india"

        },
        {
            
            "name:":"narendra modi",
            "followers:":51.1,
            "country:":"india"

        
        },
        {
            
            "name:":"neha kakkar",
            "followers:":52.6,
            "country:":"india"



        
        },
        {

            "name:":"deepika padhukon",
            "followers:":53.2,
            "country:":"india"

        
        },
        {

            "name:":"shraddha kapoor",
            "followers:":57.9,
            "country:":"india"

        
        },
        {

            "name:":"priyanka chopra",
            "followers:":60.7,
            "country:":"india"

        
        },
        {

            "name:":"virat kohli",
            "followers:":98.1,
            "country:":"india"

        
        }
   
]

def check(guess,score,score1):
    if score>score1:
        return guess=="a"
    else:
        return guess=="b"

account_b=random.choice(game_data)
total_score=0
end_game=True
while end_game:
    def game(account):
        name=account["name:"]
        country=account["country:"]
        return f"{name} from {country}"

    account_a=account_b

    account_b=random.choice(game_data)
    if account_a==account_b:
        account_b=random.choice(game_data)

    print(f"compare A: {game(account_a)}")

    print(f"against B: {game(account_b)}")


    guess=input("who has more followers? type 'A' or 'B'").lower()


    score=account_a["followers:"]
    score1=account_b["followers:"]

    check_answer=check(guess,score,score1)


    if check_answer:
        total_score+=1
        os.system("clear")
        print(f"you are right.current score is {total_score}")
        

       
    else:
        end_game=False
        print(f"wrong ! final score is:{total_score}")
