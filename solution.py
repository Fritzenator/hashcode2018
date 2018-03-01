import math

def read():
    with open("a_example.in") as input:
        row_count, column_count, vehicle_count, ride_count, bonus, steps_count = tuple(
            map(
                int, input.readline().split(' ')
            )
        )
        rides = {}
        count = 0
        for ride in input:
            ride_l = tuple(
                map(
                    int, ride.split(' ')
                )
            )
            ride_dict = {
                'start_x': ride_l[0],
                'start_y': ride_l[1],
                'end_x': ride_l[2],
                'end_y': ride_l[3],
                'start_time': ride_l[4],
                'end_time': ride_l[5],
                'completed': False,
                'count': count
            }
            count += 1

            ride_dict['distance'] = math.fabs(
                ride_dict['end_y'] - ride_dict['start_y']
            ) + math.fabs(
                ride_dict['end_x'] - ride_dict['start_x']
            )

            if ride_dict['distance'] > (ride_dict['end_time'] - ride_dict['start_time']):
                continue
            rides[ride_dict['count']] = ride_dict
        return rides, row_count, column_count, vehicle_count, ride_count, bonus, steps_count


def main():
    rides, row_count, column_count, vehicle_count, ride_count, BONUS, steps_count = read()

    vehicles = [{
        'id': v,
        'is_occupied': False,
        'current_x': 0,
        'current_y': 0,
        'freeing_time':0
    } for v in range(vehicle_count)]

    ride_assignments = {
        vehicle['id']: [] for vehicle in vehicles
    }    
    
    # print(rides, row_count, column_count, vehicle_count, ride_count, bonus, steps_count)
    # print(ride_assignments)
    # print(initial_rides)
    for simulation_step in range(steps_count):
        priorities = {}
        for vehicle in vehicles if not vehicles[vehicle]['is_occupied']:
            priorities[vehicle] = {}
            for ride in rides if not rides[ride]['completed']:

                priorities[vehicle][ride] = []
                time_in_way_to_client = math.fabs(
                        vehicle['current_y'] - rides[ride]['start_y']
                    ) + math.fabs(
                        vehicle['current_x'] - rides[ride]['start_x']
                    )
                arrive_time = simulation_step + time_in_way_to_client

                priority = rides[ride]['distance']

                if arrive_time <= rides[ride]['start_time']:
                    arrive_time = rides[ride]['start_time']
                    priority += BONUS

                priority -= arrive_time

                priorities[vehicle][ride].push(priority)

            
            try:
                selected_ride = priorities[k[0]]
                ride_assignments[ride].append(selected_ride)
                vehicles[vehicle]['is_occupied'] = True
                vehicles[vehicle]['freeing_time'] =
                vehicles[vehicle]['current_x'] = selected_ride['end_x']
                vehicles[vehicle]['current_y'] = selected_ride['end_y']
                rides[ride]['completed'] = True
            except IndexError:

            
                

                
            

    

if __name__ == '__main__':
    main()