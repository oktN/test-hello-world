from mamba import *
from expects import *

from test import Test

with description('Test') as self:
    with it('returns Hello World'):
        sent_message = "Hello World"

        test = Test(sent_message)

        returned_message = test.hello()

        expect("Hello World").to(equal(returned_message))