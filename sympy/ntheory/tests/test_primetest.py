from sympy.ntheory.generate import Sieve, sieve
from sympy.ntheory.primetest import (mr, is_lucas_prp, is_square,
                                     is_strong_lucas_prp, is_extra_strong_lucas_prp, isprime, is_euler_pseudoprime,
                                     is_gaussian_prime)

from sympy.testing.pytest import slow
from sympy.core.numbers import I

def test_euler_pseudoprimes():
    assert is_euler_pseudoprime(9, 1) == True
    assert is_euler_pseudoprime(341, 2) == False
    assert is_euler_pseudoprime(121, 3) == True
    assert is_euler_pseudoprime(341, 4) == True
    assert is_euler_pseudoprime(217, 5) == False
    assert is_euler_pseudoprime(185, 6) == False
    assert is_euler_pseudoprime(55, 111) == True
    assert is_euler_pseudoprime(115, 114) == True
    assert is_euler_pseudoprime(49, 117) == True
    assert is_euler_pseudoprime(85, 84) == True
    assert is_euler_pseudoprime(87, 88) == True
    assert is_euler_pseudoprime(49, 128) == True
    assert is_euler_pseudoprime(39, 77) == True
    assert is_euler_pseudoprime(9881, 30) == True
    assert is_euler_pseudoprime(8841, 29) == False
    assert is_euler_pseudoprime(8421, 29) == False
    assert is_euler_pseudoprime(9997, 19) == True

def test_is_extra_strong_lucas_prp():
    assert is_extra_strong_lucas_prp(4) == False
    assert is_extra_strong_lucas_prp(989) == True
    assert is_extra_strong_lucas_prp(10877) == True
    assert is_extra_strong_lucas_prp(9) == False
    assert is_extra_strong_lucas_prp(16) == False
    assert is_extra_strong_lucas_prp(169) == False

@slow
def test_prps():
    oddcomposites = [n for n in range(1, 10**5) if
        n % 2 and not isprime(n)]
    # A checksum would be better.
    assert sum(oddcomposites) == 2045603465
    assert [n for n in oddcomposites if mr(n, [2])] == [
        2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141,
        52633, 65281, 74665, 80581, 85489, 88357, 90751]
    assert [n for n in oddcomposites if mr(n, [3])] == [
        121, 703, 1891, 3281, 8401, 8911, 10585, 12403, 16531,
        18721, 19345, 23521, 31621, 44287, 47197, 55969, 63139,
        74593, 79003, 82513, 87913, 88573, 97567]
    assert [n for n in oddcomposites if mr(n, [325])] == [
        9, 25, 27, 49, 65, 81, 325, 341, 343, 697, 1141, 2059,
        2149, 3097, 3537, 4033, 4681, 4941, 5833, 6517, 7987, 8911,
        12403, 12913, 15043, 16021, 20017, 22261, 23221, 24649,
        24929, 31841, 35371, 38503, 43213, 44173, 47197, 50041,
        55909, 56033, 58969, 59089, 61337, 65441, 68823, 72641,
        76793, 78409, 85879]
    assert not any(mr(n, [9345883071009581737]) for n in oddcomposites)
    assert [n for n in oddcomposites if is_lucas_prp(n)] == [
        323, 377, 1159, 1829, 3827, 5459, 5777, 9071, 9179, 10877,
        11419, 11663, 13919, 14839, 16109, 16211, 18407, 18971,
        19043, 22499, 23407, 24569, 25199, 25877, 26069, 27323,
        32759, 34943, 35207, 39059, 39203, 39689, 40309, 44099,
        46979, 47879, 50183, 51983, 53663, 56279, 58519, 60377,
        63881, 69509, 72389, 73919, 75077, 77219, 79547, 79799,
        82983, 84419, 86063, 90287, 94667, 97019, 97439]
    assert [n for n in oddcomposites if is_strong_lucas_prp(n)] == [
        5459, 5777, 10877, 16109, 18971, 22499, 24569, 25199, 40309,
        58519, 75077, 97439]
    assert [n for n in oddcomposites if is_extra_strong_lucas_prp(n)
            ] == [
        989, 3239, 5777, 10877, 27971, 29681, 30739, 31631, 39059,
        72389, 73919, 75077]


def test_isprime():
    s = Sieve()
    s.extend(100000)
    ps = set(s.primerange(2, 100001))
    for n in range(100001):
        # if (n in ps) != isprime(n): print n
        assert (n in ps) == isprime(n)
    assert isprime(179424673)
    assert isprime(20678048681)
    assert isprime(1968188556461)
    assert isprime(2614941710599)
    assert isprime(65635624165761929287)
    assert isprime(1162566711635022452267983)
    assert isprime(77123077103005189615466924501)
    assert isprime(3991617775553178702574451996736229)
    assert isprime(273952953553395851092382714516720001799)
    assert isprime(int('''
531137992816767098689588206552468627329593117727031923199444138200403\
559860852242739162502265229285668889329486246501015346579337652707239\
409519978766587351943831270835393219031728127'''))

    # Some Mersenne primes
    assert isprime(2**61 - 1)
    assert isprime(2**89 - 1)
    assert isprime(2**607 - 1)
    # (but not all Mersenne's are primes
    assert not isprime(2**601 - 1)

    # pseudoprimes
    #-------------
    # to some small bases
    assert not isprime(2152302898747)
    assert not isprime(3474749660383)
    assert not isprime(341550071728321)
    assert not isprime(3825123056546413051)
    # passes the base set [2, 3, 7, 61, 24251]
    assert not isprime(9188353522314541)
    # large examples
    assert not isprime(877777777777777777777777)
    # conjectured psi_12 given at http://mathworld.wolfram.com/StrongPseudoprime.html
    assert not isprime(318665857834031151167461)
    # conjectured psi_17 given at http://mathworld.wolfram.com/StrongPseudoprime.html
    assert not isprime(564132928021909221014087501701)
    # Arnault's 1993 number; a factor of it is
    # 400958216639499605418306452084546853005188166041132508774506\
    # 204738003217070119624271622319159721973358216316508535816696\
    # 9145233813917169287527980445796800452592031836601
    assert not isprime(int('''
803837457453639491257079614341942108138837688287558145837488917522297\
427376533365218650233616396004545791504202360320876656996676098728404\
396540823292873879185086916685732826776177102938969773947016708230428\
687109997439976544144845341155872450633409279022275296229414984230688\
1685404326457534018329786111298960644845216191652872597534901'''))
    # Arnault's 1995 number; can be factored as
    # p1*(313*(p1 - 1) + 1)*(353*(p1 - 1) + 1) where p1 is
    # 296744956686855105501541746429053327307719917998530433509950\
    # 755312768387531717701995942385964281211880336647542183455624\
    # 93168782883
    assert not isprime(int('''
288714823805077121267142959713039399197760945927972270092651602419743\
230379915273311632898314463922594197780311092934965557841894944174093\
380561511397999942154241693397290542371100275104208013496673175515285\
922696291677532547504444585610194940420003990443211677661994962953925\
045269871932907037356403227370127845389912612030924484149472897688540\
6024976768122077071687938121709811322297802059565867'''))
    sieve.extend(3000)
    assert isprime(2819)
    assert not isprime(2931)
    assert not isprime(2.0)


def test_is_square():
    assert [i for i in range(25) if is_square(i)] == [0, 1, 4, 9, 16]

    # issue #17044
    assert not is_square(60 ** 3)
    assert not is_square(60 ** 5)
    assert not is_square(84 ** 7)
    assert not is_square(105 ** 9)
    assert not is_square(120 ** 3)

def test_is_gaussianprime():
    assert is_gaussian_prime(7*I)
    assert is_gaussian_prime(7)
    assert is_gaussian_prime(2 + 3*I)
    assert not is_gaussian_prime(2 + 2*I)
