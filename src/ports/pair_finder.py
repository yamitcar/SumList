import bisect


class PairFinder:

    def execute(self, values, operation_result):
        results = []
        ordered_values = sorted(values)  # uses timSort, and modify the array itself. O(n log n)
        self._find_with_ordered_values(ordered_values, operation_result, results)
        return results
    
    def _find_with_ordered_values(self, ordered_values, operation_result, results):
        pair = self._search_pair(ordered_values, operation_result)
        if pair is not None:
            results.append(pair)
        
        if len(ordered_values) >= 2:
            self._find_with_ordered_values(ordered_values, operation_result, results)  # lineal recursion O(n)
    
    def _search_pair(self, ordered_values, operation_result):
        first_pair_element = ordered_values.pop(0)  # o(n)
        second_pair_to_find = operation_result - first_pair_element
        
        second_pair_index = bisect.bisect_left(ordered_values, second_pair_to_find)  # binary search O(log n)
        if self._second_element_is_in(ordered_values, second_pair_index, second_pair_to_find):
            ordered_values.pop(second_pair_index)  # o(n)
            return [first_pair_element, second_pair_to_find]
        else:
            return None
    
    def _second_element_is_in(self, ordered_values, second_pair_index, second_pair_to_find):
        return second_pair_index < len(ordered_values) and ordered_values[second_pair_index] == second_pair_to_find
    