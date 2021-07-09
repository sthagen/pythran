import numpy as np
import builtins

#pythran export _create_binned_data(int64[:], int[:], float[:,:], int)
#pythran export _create_binned_data(int64[:], int[:], int[:,:], int)
#pythran export _create_binned_data(intc[:], int[:], float[:,:], int)
#pythran export _create_binned_data(intc[:], int[:], int[:,:], int)
#pythran export _create_binned_data(int[:], int[:], float[:,:], int)
#pythran export _create_binned_data(int[:], int[:], int[:,:], int)
def _create_binned_data(bin_numbers, unique_bin_numbers, values, vv):
    """ Create hashmap of bin ids to values in bins
    key: bin number
    value: list of binned data
    """
    bin_map = dict()
    for i in unique_bin_numbers:
        bin_map[i] = []
    for i in builtins.range(len(bin_numbers)):
        bin_map[bin_numbers[i]].append(values[vv, i])
    return bin_map


#pythran export _calc_binned_statistic(int, int64[:], float[:,:], float[:,:], str)
#pythran export _calc_binned_statistic(int, int64[:], float[:,:], int[:,:], str)
#pythran export _calc_binned_statistic(int, intc[:], float[:,:], float[:,:], str)
#pythran export _calc_binned_statistic(int, intc[:], float[:,:], int[:,:], str)
#pythran export _calc_binned_statistic(int, int[:], float[:,:], float[:,:], str)
#pythran export _calc_binned_statistic(int, int[:], float[:,:], int[:,:], str)
def _calc_binned_statistic(Vdim, bin_numbers, result, values, stat_func):
    unique_bin_numbers = np.unique(bin_numbers)
    for vv in builtins.range(Vdim):
        bin_map = _create_binned_data(bin_numbers, unique_bin_numbers,
                                      values, vv)
        for i in unique_bin_numbers:
            # if the stat_func is np.std, calc std only when binned data is 2
            # or more for speed up.
            if stat_func == 'std':
                if len(bin_map) >= 2:
                    result[vv, i] = np.std(np.array(bin_map[i]))
            elif stat_func == 'median':
                result[vv, i] = np.median(np.array(bin_map[i]))
            elif stat_func == 'min':
                result[vv, i] = np.min(np.array(bin_map[i]))
            elif stat_func == 'max':
                result[vv, i] = np.max(np.array(bin_map[i]))
            else:
                raise Exception('Exception: {stat_func} is not supported')