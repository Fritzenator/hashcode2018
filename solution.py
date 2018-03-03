import math

def read():
    with open("input_data/a_example.in") as input:
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


def write(ride_assignments):
    with open('output_data/a_example.out', 'w') as output:
        for r in ride_assignments:
            tmp = '{length} {rides}\n'.format(
                length=len(ride_assignments[r]),
                rides=' '.join(map(str, ride_assignments[r]))
            )
            output.write(tmp)


def calculate_priority(simulation_step, BONUS, vehicle, ride):
    time_in_way_to_client = math.fabs(
                        vehicle['current_y'] - ride['start_y']
                    ) + math.fabs(
                        vehicle['current_x'] - ride['start_x']
                    )
    arrive_time = simulation_step + time_in_way_to_client

    priority = ride['distance']

    if arrive_time <= ride['start_time']:
        arrive_time = ride['start_time']
        priority += BONUS

    priority -= arrive_time

    return priority


def main():
    rides, row_count, column_count, vehicle_count, ride_count, BONUS, steps_count = read()

    vehicles = [{
        'id': v,
        'is_occupied': False,
        'current_x': 0,
        'current_y': 0,
        'freeing_time': 0
    } for v in range(vehicle_count)]

    ride_assignments = {
        vehicle['id']: [] for vehicle in vehicles
    }

    for simulation_step in range(steps_count):
        for vehicle in vehicles:
            if not vehicles[vehicle['id']]['is_occupied']:
                continue
            if simulation_step == vehicles[vehicle['id']]['freeing_time']:
                vehicles[vehicle['id']]['is_occupied'] = False
        if len([ride for ride in rides if not rides[ride]['completed']]) == 0:
            break
        for vehicle in vehicles:
            if vehicles[vehicle['id']]['is_occupied']:
                continue
            priorities = {}
            for ride in rides:
                if rides[ride]['completed']:
                    continue

                priority = calculate_priority(simulation_step, BONUS, vehicle, rides[ride])
                # time_in_way_to_client = math.fabs(
                #         vehicle['current_y'] - rides[ride]['start_y']
                #     ) + math.fabs(
                #         vehicle['current_x'] - rides[ride]['start_x']
                #     )
                # arrive_time = simulation_step + time_in_way_to_client

                # priority = rides[ride]['distance']

                # if arrive_time <= rides[ride]['start_time']:
                #     arrive_time = rides[ride]['start_time']
                #     priority += BONUS

                # priority -= arrive_time

                priorities[priority] = ride


            selected_ride = max(priorities)
            ride_assignments[vehicle['id']].append(priorities[selected_ride])
            vehicles[vehicle['id']]['is_occupied'] = True
            #TODO: freeing time should be calculated as vehicle arrive time + ride distance
            vehicles[vehicle['id']]['freeing_time'] = rides[priorities[selected_ride]]['start_time'] + rides[priorities[selected_ride]]['distance']
            vehicles[vehicle['id']]['current_x'] = rides[priorities[selected_ride]]['end_x']
            vehicles[vehicle['id']]['current_y'] = rides[priorities[selected_ride]]['end_y']
            rides[ride]['completed'] = True

    write(ride_assignments)


if __name__ == '__main__':
    main()