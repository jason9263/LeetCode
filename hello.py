# class Solution:
from collections import defaultdict
from typing import List

def findItinerary(tickets: List[List[str]]) -> List[str]:
    d = defaultdict(list)
# establish the graph
    for flight in tickets:
        d[flight[0]].append(flight[1])

    trips = ["SEA"]

    def dfs(start): # start 
        # start point populate all the children to run         
        #base condition

        if len(trips) == len(tickets) + 1:
            print(trips)
            return trips

        # further steps 
        myDests = sorted(d[start]) #SFO

        for dst in myDests:
            d[start].remove(dst)
            trips.append(dst)  # SEA + SFO + LAX + DXW + BOS + JFK == 6 node city
            # left dfs 
            tmptrip = dfs(dst)

            if tmptrip:
                return tmptrip # this the basic return the city name or list of city name
            #backtacking from here pop the dst
            trips.pop()
            d[start] += dst

    dfs("SEA")

tickets = [("DXW", "BOS"), ("SEA", "SFO"),("LAX", "DXW"),("BOS", "JFK"), ("SFO", "LAX")]

findItinerary(tickets)