class pretty_set(frozenset):
    """
    This class implements a frozen set with pretty printing function.
    """
    def __repr__(self):
        elems = list(self)
        if len(elems) == 0 :
            return "{}"
        result = "{" + str(elems[0])
        for e in elems[1:]:
            result += ", " + str(e)
        result += "}"
        return result



def _test_is_hashable( obj, name ):
        try:
            pretty_set( [obj] )
        except:
            msg = "In automaton module, " + name + " have to be hashable."
            if type( obj ) is set:
                msg += " Use automaton.pretty_set or frozenset instead of set."
            if type( obj ) is list:
                msg += " Use tuple instead of list. For example (1,3) instead of [1,3]."
            raise Exception( msg )


class automaton:
    def __init__(
        self, alphabet=None, epsilons=None, states=None, initials=None, finals=None, 
        transitions=None
    ):
        self._epsilons = set()
        self._states = set( )
        self._adjacence = {}
        self._initial_states = set( )
        self._final_states = set( )
        self._alphabet = set( )
        if alphabet != None:
            self.add_characters( alphabet )
        if epsilons != None :
            self.add_epsilon_characters( epsilons )
        if states != None:
            self.add_states( states )
        if transitions != None:
            self.add_transitions( transitions )
        if initials != None:
            self.add_initial_states( initials )
        if finals != None:
            self.add_final_states( finals )
    
    
    
    def add_state( self, state ):
        """
        Adds a state.
        The state have to be hashable.
        That's why you have to use:
            automaton.pretty_set or frozenset   instead of    set
            tuple                               instead of    list

        Example:

        >>> a = automaton( )
        >>> a.get_states() == set()
        True
        >>> a.add_state( 2 )
        >>> a.get_states() == set( [2] )
        True
        >>> a.add_state( (1,3) )
        >>> a.get_states() == set( [2, (1,3)] )
        True

        We get an error if we try to use a set to code a state:

        >>> a.add_state( set([1,2,5]) )
        Traceback (most recent call last):
            ...
        Exception: In automaton module, States have to be hashable. Use automaton.pretty_set or frozenset instead of set.

        The solution is to use automaton.pretty_set:

        >>> a.add_state( pretty_set([1,2,5]) )

        We get an error if we try to use a list to code a state:

        >>> a.add_state( [1,2,5] )
        Traceback (most recent call last):
            ...
        Exception: In automaton module, States have to be hashable. Use tuple instead of list. For example (1,3) instead of [1,3].

        The solution is to use a tuple:

        >>> a.add_state( (1,2,5) )
        
        """
        _test_is_hashable( state, "States" )
        self._states.add( state )
    def add_states( self, list_of_states ):
        """
        Adds a list of states.

        Example:

        >>> a = automaton( )
        >>> a.add_states( [1,2,6] )
        >>> a.get_states() == set( [1,2,6] )
        True
        """
        for state in list_of_states:
            self.add_state( state )

    def add_characters( self, list_of_characters ):
        """
        Adds all the characters of a list in the alphabet of the automaton.

        Example:

        >>> a = automaton( )
        >>> a.add_characters( ['a','b'] )
        >>> a.get_alphabet() == set( ['a','b'] )
        True
        """
        for character in list_of_characters:
            self.add_character( character )
    def add_character( self, character ):
        """
        Adds a character in the alphabet of the automaton.

        Characters have to be hashable.
        That's why you have to use:
            automaton.pretty_set or frozenset   instead of    set
            tuple                               instead of    list

        Example:

        >>> a = automaton( )
        >>> a.add_character( 'a' )
        >>> a.get_alphabet() == set( ['a'] )
        True

        We get an error if we try to use a set to code a character:

        >>> a.add_character( set([1,2,5]) )
        Traceback (most recent call last):
            ...
        Exception: In automaton module, Characters have to be hashable. Use automaton.pretty_set or frozenset instead of set.

        The solution is to use automaton.pretty_set:

        >>> a.add_character( pretty_set([1,2,5]) )

        We get an error if we try to use a list to code a character:

        >>> a.add_character( [1,2,5] )
        Traceback (most recent call last):
            ...
        Exception: In automaton module, Characters have to be hashable. Use tuple instead of list. For example (1,3) instead of [1,3].

        The solution is to use a tuple:

        >>> a.add_character( (1,2,5) )
        """
        _test_is_hashable( character, "Characters" )
        self._alphabet.add( character )