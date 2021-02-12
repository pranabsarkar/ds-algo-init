from execution_duration import ExcecutionDuration

client = ExcecutionDuration()


class Kadane:
    def __init__(self) -> None:
        pass

    @client.execution_details
    def max_sub_array_sum_brute_force(self, a: list, size: int) -> list:
        """
        This is a brute-force solution to find the Max Sub Array Sum
        """
        temp = {}
        for i in range(0, size):
            maximum = 0
            summation = 0
            start = 0
            end = 0
            for item in range(0, size):
                summation = sum(a[item:item+i+1])
                if summation>maximum:
                    maximum = summation
                    start = item
                    end = item+i
            temp[maximum] = {"start": start, "end": end}
        return [max(temp.keys()), temp[max(temp.keys())]]

    @client.execution_details
    def max_sub_array_sum(self, a: list,size: int) -> int:
        """
        This is a Kadane's Algorithm solution to find the Max Sub Array Sum
        """
        max_so_far =a[0]
        curr_max = a[0]
        
        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
            
        return max_so_far

arr = [-2,2,5,-11,6, 99, 112, 8729, 291, 921793, 9739123, 12, 3, -1]

print(
    "Brute-Force Solution ->", Kadane().max_sub_array_sum_brute_force(
        arr, 
        len(arr))
    )

print(
    "Kadane's Algorithm Solution ->", Kadane().max_sub_array_sum(
        arr, 
        len(arr))
    )

"""
Execution Results:

Brute-Force Solution -> ([10670168, {'start': 4, 'end': 12}], 0.001979351043701172)
Kadane's Algorithm Solution -> (10670168, 0.0009949207305908203)

"""