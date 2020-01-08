#ifndef PYTHONIC_RANDOM_SEED_HPP
#define PYTHONIC_RANDOM_SEED_HPP

#include "pythonic/include/random/seed.hpp"

#include "pythonic/utils/functor.hpp"
#include "pythonic/builtins/None.hpp"
#include "pythonic/random/random.hpp"

#include <ctime>

PYTHONIC_NS_BEGIN

namespace random
{
  types::none_type seed(long s)
  {
    __random_generator.seed(s);
    return builtins::None;
  }

  types::none_type seed()
  {
    __random_generator.seed(time(nullptr));
    return builtins::None;
  }
}
PYTHONIC_NS_END

#endif
