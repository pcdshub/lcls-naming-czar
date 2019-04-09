import czar
import pytest
expectedKeys = ['functionalTaxon', 'functionalClass', 'functionalIncrement',
'beamPath', 'fungibleTaxon', 'component', 'componentIncrement', 'auxiliaryPV']

testName = 'EM1K2:GEM:VGC:02:OPN_REQ'
badName = 'XLEM1K2G:GEM:VGC:02:OPN_REQ'

#Add a name to this list to make sure it stays valid for all time
@pytest.mark.parametrize("Name", [
    'EM1K2:GEM:VGC:02:OPN_REQ'
])
def test_describe_valid_name(Name):
    assert czar.describe(Name), Name + " is invalid."

def test_describe_invalid_name():
    with pytest.raises(ValueError):
        czar.describe(badName)

def test_one_works_with_the_other():
    assert czar.name(czar.describe(testName)) == testName

@pytest.mark.parametrize("key,thing", [
    ("functionalTaxon", "EM1K2"),
    ("functionalClass", "EM"),
    ("functionalIncrement", "1"),
    ("beamPath", "K2"),
    ("fungibleTaxon", "GEM"),
    ("component", "VGC"),
    ("componentIncrement", "02"),
    ("auxiliaryPV", "OPN_REQ")
])
def test_describe_parse_functionalTaxon(key, thing):
    assert czar.describe(testName)[key] == thing
