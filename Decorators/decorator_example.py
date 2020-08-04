def main_execution(function):
    def inner_execution():
        print('Executing...')
        function()
        print('Executed...')
    return inner_execution


# method - 1
# def sample_execution():
#     print('Sample executed')
# sample_execution = main_execution(sample_execution)

# method - 2
@main_execution
def sample_execution():
    print('Sample executed')


sample_execution()