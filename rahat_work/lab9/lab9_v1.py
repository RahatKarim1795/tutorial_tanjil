import json

def load_json(filename) -> dict:

    # f = open(filename,"r")

    with open(filename, 'r') as file:
        json_data = json.load(file)

    return json_data


def find_show(query: str, shows: dict) -> str:


    query = query.lower()

    for show_name, show_info in shows.items():

        # Extract the 'name' value from the show_info and convert to lowercase
        lowercase_show_name = show_info.get('name').lower()

        # Check if the query string is present in the lowercase show name
        if query in lowercase_show_name:
            # Return the show name
            return show_name

    # If no match is found, return None or an appropriate message
    return None


def main():
    """
    Main function
    """
    shows = load_json("tvshows.json")

    query = input("Search for a TV show: ")

    show_name = find_show(query, shows)

    if show_name:
        print(f"Found: {show_name}")
    else:
        print("Can't find this TV show in the Top 100!")


if __name__ == '__main__':
    main()
