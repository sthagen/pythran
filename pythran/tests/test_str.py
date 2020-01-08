from pythran.tests import TestEnv
from pythran.typing import List

import unittest


class TestStr(TestEnv):
    """
    def test_str_startswith0(self):
        self.run_test("def str_startswith0(s0, s1): return s0.startswith(s1)", "barbapapa", "barba", str_startswith0=[str, str])

    def test_str_startswith1(self):
        self.run_test("def str_startswith1(s0, s1): return s0.startswith(s1)", "barbapapa", "barbi", str_startswith1=[str, str])

    def test_str_endswith0(self):
        self.run_test("def str_endswith0(s0, s1): return s0.endswith(s1)", "barbapapa", "papa", str_endswith0=[str, str])

    def test_str_endswith1(self):
        self.run_test("def str_endswith1(s0, s1): return s0.endswith(s1)", "barbapapa", "papy", str_endswith1=[str, str])

    def test_str_empty(self):
        self.run_test("def str_empty(s0): return '>o_/' if s0 else '0x0'", "", str_empty=[str])

    def test_str_failed_conversion(self):
        self.run_test("def str_failed_conversion(s):\n try: return int(s)\n except: return 42", "prout", str_failed_conversion=[str])

    def test_str_replace0(self):
        self.run_test("def str_replace0(s): return s.replace('er', 'rer')", "parler", str_replace0=[str])

    def test_str_replace1(self):
        self.run_test("def str_replace1(s): return s.replace('er', 'rer', 1)", "erlang manger dessert", str_replace1=[str])

    def test_str_replace2(self):
        self.run_test("def str_replace2(s): return s.replace('', 'du vide surgit rien', 1)", "j aime les moulinettes a fromage", str_replace2=[str])

    def test_str_ascii_letters(self):
        self.run_test("def str_ascii_letters(): import string; return string.ascii_letters", str_ascii_letters=[])

    def test_str_ascii_lowercase(self):
        self.run_test("def str_ascii_lowercase(): import string; return string.ascii_lowercase", str_ascii_lowercase=[])

    def test_str_ascii_uppercase(self):
        self.run_test("def str_ascii_uppercase(): import string; return string.ascii_uppercase", str_ascii_uppercase=[])

    def test_str_digits(self):
        self.run_test("def str_digits(): import string; return string.digits", str_digits=[])

    def test_str_hexdigits(self):
        self.run_test("def str_hexdigits(): import string; return string.hexdigits", str_hexdigits=[])

    def test_str_octdigits(self):
        self.run_test("def str_octdigits(): import string; return string.octdigits", str_octdigits=[])

    def test_str_lower(self):
        self.run_test("def str_lower(s): return s.lower()", "ThiS iS a TeST", str_lower=[str])

    def test_str_upper(self):
        self.run_test("def str_upper(s): return s.upper()", "ThiS iS a TeST", str_upper=[str])

    def test_str_capitalize(self):
        self.run_test("def str_capitalize(s): return s.capitalize()", "thiS iS a TeST", str_capitalize=[str])

    def test_str_strip(self):
        self.run_test("def str_strip(s): return s.strip()", "       ThiS iS a TeST        ", str_strip=[str])

    def test_str_strip2(self):
        self.run_test("def str_strip2(s): return s.strip(\"TSih\")", "ThiS iS a TeST", str_strip2=[str])

    def test_str_lstrip(self):
        self.run_test("def str_lstrip(s): return s.lstrip()", "       ThiS iS a TeST        ", str_lstrip=[str])

    def test_str_lstrip2(self):
        self.run_test("def str_lstrip2(s): return s.lstrip(\"TSih\")", "ThiS iS a TeST", str_lstrip2=[str])

    def test_str_rstrip(self):
        self.run_test("def str_rstrip(s): return s.rstrip()", "       ThiS iS a TeST        ", str_rstrip=[str])

    def test_str_rstrip2(self):
        self.run_test("def str_rstrip2(s): return s.rstrip(\"TSih\")", "ThiS iS a TeST", str_rstrip2=[str])

    def test_str_format(self):
        self.run_test("def str_format(a): return '%.2f %.2f' % (a, a)", 43.23, str_format=[float])

    def test_str_join0(self):
        self.run_test("def str_join0(): a = ['1'] ; a.pop() ; return 'e'.join(a)", str_join0=[])

    def test_str_join1(self):
        self.run_test("def str_join1(): a = ['l', 'l'] ; return 'o'.join(a)", str_join1=[])

    def test_str_join2(self):
        self.run_test("def str_join2(a): return 'o'.join(filter(len, a))", ['l', 'l'], str_join2=[List[str]])

    def test_str_find0(self):
        self.run_test("def str_find0(s): return s.find('pop')", "popop", str_find0=[str])

    def test_str_find1(self):
        self.run_test("def str_find1(s): return s.find('pap')", "popop", str_find1=[str])

    def test_str_reversal(self):
        self.run_test("def str_reversal(s): return map(ord,reversed(s))", "dear", str_reversal=[str])

    def test_str_substring_iteration(self):
        self.run_test("def str_substring_iteration(s): return map(ord, s[1:-1])", "pythran", str_substring_iteration=[str])

    def test_str_isalpha(self):
        self.run_test("def str_isalpha(s, t, u): return s.isalpha(), t.isalpha(), u.isalpha()", "e", "1", "", str_isalpha=[str,str, str])

    def test_str_isdigit(self):
        self.run_test("def str_isdigit(s, t, u): return s.isdigit(), t.isdigit(), u.isdigit()", "e", "1", "", str_isdigit=[str,str, str])

    def test_str_count(self):
        self.run_test("def str_count(s, t, u, v): return s.count(t), s.count(u), s.count(v)",
                      "pythran is good for health", "py", "niet", "t",
                      str_count=[str, str, str, str])

    def test_str_literal_cmp(self):
        code = '''
            def eee(a, i):
                if a == "ABCD":
                    return 2 * i
                elif a != "ZDSD":
                    return 1 * i
                return 3 * i

            def str_literal_cmp(a, i):
                if a == "EEE":
                   return eee("ZZZ", i), eee("ABCD", i)
                else:
                   return eee("YYY", i), 3'''
        self.run_test(code, "EEE", 2, str_literal_cmp=[str, int])

    def test_str_literal_cmp1(self):
        code = '''
            def eee(a, i):
                if a > "ABCD":
                    return 2 * i
                elif a <= "ZDSD":
                    return 1 * i
                return 3 * i

            def str_literal_cmp1(a, i):
                if a == "EEE":
                   return eee("ZZZ", i), eee("ABCD", i)
                else:
                   return eee("YYY", i), 3'''
        self.run_test(code, "EEE", 2, str_literal_cmp1=[str, int])

    def test_str_literal_cmp2(self):
        code = '''
            def eee(a, i):
                if a < "ABCD":
                    return 2 * i
                elif a >= "ZDSD":
                    return 1 * i
                return 3 * i

            def str_literal_cmp2(a, i):
                if a == "EEE":
                   return eee("ZZZ", i), eee("ABCD", i)
                else:
                   return eee("YYY", i), 3'''
        self.run_test(code, "EEE", 2, str_literal_cmp2=[str, int])

    def test_str_literal_add(self):
        code = '''
            def eee(a, i):
                if i > 0:
                    return a + "ABCD"
                else:
                    return a + "BCD"

            def str_literal_add(a, i):
                if a == "EEE":
                   return eee("ZZZ", i), eee("ABCD", i)
                else:
                   return eee("YYY", i), "3"'''
        self.run_test(code, "EEE", 2, str_literal_add=[str, int])

    def test_str_literal_mult(self):
        code = '''
            def eee(a, i):
                if i > 0:
                    return a * i
                else:
                    return a * 3

            def str_literal_mult(a, i):
                if a == "EEE":
                   return eee("ZZZ", i), eee("ABCD", i)
                else:
                   return eee("YYY", i), "3"'''
        self.run_test(code, "EEE", 2, str_literal_mult=[str, int])

    def test_str_float(self):
        self.run_test("def str_float(s): return float(s)", "0.000012", str_float=[str])

    def test_str_numpy_float32(self):
        self.run_test("def str_numpy_float32(s): import numpy; return numpy.float32(s)", "0.000012",
                      str_numpy_float32=[str])

    def test_str_numpy_float64(self):
        self.run_test("def str_numpy_float64(s): import numpy; return numpy.float64(s)", "0.000012",
                      str_numpy_float64=[str])

    def test_str_int(self):
        self.run_test("def str_int(s): return int(s)", "12", str_int=[str])

    def test_str_id(self):
        self.run_test("def str_id(x): return id(x) != 0", "hello", str_id=[str])
"""
    def test_str_slice_assign(self):
        self.run_test('''
            def str_slice_assign(s, c):
                if s.startswith(c):
                    s = s[len(c):];
                return s''', "LEFT-B6", "LEFT-",
                      str_slice_assign=[str, str])

    def test_str_slice_assign2(self):
        self.run_test('''
        def sample_datatype(value):
            definitions = [ 
                ('LEFT-', 1), 
                ('RIGHT-', 2), 
                ('', 3)
            ]   
        
            plate_number = None
            for definition in definitions:
                s, n = definition
                if value.startswith(s):
                    plate_number = n 
                    value = value[len(s):]
                    break
            if plate_number is None:   # Comment for make it works
               raise ValueError("Invalid value")
            return None

        def str_slice_assign2(s1):
            sample_datatype(s1)
            return s1''', "LEFT-B6", str_slice_assign2=[str])
