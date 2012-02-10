# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
#
# notes: run with: python pacman.py

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

DEBUG = True

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  ['South',s,'West',s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  """
  run with:
  python pacman.py -l tinyMaze -p SearchAgent;
  python pacman.py -l mediumMaze -p SearchAgent;
  python pacman.py -l bigMaze -p SearchAgent -z .5
  """
  print "Start:", problem.getStartState()
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  successors = problem.getSuccessors(problem.getStartState() )
  actions = [action for s, action, p in successors]
  L = [0,1,2,3,4]
  L[2:] = []
  print L
  
  return genericSearch(problem, -1)

def genericSearch(problem, x):
  # initialize variables
  actions = []		# list of actions
  frontier = util.PriorityQueue()		# priority queue of (node, depth)
  explored = set()		# explored set of states
  
  rootNode = (problem.getStartState(), None, 0)	# (state, action, depth)
  frontier.push(rootNode, 0)
  if DEBUG: assert set() == set([])
  #if DEBUG: print dir(list)
  
  while frontier != set() :
    raw_input('waiting for input...')
    node = state, action, depth = frontier.pop()
    if DEBUG: print 'popped node: ' + str(node)
    actions[depth-1:] = []		# reset actions to current node
    if action is not None:
    	actions.append(action)
    if DEBUG: print 'action stack: ' + str(actions[-12:])
    # add state to explored set
    explored.add(state)
    
    # test for goal state
    if problem.isGoalState(state):
      if DEBUG: print 'returning actions: ' + str(actions)
      return actions
    
    # add successors to frontier
    depth += 1
    #if DEBUG: print 'depth: ' + str(depth)
    for state, action, c in problem.getSuccessors(state):
        if state not in explored:
          frontier.push((state, action, depth), x*depth)
  
  if DEBUG: print 'frontier empty'
  return actions

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  """
  run with:
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
  """
  
  return genericSearch(problem, 1)
  
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
