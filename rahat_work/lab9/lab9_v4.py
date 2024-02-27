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


def get_cast_by_id(show_id: int) -> list[dict]:

    path = "cast/" + str(show_id) + "_cast.json"

    cast_dictionary = load_json(path)

    return cast_dictionary
    


def format_cast(cast: list[dict]) -> str:

    cast_info = ""

    for entry in cast:
        # person_name = entry['person']['name']
        # character_name = entry['character']['name']

        person_name = entry.get('person').get('name', 'Unknown')
        character_name = entry.get('character').get('name', 'Unknown')

        # cast_info = cast_info + f"{person_name} as {character_name}\n"

        cast_info += f"{person_name} as {character_name}\n"

        # strinss = "hello" + person_name + "world"

    return cast_info



def get_show_id(query, shows):
    
    query = query.lower()
    for show_name, show_info in shows.items():

        lowercase_show_name = show_info.get('name').lower()

        if query in lowercase_show_name:
            
            return show_info.get('id')
        


def find_actor(query: str, cast: list[dict]) -> dict:

    for entry in cast:
        check_name = entry.get('person').get('name')

        if query.lower() == check_name.lower():
            actor_info = entry

            return actor_info

    return None



def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    # TODO: Implement the function
    # actor_info={
            #     "name": entry.get('person').get('name'),
            #     "gender": entry.get('person').get('gender'),
            #     "birthday": entry.get('person').get('birthday'),
            #     "country": entry.get('person').get('country').get('name')
            # }

    name = actor_dict.get('person').get('name')
    gender =  actor_dict.get('person').get('gender')
    birthday = actor_dict.get('person').get('birthday')
    country = actor_dict.get('person').get('country').get('name')
    role = actor_dict.get('character').get('name')


    info = f'{name} ({gender}, born {birthday} in {country}) plays {role}'
    
    return info



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

    show = get_show_data_by_name(query,shows)

    print(format_show_details(show))

    show_id = get_show_id(query, shows)

    cast_info = get_cast_by_id(show_id)

    print()

    print("Cast List:\n\n" + format_cast(cast_info))

    actor = input("To know actor details name: ")

    char_info = find_actor(actor, cast_info)

    # print(char_info)

    print(format_actor_info(char_info))



    


if __name__ == '__main__':
    main()
