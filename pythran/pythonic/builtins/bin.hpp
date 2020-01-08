#ifndef PYTHONIC_BUILTIN_BIN_HPP
#define PYTHONIC_BUILTIN_BIN_HPP

#include "pythonic/include/builtins/bin.hpp"

#include "pythonic/types/str.hpp"
#include "pythonic/utils/functor.hpp"

#include <sstream>

PYTHONIC_NS_BEGIN

namespace builtins
{
  template <class T>
  types::str bin(T const &v)
  {
    long unsigned int i = 1L << (8 * sizeof(T) - 1);
    while (i && !(v & i))
      i >>= 1;
    if (!i)
      return "0b0";
    else {
      std::ostringstream oss;
      oss << "0b";
      for (; i; i >>= 1)
        if (v & i)
          oss << "1";
        else
          oss << "0";
      return oss.str();
    }
  }
}
PYTHONIC_NS_END

#endif
