import functools

def repeat(num):
    
    def decorator_repeat(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            
            for _ in range(num):
                value = func(*args, **kwargs)
            
            return value
        return wrapper
    return decorator_repeat

@repeat(num=5)
def function(name):
    print(f'{name}')
    
function('Python')