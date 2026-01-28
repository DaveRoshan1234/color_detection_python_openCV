import json
 
def load_follower(followers_1):
    with open(followers_1,'r',encoding="utf-8") as f:
        data=json.load(f)

    follower=set()
    for i in data:
        name = i["string_list_data"][0]["value"]
        follower.add(name)
    return follower


def load_following(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    following = set()
    for i in data["relationships_following"]:
        entry = i["string_list_data"][0]

        if "value" in entry:
            name = entry["value"]
        else:
            name = entry["href"].rstrip("/").split("/")[-1]

        following.add(name)

    return following

followers = load_follower("followers_1.json")
following = load_following("following.json")

not_following_me = following - followers
I_dont_follow = followers - following



print("\n........People I follow but they DON'T follow  back:.........")
for user in sorted(not_following_me):
    print(user)

print("\n........People who follow me but I DON'T follow back:........")
for user in sorted(I_dont_follow):
    print(user)

