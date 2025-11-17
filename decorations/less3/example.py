from collections import deque
import random

class Memorized:
    def __init__(self, cache_size=100):
        self.cache_size = cache_size
        self.call_args_queue = deque()
        self.call_args_to_result = {}

    def __call__(self, fn):
        def new_func(*args, **kwargs):
            memorization_key = self._convert_call_arguments_to_hash(args, kwargs)
            if memorization_key not in self.call_args_to_result:
                result = fn(*args, **kwargs)
                self._update_cache_key_with_value(memorization_key, result)
                self._evict_cache_if_necessary()
            return self.call_args_to_result[memorization_key]
        return new_func
    
    def _update_cache_key_with_value(self, key, value):
        self.call_args_to_result[key] = value
        self.call_args_queue.append(key)

    def _evict_cache_if_necessary(self):
        if len(self.call_args_queue) > self.cache_size:
            oldest_key = self.call_args_queue.popleft()
            del self.call_args_to_result[oldest_key]

    @staticmethod
    def _convert_call_arguments_to_hash(args, kwargs):
        return hash(str(args) + str(kwargs))
    
@Memorized(cache_size=5)
def get_not_so_random_number_with_max(max_value):
    return random.random() *max_value

memoiz = get_not_so_random_number_with_max(10)
print(memoiz)
