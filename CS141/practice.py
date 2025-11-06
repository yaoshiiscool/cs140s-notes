#Practice problems for Midterm

from math import sqrt
def count_suffix_names(lst,suffix):
    count = 0
    suff_r = list(suffix)[-1]
    lst_r = []
    for item in lst:
        word_lst = list(item)
        word_lst_r = word_lst[-1]
        lst_r.append(word_lst_r)
        if word_lst_r == suff_r:
            count += 1
    return count 

def create_inverted_index(book):
    invert_index = [[]]*len(book)
    for n,page in enumerate(book):
        for refr in page:
            invert_index[refr].append(n)
    return invert_index

def compute_rms_profile(profiles):
    rows = len(profiles)
    k = len(profiles[0])
    output = []
    for i in range(k):
        output.append([])
    for profile in profiles:
        for n, item in enumerate(profile):
            output[n].append(item**2)
    for p, l in enumerate(output):
        output[p] = sqrt(sum(l)/rows)
    return output

compute_rms_profile([[1,2,1],[2,0,4],[3,5,2]])
compute_rms_profile([(4.0,5.2),(4.7,5.0),(10.6,12.6),(9.8,10.1)])
