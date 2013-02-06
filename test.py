
import one
import two, three, four
import five as blah, six as blah, seven, eight as blah
from nine import blahblah
from ten import blabhblabhab as foobar
from eleven import asdf, asrc, arst as ar, ardf
x = __import__('twelve')
y = __import__('thirteen', globals(), locals(), ['eggs', 'sausage'], -1)
print "hello, world!"
