import networkx as nx
import geocoder
import urllib.parse
#### Takes a list of addresses and returns an optimized list
#  

# Getting api_key from file to allow for changing or updating keys 
def get_api_key():
    try:
        with open("api_key", "r") as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        raise "The api_key file with the valid map quest API key should be in the same folder as the exe file."
    return api_key


def get_optimization(addresses):
    ############ Cordinates/ Geocoding section ###################
    ##############################################################

    # Initialize the geocoder
    geolocator = geocoder.mapquest
    
    nodes = [] # This should become a list of node tuples

    nodes_labeled = []

    # Geocode the address
    for address in addresses:
        try:
            location = geolocator(address,key=get_api_key())
        except Exception as e:         
            print(e)

        print(location.latlng)
        try:
            node = (location.latlng)
            nodes.append(node)
            # what if i init a list of lists: ['label',node]
            nodes_labeled.append([address,node])
        except Exception as e:
            print(e)

    ################# Graphing section ##################
    #####################################################
    # Creating a graph which will contain 
    # the nodes and edges representing the network of locations
    G = nx.Graph() # Undirected graph
    
    #G = nx.DiGraph() # Directed graph

    # Adding nodes to my graph
    for node in nodes_labeled:
        G.add_node(node[0], pos=node[1])

    # Adding edges
    for node in nodes_labeled:
        # For each node, connect to all the other nodes, G.add_node("A", pos=(0, 0))  
        for other_node in nodes_labeled:
            if not node[0] == other_node[0]:
                # Connectig the node with each of the other node that is not itself, 
                # ommiting the weight param 'G.add_edge("A", "B", weight=3)'
                G.add_edge(node[0], other_node[0])

    print(G)

    # Solves the traveling salesman problem
    optimized_routes = nx.approximation.traveling_salesman_problem(G)
    #optimized_routes = nx.algorithms.tournament.hamiltonian_path(G)

    ## ########## Create Google maps URL ####
    base_url = "https://www.google.com/maps/dir/"
    itinerary = ""
    for address in optimized_routes:
        # print(address)
        itinerary += address + "/"
    itinerary_encoded = urllib.parse.quote(itinerary)
    full_url = base_url+itinerary_encoded
    # print(full_url)
    rtn_data = {"full_url": full_url,
                "optimized_routes":optimized_routes,
                "lined_output":"\n".join(optimized_routes)}
    return rtn_data


"""
627 Manitou Rd SE, Calgary, AB T2G4C5
905 30 Ave NW, Calgary, AB T2K 0A2
19A Hemlock Crescent SW, Calgary, AB T3C 3A2
4403 10 St SW, Calgary, AB T2S 1J4
2915 26 Ave SE #200, Calgary, AB T2B 2W6
"""