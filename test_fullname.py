from tester import sayFullName

def test_fname_lname():
    """ Unit test case to validate function by giving only first and last names """
    fn=sayFullName('Shankar','Shunmugavel')
    assert fn=='Shankar Shunmugavel'

def test_fn_ln_mn():
    """ Unit test case to validate fn by giving all 3 fn, mn and last names """
    fn=sayFullName('Shankar','Shunmugavel','Manick')
    assert fn=='Shankar Manick Shunmugavel'

def test_either_fn_or_ln():
    """ Unit test case to validate fn by giving only one name """
    fn=sayFullName('Shankar')
    assert fn=='Shankar'