'''
Jett Kopalek
CSCI 395
Homework 2: Arad to Bucharest Searching

This program finds a path between Arad and Bucharest using BFS DFS and IDS/DLS
'''

#Import required files
from map_ import map_
from city import city
from bfs import BFS
from dfs import DFS
from ids import IDS

def printBFS(Romania):
    bfs = BFS(Romania)
    path, distance = bfs.search("Arad", "Bucharest")
    print(f"\nBFS path from Arad to Bucharest: {toString(path)}")
    print(f"Total Distance: {distance}")

def printDFS(Romania):
    dfs = DFS(Romania)
    path, distance = dfs.search("Arad", "Bucharest")
    print(f"\nDFS path from Arad to Bucharest: {toString(path)}")
    print(f"Total Distance: {distance}")  
    
def printIDS(Romania):
    ids = IDS(Romania)
    path, distance = ids.search("Arad", "Bucharest")
    print(f"\nIDS path from Arad to Bucharest: {toString(path)}")
    print(f"Total Distance: {distance}")

def toString(path):
    return " => ".join(path)

def main():
    Romania = map_()
    printBFS(Romania)
    printDFS(Romania)
    printIDS(Romania)
    
main()