def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = [0 for i in range(bridge_length)]
    i = 0
    total = 0
    while i < len(truck_weights):

        if total + truck_weights[i] > weight:
            total -= bridge[0]
            bridge = bridge[1:]
            if total + truck_weights[i] <= weight:
                bridge.append(truck_weights[i])
                total += bridge[-1]
            else:
                bridge.append(0)
                i -= 1
        else :
            total -= bridge[0]
            bridge = bridge[1:]
            bridge.append(truck_weights[i])
            total += bridge[-1]
        i += 1
        count += 1
    return count + bridge_length