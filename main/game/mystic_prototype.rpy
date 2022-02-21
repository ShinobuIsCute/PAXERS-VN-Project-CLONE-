'''
DESIGN

Turn based style with time bars for action activations (ie somewhat like https://youtu.be/eyYkdqm8BaA, not exactly, but similar system with timeline-turn based gameplay thing)

Spells are constructed by placing Arcana on a pointy-top hexagonal board indexed by axial coordinates. https://www.redblobgames.com/grids/hexagons/
 Board will have obstacles and pre-placed arcana depending on encounter.

Player gets an amount of different arcana types from story choices (maybe add optional objectives, conversations, etc. to add variety in how they're obtained)

The player can run out of some arcana within an encounter, but they will always be restored for the next encounter. Some default arcana (perhaps some obtained arcana as well) will be infinite.

Arcana have different properties (stuff like damage types, elemental attributes, time (chronos) cost, mana cost, bonuses for certain board configurations with other arcana, and so on)
Arcana have "manaflow" directions: each arcana is represented by a hexagon, and some of that hexagons sides will have imaginary arrows pointing out of them, representing which sides of that arcana will activate subsequent arcana. 
Arcana can be rotated, but have predefined number and topology for their manaflow directions (ie there are 3 different hexagons with two arrows pointing out of their sides which are not the same under rotational symmetry)
The root arcana has manaflow on every side of the hexagon, and all manaflow out of the root arcana must flow back (ie player must create loops of manaflow starting and ending at the root arcana when placing arcana to complete a spell)
Manaflow can branch, but all of it must return to the root somehow.
    - Final spell properties will be computed by traversing a directed acyclic graph* of arcana
    - Once the player creates a valid spell, they can click a button to cast it: it will be cast in a number of time units determined by the chronos cost of that spell, and will cost mana, 
    which the player regenerates a certain amount of (dependant on the encounter) every time unit. There may be other costs associated with casting a spell, 
    other than indirect opportunity cost of not being able to cast other spells due to mana limitations: for example, health cost
    *the only allowed cycles are those that start and end at the root arcana

Different encounter types: combat, puzzle

Combat encounters have spells/actions with different properties laid out on the enemy timeline (these actions get activated against the player after a certain number of time units), as well as enemies with health
    - Player needs to cast spells at correct times and with correct properties in order to block, counter, reflect, resist, and otherwise respond to enemy actions
    - Player needs to cast spells with correct damage types, properties, etc. in order to deal damage and kill enemies.
    - Should be ways of making utility spells which, for example, move enemy actions around on the timeline, move enemy positional order, and so on.

Puzzle encounters require the player to cast spells within a certain timeframe (ie chronos doesn't go over limit) that meet certain conditions (ie a spell with a certain combination of elemental attributes in the correct ratio)

General UI layout:

Hexagonal board takes up most of screen (probably a hexagon made of hexagons, about 5 hexagons radius (?) maybe dependant on encounter)
Player timeline on the top left half of the screen. Enemy timeline OR puzzle objective on the top right half of the screen.
Basic buttons all on bottom right.
    "Cast" button casts the current arcana configuration as a complete spell and puts it on the players timeline if that configuration is valid.
    "Play" button forwards time until the next action (enemy or player) is activated.
    Play button gets replaced with "Pause" button while running. Pause button does the obvious.
    "Next" button forwards time by one chronos (one time unit)

Player mana amount (and an indicator for mana regen amount per chronos), player health, and buffs/debuffs, all displayed below player timeline in top left.
Enemy Health amounts and positional order displayed vertically on the right side of the screen

Notes:
    Current plan is to have a json format for implementing different arcana; I'll write a static method to load them all into an array for use in the minigame

    Maybe add companions (ie getting certain characters to help you out) to combat/puzzle encounters? Would be cool if they gave modifiers and bonuses to normal encounters, and some encounters could require one or more companions
    - Good opportunity for character interactions and fun dialogue while encounters happen
    - Enemies should def get dialogue during encounters as well

TODO: 

once systems are implemented as well as a prototype UI, come up with good terms for everything, build off of stuff already in the game (attributes and such), make some arcana, make some encounters, balance them properly.


'''

python:
    class Arcana:
        #Retrieve arcana defined in a json file
        #TODO: Decide on arcana json format and implement this
        @staticmethod
        def loadArcana(file):
            pass
        def __init__(self, position, empty=True):
            # directions start at "top right" side of the pointy-topped hexagon before any orientation is applied
            self.directions = [False, False, False, False, False, False]
            # Represents number of clockwise rotations of the hexagon.
            self.orientation = 0
            self.position = position
            self.empty = empty
        def transformedDirection(self, i):
            return self.directions[i - self.orientation]
        def update(self):
            pass
        def rotate(self, n):
            self.orientation += n
            self.orientation %= 6
        def getPositionsFromDirections(self):
            return []

            
    class ArcanaNode:
        def __init__(self, graph, arcana):
            self.traversed = False
            if graph == None:
                raise ValueError "ArcanaNode: No graph defined on node creation"
                return
            self.graph = graph

            if arcana == None:
                raise ValueError "ArcanaNode: No arcana deifned on node creation"
            self.arcana = arcana

            self.children = [None, None, None, None, None, None]


    class TraversalFunction:
        #NOTE: all accumulators must check for None case of the current value because None is passed in when traversal starts.
        #      all accumulators must also return self.err when self.err is one of the parameters so that the error state is fed back to the start of recursion.
        #TODO: think of better way to implement error system that gives more feedback to the player about what is going wrong in their spell configuration (other than just that it doesnt work)
        def __init__(self, f, accumulator, base, err):
            self.f = f
            self.accumulator = accumulator
            self.err = err
            #self.base = base
    
    
    class ArcanaGraph:
        def __init__(self):
            self.MAX_DEPTH = 100
            self.root = ArcanaNode(graph = self)
        def getNeighbors(self):
            pass
        # Pass in a function and an accumulator for that function which represents some payload to be calculated in traversal.
        # Starts at the root node and traverses children recursively, information about the current node, children nodes, and the last node traversed is available.
        # Coordinate transformations on the hex grid can be used to access other nodes as well.
        def traverse(self, traversal_function, multi_traverse=False):
            self._traverse(self.root, traversal_function, None, multi_traverse)

        # TODO: Maybe implement tail recursion? Probably not needed though and idk if python even optimises it
        # Recursive traverse
        def _traverse(self, node, traversal_function, result, multi_traverse, depth=0):
            # When recursion loops back to the root node, the recursive accumulation chain all "collapses" back to the root, then the root returns the accumulated result on the very last return statement.
            if node == self.root and root.traversed:
                return result
            node.traversed = True

            # increase recursion depth counter by one for each recursive call: if counter gets to 100 (will only happen if there is a non-root cycle since boards are small-ish), stop recursion and return the error state of the traversal function
            depth += 1
            if depth > self.MAX_DEPTH:
                return traversal_function.err
            
            # recursively accumulate contributions to the traversal function of children of this node with the current node
            for child in node.children:
                if child != None: 
                    # When multi_traverse is True, accumulate even for nodes which were already visited (ie count the same node as part of the calculation even if it's visited more than once by different recursion branches)
                    # The same node will occur more than once in different recursion branches when the graph branches and then recombines later
                    if multi_traverse:
                        result = traversal_function.accumulator(self._traverse(child, traversal_function, result, multi_traverse, depth), traversal_function.f(node))
                    else:
                        if not child.traversed:
                            # Don't need to continue traversing when child.traversed is True because that must mean that another recursion branch has already accounted for further nodes.
                            result = traversal_function.accumulator(self._traverse(child, traversal_function, result, multi_traverse, depth), traversal_function.f(node))
                            child.traversed = True
                    #self._traverse(child, traversal_function, result, multi_traverse, depth)
            
            #inefficient way of doing this, but it will work: if need to optimize later, just add node.leaf bool to nodes on graph construction that just gets set to true by default and set to false when any children are inserted.
            #should only happen if there is manaflow that does not flow back to the root node anyways
            if all(child == None for child in node.children):
                return traversal_function.err

            # traversal gets here and returns accumulated values for everything, including finally at the beginning root node once the entire graph has been traversed and everything has been accumulated.
            return result
            


    # A spell is represented by a directed acyclic graph of Arcana on a board: spell statistics are calculated by traversing the graph from a predefined root node. 
    # Each arcana is hexagonal and is capable of "pointing" in up to 6 directions at once (number of directions and where they are on the hex dependant on the arcana).
    # "Mana" flows in loops; starting at the root arcana and flowing as directed by the pointing directions of the arcana (paths may split and merge). 
    # A configuration is only valid when all mana flows back to the root node and there are no other cycles in the graph.
    class Spell:
        def __init__(self, board_size):
            #Generate Hexagonal board made of hexagons with center at hash key (q, r) = (board_size, board_size)
            #Uses axial coordinate system: https://www.redblobgames.com/grids/hexagons/
            self.board = {}
            self.coordinates = []
            for q in range(-board_size, board_size + 1):
                for r in range(-board_size, board_size + 1):
                    for s in range(-board_size, board_size + 1):
                        if s + q + r == 0:
                            self.board[(q, r)] = Arcana(position=(q, r))
                            coordinates.append((q, r))
                            


            self.arcanaGraph = ArcanaGraph()
        def getAdjacent(self, arcana):
            return [self.board[(arcana.position[0] - 1, arcana.position[1] - 1)],
                    self.board[(arcana.position[0] - 1, arcana.position[1] + 0)],
                    self.board[(arcana.position[0] - 1, arcana.position[1] + 1)],
                    self.board[(arcana.position[0] + 0, arcana.position[1] - 1)],
                    self.board[(arcana.position[0] + 0, arcana.position[1] + 1)],
                    self.board[(arcana.position[0] + 1, arcana.position[1] - 1)],
                    self.board[(arcana.position[0] + 1, arcana.position[1] + 0)],
                    self.board[(arcana.position[0] + 1, arcana.position[1] + 1)],
                    ]
        def generateGraph(self):
            for q, r in self.coordinates:
                arcana = self.board[(q, r)]
                if not arcana.empty
                    node = ArcanaNode(self.arcanaGraph, arcana)
                    for pos in node.getPositionsFromDirections():
                        if self.board[pos] != None:
                            self.board[]




        # Runs only when an Arcana is added or removed from the current configuration
        def onConfigurationUpdate(self):
            self.generateGraph()
            self.chronos = self.calculateChronos()
        # Calculates the time cost (chronos) of the current Arcana configuration
        def calculateChronos(self):
            pass
    

    class HexBoard:
        def __init__(self):
            #add obstacles
            pass
    #Enemies represented by 
            

    class MysticDisplayable(renpy.Displayable):
        def define_constants(self):
            self.MYSTIC_WIDTH = 1000
            self.MYSTIC_HEIGHT = 1000

        def __init__(self):
            renpy.Displayable.__init__(self)

            self.define_constants()
            
            self.background = Solid("#ffffff", xsize=self.MYSTIC_WIDTH, ysize=self.MYSTIC_HEIGHT)
            #self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT))


screen mystic():
    # named the minigame "mystic" for internal use

    default mystic = MysticDisplayable()

    #add "bg mystic"

    add mystic

    text _("Player"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text _("Eileen"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text _("Click to Begin"):
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

show eileen vhappy

if _return == "eileen":

    e "I win!"

else:

    e "You won! Congratulations."