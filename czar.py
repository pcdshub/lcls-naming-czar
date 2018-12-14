import re

pattern = re.compile(r'^(?P<functionalTaxon>(?P<functionalClass>\w{2})(?P<functionalIncrement>\d{1,})(?P<beamPath>\w{1,}\d{0,}\w{0,})):(?P<fungibleTaxon>.{3,})?(?(fungibleTaxon):|)(?P<component>\w{3}):(?P<componentIncrement>\d{2,3}|[X,Y,Z]):(?P<elementTaxon>[\w|\d]+$)')

def describe(Name):
        '''
        Returns a dictionary of all the elements of a well formed name.

        Raises a ValueError if the name doesn't conform (ie. doesn't match the regex).
        '''
        match = re.search(pattern, Name)

        if match is None:
                raise ValueError

        NameDict = match.groupdict()

        return NameDict

def name(NameDict):
        '''
        Returns a properly formatted device name from a dictionary.

        Dictionary must include all elements of a name, omitted increments will be set to 01.
        '''
        theName = """{functionalClass}{functionalIncrement}{beamPath}:{fungibleTaxon}:{componentTaxon}:{componentIncrement}:{processVariable}""".format(
                **NameDict
        )

        if re.search(pattern, theName) == None:
                raise ValueError

        return theName

def human_readable(Name):
        '''Produce a human-readable description of the name'''

        NameDict = describe(Name)
        humanReadableDescription = '''This name refers to the {componentIncrementTranslated} {componentTaxonTranslated}'''.format(
                **NameDict
        )

        return humanReadableDescription


