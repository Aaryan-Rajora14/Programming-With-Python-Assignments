# 1.Given a list, write a Python program to swap first and last element of the list.

Sports = ["Badminton","Hockey","Cricket","Racing","Football","Basketball"]

print(f'Original Sports List:{Sports}')

Saved_sport = Sports[0]
Sports[0] = Sports[-1]
Sports[-1] = Saved_sport

print(f"Modified Sports LIst: {Sports}")
