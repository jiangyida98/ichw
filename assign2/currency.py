"""currency.py: Description of how to exchange currency.
__author__ = "Yida Jiang"
__pkuid__  = "1700011739"
__email__  = "1700011739@pku.edu.cn"
"""

def inp():
    #input
    global cfrom
    global cto
    global num
    cfrom=input('input currency which you want to exchange:(USD,EUR,CNY)')
    cto=input('input currency which you want to exchange to:(USD,EUR,CNY)')
    num=float(input('nput the amount of currency which you want to exchange:'))

def testAll():
    """test all cases"""
    test_A()
    test_B()
    test_C()
    print("All tests passed")

def test_A():
    #test USD to EUR
    assert 2<exchange('USD','EUR',2.5)<2.4
    
def test_B():
    #test EUR to CNY
    assert 18<exchange('EUR','CNY',2.5)<21

def test_C():
    #test CNY to USD
    assert 0.25<exchange('CNY','USD',2.5)<0.5

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    #import mod
    from urllib.request import urlopen
    import string
    
    #get result from web
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    #extract result
    list_result=[]
    swift=0
    extract=0
    for i in jstr:
        if i in string.digits:
            swift=1
            if extract==1:
                list_result.append(i)
        if swift==1 and i ==' ':
            extract=1
            if not list_result==[]:
                extract=0
        if i =='.'and extract==1:
            list_result.append(i)
            
    #return result
    result=float(''.join(list_result))
    return result
        
    
if __name__ == '__main__':
    """
    it's time to run it.
    """
    #input
    inp()
    
    #get result
    print(exchange(cfrom,cto,num))
    # if you want to make a friendly code: print(str(num)+cfrom+' can exchange '+str(exchange(cfrom,cto,num))+cto)

    #test
    testAll()

