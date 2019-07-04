import czar
import pytest
expectedKeys = ['functionalTaxon', 'functionalClass', 'functionalIncrement',
                'beamPath', 'fungibleTaxon', 'component',
                'auxiliaryPV']

testName = 'EM1K2:GEM:VGC:2:OPN_REQ'


# Add a name to this list to make sure it stays valid for all time
@pytest.mark.parametrize("Name", [
    'EM1K2:GEM:VGC:2:OPN_REQ'
])
def test_describe_valid_name(Name):
    assert czar.describe(Name), Name + " is invalid."


# Add a name to this list to make sure it stays invalid for all time
@pytest.mark.parametrize("Name", [
    'EP2624:0002',
    'XLEM1K2G:GEM:VGC2:OPN_REQ'
    'EM1K2:GEM:VGC:2:OPN_REQasdlkj-asdfkj:asdfkj'
])
def test_describe_invalid_name(Name):
    with pytest.raises(ValueError):
        czar.describe(Name), Name + " is invalid."


def test_one_works_with_the_other():
    assert czar.name(czar.describe(testName)) == testName


@pytest.mark.parametrize("key,thing", [
    ("functionalTaxon", "EM1K2"),
    ("functionalClass", "EM"),
    ("functionalIncrement", "1"),
    ("beamPath", "K2"),
    ("fungibleTaxon", "GEM"),
    ("component", "VGC"),
    ("componentIncrement", "2"),
    ("auxiliaryPV", "OPN_REQ")
])
def test_describe_parse_functionalTaxon(key, thing):
    assert czar.describe(testName)[key] == thing
