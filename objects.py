class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

s1 = Student("Ada", 26, "Backend", 40.56)
print(s1.name)
print(s1.age)
print(s1.tracks)
print(s1.score)



# [assignment] Skeleton class. Add your code here
class Student:
    def __init__(Bob,name, age, tracks, score):
        Bob.name = name
        Bob.age = age
        Bob.tracks= tracks
        Bob.score = score

Bob = Student("Bob",26,["FE","BE"],20.90)

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)

# Expected methods
class Student:
    def __init__(Bob,change_name, change_age, add_tracks, get_score):
        Bob.change_name= change_name
        Bob.change_age = change_age
        Bob.add_track = add_tracks
        Bob.get_score = get_score

Bob = Student("Peter", 34, ["UI/UX"], 20.90)

print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score)


