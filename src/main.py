from cfg import ACTOR2ID, ACTOR_LOOKUP

def main():
    print(ACTOR2ID["Tom Cruise"])
    print(ACTOR_LOOKUP[ACTOR2ID["Tom Cruise"]])

if __name__ == "__main__":
    main()
