#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
       #
       ### Add you code here 
       #
    one = "|00000*****   |"
    row = ["|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" , "|00000*****|" ]
    n = 0
    y = str(value)
    v = len(y)
    z = 10 - v
    x = 0
    
    while x < z:
        print one
        x = x+1
    
    while n < v:
        row[9 -n]= row[9-n][:11 - int(y[n])] + "   " + row[9-n][11 -int(y[n]):]
        value = value / 10
        print  row [9 - n]
        n = n + 1
     
