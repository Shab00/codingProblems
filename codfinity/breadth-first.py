from collections import deque
graph = {}
graph["you"] = ["alice", "bobm", "clarie"]
graph["alice"] = [] 
graph["bob"] = [] 
graph["clarie"] = []  

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("%s is a mango seller" % person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return print("No mango seller!")

def person_is_seller(name):
    return name[-1] == 'm'

search("you")
