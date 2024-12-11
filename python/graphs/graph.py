from collections import deque
from typing import List

graph = {}
graph["you"] = ["Eli", "Roger", "Ana"]
graph["ana"] = ["Jose"]


def personIsSeller(person: List[str]) -> bool:
    return person[0][-2] == "l"


def shortPath(name):
    search_queue: deque = deque()
    search_queue.append(graph[name])
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            return False

        if personIsSeller(person):
            print("Person is seller mongo")
            return True
        else:
            searched.append(person)
            search_queue.append(graph["ana"])

    return False


shortPath("you")
