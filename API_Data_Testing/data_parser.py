import pandas as pd


def parse_users(users):

    # Validate input
    if not isinstance(users, list):
        raise TypeError("users must be a list")

    rows = []

    for user in users:

        user_data = {
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "company": user.get("company", {}).get("name")
        }

        rows.append(user_data)

    dataframe = pd.DataFrame(rows)

    return dataframe


def save_users_to_csv(dataframe, output_path="users.csv"):

    dataframe.to_csv(output_path, index=False)

    print(f"Data successfully saved to {output_path}")