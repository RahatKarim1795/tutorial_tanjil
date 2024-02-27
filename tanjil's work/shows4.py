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

    return load_json(path)
    


def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    add_str = ""
    for name_cast in cast:
        name1 = name_cast.get('person').get('name')
        char_name = name_cast.get('character').get('name')
        
        refer_as = f'{name1} acted as {char_name}\n'
        
        add_str += refer_as
        
    return add_str
    


def get_show_id(query, shows):
    
    query = query.lower()
    for show_name, show_info in shows.items():

        lowercase_show_name = show_info.get('name').lower()

        if query in lowercase_show_name:
            
            return show_info.get('id')
        
        
        
def find_actor(query: str, cast: list[dict]) -> dict:
    """
    Search for an actor in the cast list
    Return the actor's data if found
    If the actor is not found, return None
    """
    for actor in cast:
        actor_name = actor.get('person').get('name').lower()
        
        actor_role = actor.get('character').get('name').lower()
        if query in actor_name or query in actor_role:
            return actor
    return None   
    
    
def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    actor_name = actor_dict.get('person').get('name')
    actor_role = actor_dict.get('character').get('name')
    actor_gender = actor_dict.get('person').get('birthday')
    actor_bd = actor_dict.get('person').get('birthday')
    actor_country = actor_dict.get('person').get('country').get('name')

    return f'Found: {actor_name} ({actor_gender}, born {actor_bd} in {actor_country}) plays {actor_role}'

    

def main():
    """
    Main function
    """
    shows = load_json("tvshows.json")

    query = input("Search for a TV show: ").lower()

    show_name = find_show(query, shows)

    
    if show_name:
        print(f"Found: {show_name}")
    else:
        print("Can't find this TV show in the Top 100!")

    show = get_show_data_by_name(query,shows)

    print(format_show_details(show))

    show_id = get_show_id(query, shows)

    cast_info = get_cast_by_id(show_id)

    cast_name = format_cast(cast_info)
    print(cast_name)
    
    actor_name = input("Which actor do you want to know about? ").lower()
    actor = find_actor(actor_name, cast_info)
    
    if actor:
        print(format_actor_info(actor))
    else:
        print("Can't find this actor or character in the cast!")

    
    
    


if __name__ == '__main__':
    main()
