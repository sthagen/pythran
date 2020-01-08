#ifndef PYTHONIC_BUILTIN_STR_SPLIT_HPP
#define PYTHONIC_BUILTIN_STR_SPLIT_HPP

#include "pythonic/include/builtins/str/split.hpp"

#include "pythonic/builtins/str/strip.hpp"
#include "pythonic/types/list.hpp"
#include "pythonic/types/NoneType.hpp"
#include "pythonic/types/str.hpp"
#include "pythonic/utils/functor.hpp"

PYTHONIC_NS_BEGIN

namespace builtins
{

  namespace str
  {

    types::list<types::str> split(types::str const &in, types::str const &sep,
                                  long maxsplit)
    {
      types::str s = strip(in);
      types::list<types::str> res(0);
      size_t current = 0;
      size_t next = 0;
      long numsplit = 0;
      while (next != types::str::npos &&
             (numsplit++ < maxsplit || maxsplit == -1)) {
        next = s.find_first_of(sep, current);
        res.push_back(s.substr(current, next - current));
        current = next + 1;
      }
      if (next != types::str::npos) {
        current = next + 1;
        res.push_back(s.substr(current, s.size() - current));
      }
      return res;
    }

    types::list<types::str> split(types::str const &s, types::none_type const &,
                                  long maxsplit)
    {
      return split(s, " ", maxsplit);
    }
  }
}
PYTHONIC_NS_END
#endif
