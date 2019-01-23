# /usr/bin/env python

# This file is part of checkdigit.

# checkdigit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# checkdigit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with checkdigit.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time
from config import test

sys.path.append("../")  # Go back a directory
from checkdigit import luhn

start_time = time.time()

test(luhn.luhn_calculate('53251309870224'), '3', 'luhn_calculate(1)')
test(luhn.luhn_calculate('601195843045086'), '9', 'luhn_calculate(2)')
test(luhn.luhn_calculate('543669577125419'), '0', 'luhn_calculate(3)')
test(luhn.luhn_calculate('436076111511668'), '6', 'luhn_calculate(4)')
test(luhn.luhn_calculate('37266630277430'), '0', 'luhn_calculate(5)')
test(luhn.luhn_calculate('91497796683515'), '3', 'luhn_calculate(6)')
test(luhn.luhn_calculate('10408772972296'), '9', 'luhn_calculate(7)')

test(luhn.luhn_validate('541756116585277'), True, 'luhn_validate(1)')
test(luhn.luhn_validate('526012730485489'), True, 'luhn_validate(2)')
test(luhn.luhn_validate('515853022176176'), True, 'luhn_validate(3)')
test(luhn.luhn_validate('6011365035868968'), True, 'luhn_validate(4)')
test(luhn.luhn_validate('372098369216316'), True, 'luhn_validate(5)')
test(luhn.luhn_validate('4556098986775827'), True, 'luhn_validate(6)')

finish_time = time.time()


def luhn_time():
    return finish_time - start_time