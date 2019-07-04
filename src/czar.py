import re

pattern = re.compile(
        r"^(?P<functionalTaxon>(?P<functionalClass>\w{2})"
        r"(?P<functionalIncrement>\d{1,})"
        r"(?P<beamPath>\w{1,}\d{0,}\w{0,}))[:-]"
        r"(?P<fungibleTaxon>[\w\d_]{3,}[:-]|)"
        r"(?P<component>\w{3,}?)[:-]?(?P<componentIncrement>\d*)"
        r"($|[:-](?P<auxiliaryPV>.{3,})$)")


pattern = re.compile(r"^(?P<functionalTaxon>(?P<functionalClass>\w{2})(?P<functionalIncrement>\d{1,})(?P<beamPath>\w{1,}\d{0,}\w{0,})):((?P<fungibleTaxon>[\w\d_]{3,}):|)(?P<component>\w{3,}?):?(?P<componentIncrement>\d*)($|:(?P<auxiliaryPV>.{3,})$)")


def describe(Name):

        '''
        Returns a dictionary of all the elements of a well formed name.

        Raises a ValueError if the name doesn't conform (ie. doesn't
         match the regex).

        ### Increments
        May come with zero padding. Strip and convert as you like.
        '''
        match = re.search(pattern, Name)

        if match is None:
                raise ValueError

        NameDict = match.groupdict()

        return NameDict


def name(NameDict):
        '''
        Returns a properly formatted device name from a dictionary.

        Dictionary must include all elements of a name, omitted increments
         will be set to 01. <todo>
        '''
        theName = '{functionalClass}{functionalIncrement}{beamPath}:' \
                  '{fungibleTaxon}:{component}:{componentIncrement}:' \
                  '{auxiliaryPV}'.format(
                        **NameDict)

        if re.search(pattern, theName) is None:
                raise ValueError

        return theName


def human_readable(Name):
        '''Produce a human-readable description of the name'''

        NameDict = describe(Name)
        humanReadableDescription = '''This name refers to the \
        {componentIncrementTranslated} {componentTaxonTranslated}'''.format(
                **NameDict
        )

        # This will take a bit more work to really pull off

        return humanReadableDescription
