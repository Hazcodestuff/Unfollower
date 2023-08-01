import instaloader

def get_unfollowers(username):
    L = instaloader.Instaloader()

    try:
        # Load the Instagram profile by username
        profile = instaloader.Profile.from_username(L.context, username)
        followers = set(profile.get_followers())
        following = set(profile.get_followees())

        # Calculate the difference to find unfollowers
        unfollowers = following - followers

        return unfollowers
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")
        return set()
    except instaloader.exceptions.QueryReturnedNotFoundException:
        print("Account with private followers.")
        return set()

if __name__ == "__main__":
    username = input("Enter your Instagram account name: ")
    unfollowers = get_unfollowers(username)

    print("Unfollowers:")
    for user in unfollowers:
        print(user.username)
