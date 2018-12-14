import czar

expectedKeys = ['functionalTaxon', 'functionalClass', 'functionalIncrement',
'beamPath', 'fungibleTaxon', 'component', 'componentIncrement', 'elementTaxon']

testName = 'EM1K2:GEM:VGC:02:OPN_REQ'

def test_describe_functionalTaxon_capture():
    assert czar.describe(testName)['functionalTaxon'] == 'EM1K2'

