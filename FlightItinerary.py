flight_route = [('departure_city', 'arrival_city'), ('departure_city1' , 'arrival_city2') , ('departure_city3' , 'arrival_city3')]
def print_itinerary(route_list):
    for departure , arrival in route_list:
        print('Departure City: ' + departure + '      Arrival City: ' + arrival + '\n')
print_itinerary(flight_route)