# Flow of Context Manager
# with block starts
# → __enter__()
# → code runs
# → __exit__()
# → cleanup

# class MyContext:

#     def __enter__(self):
#         print("Entering block")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting block")

# with MyContext():
#     print("Inside block")
# /////// //////
# with Exception
# class Test:

#     def __enter__(self):
#         print("start")

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("error type:", exc_type)
#         print("end")

# with Test():
#     print(10 / 0)
# start
# error type: <class 'ZeroDivisionError'>
# end
# Even with error:

# __exit__ still runs

# Very important for cleanup.