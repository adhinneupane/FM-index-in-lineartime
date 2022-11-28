# CSC7300


### Wavelet tree Documentation

<b>The tree supports 3 operations track_symbol/access ,  rank , select</b>

Same concept as explained in this video https://youtu.be/JszVzStky1E?list=PL2mpR0RYFQsADmYpW2YWBrXJZ6EL3nu
  


    track_symbol(position)  returns the position of a character (similar to access operation) 
      usage: wavelet_tree.track_symbol(position)
      example: print(wavelet_tree.track_symbol(2))
      input: e $ l p p a 
      output:  $

    rank_query(character, position) returns the rank of character until the specified position
      usage: wavelet_tree.rank_query(character, position)
      example: print(wavelet_tree.rank_query('p', 5))
      input: e $ l p p a 
      output: 2


    select_query(character, position) returns the position of the jth(position) occurrence of character in input
      usage: wavelet_tree.select_query(character, position)
      example: print(wavelet_tree.select_query('l', 1))
      input: e $ l p p a
      output: 3


To run the wavelet tree and perform these operations use the following command

    python main.py <inputtextfile>

in our case
  
    python main.py bwt.txt

main.py calls each of the function with hardcoded input, the functions can be called again with your queries as defined above.

