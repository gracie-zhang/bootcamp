import pytest
import seq_features as sf

def test_number_negatives_single_aa():
    """Perform unit tests on number_negatives() for single aa"""
    assert sf.number_negatives('E') == 1
    assert sf.number_negatives('D') == 1
    
def test_number_negatives_short_seq():
    """Perform unit tests on number_negatives() for short sequences"""
    assert sf.number_negatives('EEEEEAAAAA') == 5
        
def test_number_negatives_lowercases():
    """Perform unit tests on number_negatives() for lower case aa"""
    assert sf.number_negatives('adseds') == 3
    
def test_number_negatives_invalid_amino_acid():
    """Perform unit tests on number_negatives() for invalid aa"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.number_negatives('Z')
    excinfo.match('Z is not a valid aa you fuckface')

def test_number_positives_single_aa():
    """Perform unit tests on number_positives() for single aa"""
    assert sf.number_positives('E') == 0
    assert sf.number_positives('D') == 0
    assert sf.number_positives('R') == 1
    assert sf.number_positives('K') == 1
    assert sf.number_positives('H') == 1
    
def test_number_positives_short_seq():
    """Perform unit tests on number_positives() for short sequences"""
    assert sf.number_positives('EEEEEAAAAA') == 0
    assert sf.number_positives('KRAKRHAAAAA') == 5
        
def test_number_positives_lowercases():
    """Perform unit tests on number_positives() for lower case aa"""
    assert sf.number_positives('adseds') == 0
    assert sf.number_positives('akrhdkseds') == 4
    
def test_number_positives_invalid_amino_acid():
    """Perform unit tests on number_positives() for invalid aa"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.number_positives('Z')
    excinfo.match('Z is not a valid aa you fuckface')
    
def test_is_valid_with_Z():
    """Perform unit tests on number_positives() for invalid sequences"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.is_valid('Z')
    excinfo.match('Z is not a valid aa you fuckface')
    
def test_is_valid_with_short_but_wrong_seq():
    """Perform unit tests on number_positives() for invalid sequences"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.is_valid('ALN&&&')
    excinfo.match('& is not a valid aa you fuckface')