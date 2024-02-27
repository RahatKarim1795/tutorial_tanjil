import json

def load_json(filename) -> dict:

    # f = open(filename,"r")

    with open(filename, 'r') as file:
        json_data = json.load(file)

    return json_data


def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    # TODO: Implement the function

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


def get_show_data_by_name(show_name: str, shows: dict):
    """
    Return the data for a show based on its name
    """
    # TODO: Implemented the function
    show_name = show_name.lower()

    data = {}

    for show_n, show_info in shows.items():
        
        lowercase_show_name = show_info.get('name').lower()

        if show_name in lowercase_show_name:
            data = show_info

    # print(data)
    return data




def format_show_details(show: dict) -> str:

    stringa = "a"
 
    name = show.get('name')

    start = show.get('premiered','?')
    startf = start.split("-")[0]

    if show.get('ended') is not None:
        end = show.get('ended', '?')
    else:
        end = '?'


    genres = show.get('genres')
    genresf = ', '.join(genres)


    stringa = f"{name} ( {startf} - {end}, {genresf} )"

    return stringa




def show_info(query, shows):
    query = query.lower()

    show_data = []

    for show_name, show_info in shows.items():

        lowercase_show_name = show_info.get('name').lower()

        if query in lowercase_show_name:
            print(show_name)
            print(show_info.get('premiered'))
            print(show_info.get('ended'))
            print(show_info.get('genres'))

    return show_data

def main():
    """
    Main function
    """
    shows = load_json("tvshows.json")

    query = input("Search for a TV show: ")

    show_name = find_show(query, shows)

    # print(show_info(query,shows))

    show = get_show_data_by_name(query,shows)

    print(format_show_details(show))

    if show_name:
        print(f"Found: {show_name}")
    else:
        print("Can't find this TV show in the Top 100!")


if __name__ == '__main__':
    main()
