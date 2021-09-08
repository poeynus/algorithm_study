def solution(bridge_length, weight, truck_weights):

    bridge = [0] * bridge_length

    all_weight = 0
    add_weight= 0
    count = 0

    while bridge:
        if truck_weights:
            add_weight = truck_weights[0]
            if all_weight + add_weight <= weight:
                all_weight += add_weight
                if bridge[0] != 0:
                    all_weight -= bridge[0]
                bridge.pop(0)
                bridge.append(truck_weights.pop(0))
            else:
                if bridge[0] != 0:
                    all_weight -= bridge[0]
                    bridge.pop(0)
                    if all_weight + truck_weights[0] <= weight:
                        a = truck_weights.pop(0)
                        bridge.append(a)  
                        all_weight += a
                    else:
                        bridge.append(0)    
                else: 
                    bridge.pop(0)
                    bridge.append(0)
        else:
            bridge.pop(0)
            
        count += 1
    answer = count
    return answer