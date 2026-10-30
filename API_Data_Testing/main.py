from api_client import fetch_users

from data_parser import parse_users, save_users_to_csv


def main():

    print("Fetching users from API...")

    users = fetch_users()

    print("Processing user data...")

    dataframe = parse_users(users)

    print("Saving data to CSV...")

    save_users_to_csv(dataframe)

    print("Total users processed:", len(dataframe))


if __name__ == "__main__":
    main()