'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    N = 0
    N2 = 0

    if to_member in social_graph[from_member]["following"]:
        N=N+1
    
    if from_member in social_graph[to_member]["following"]:
        N2=N2+1 

    if N == 1 and N2 == 1:
        print("friends")

    if N == 0 and N2 == 0:
        print("no relationship")

    if N == 1 and N2 == 0:
        print("following")

    if N == 0 and N2 == 1:
        print("followed by")


def tic_tac_toe(board):

    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    N = 0
    Symbol = " "
    #First line
    if board[0][0] == board[0][1] == board[0][2]:
        N = N + 1
        Symbol = board[0][0]

    #Second line
    if board[1][0] == board[1][1] == board[1][2]:
        N = N + 1
        Symbol = board[1][0]

    #Third line
    if board[2][0] == board[2][1] == board[2][2]:
        N = N + 1
        Symbol = board[2][0]

    #First Column
    if board[0][0] == board[1][0] == board[2][0]:
        N = N + 1
        Symbol = board[0][0]

    #Second Column
    if board[0][1] == board[1][1] == board[2][1]:
        N = N + 1
        Symbol = board[1][0]

    #Third Column
    if board[0][2] == board[1][2] == board[2][2]:
        N = N + 1
        Symbol = board[0][0]

    #Left-Right Diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        N = N + 1
        Symbol = board[0][0]

    #Right-Left Diagional
    if board[0][2] == board[1][1] == board[2][0]:
        N = N + 1
        Symbol = board[0][2]

    if N > 0:
        print("Winner: " + str(Symbol))

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several route_map between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more route_map and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from itertools import cycle

    timeL = []
    total = 0
    travel_time = 0

    routeDict = []
    routeList = []

    for a in route_map:
        routeDict.append(a)

    for a in routeDict:
        b = ' '.join(a)
        routeList.append(b)

    routeString = ' '.join(routeList)
    routeStringL = routeString.split()
    routeFinal = []

    for a in routeStringL:
        if a not in routeFinal:
            routeFinal.append(a)

    for a in route_map:
        total = total + route_map[a]["travel_time_mins"]

    for a in route_map:
        timeL.append(route_map[a]["travel_time_mins"])

    CrouteF = cycle(routeFinal)

    ix = routeFinal.index(first_stop)
    iy = routeFinal.index(second_stop)

    if iy - ix != 1:
        location = routeFinal[ix]

        while (ix + 1) > 0:
            l = next(CrouteF)
            ix = ix - 1
            print(l)
    
        while location != routeFinal[iy]:
            il = routeFinal.index(location)
            travel_time = travel_time + timeL[il]
            location = next(CrouteF)
    else:
        travel_time = route_map[first_stop,second_stop]["travel_time_mins"]

    if first_stop == second_stop:
        travel_time = total

    print(travel_time)
