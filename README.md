A method for expanding a real number into Egyptian fraction expansion.
Numbers close to eachother yield similar expansions.

Discovered as an answer to the question: how to optimally scale a fraction a/b and reduce it by adding
an integer to the numerator and/or the denominator such that the result in the lowest terms is as close to 1/1.
(i.e. for 3/5 we can scale by 2 to 6/10 and add -1 to the numerator to get 1/2, then add -1 to the denominator to get 1/1. 
In total we had to add 2 (in absolute value).) 

For rational numbers:
  let a/b be a fraction in the lowest terms.
  1. find the Bézout coefficients x,y such that ax-by=1** (1)
  2. scale by x to get ax/bx and add -1 to the numerator
  3. the result (ax-1)/(bx) is equivalent, using (1), to by/bx
  4. reduce to y/x
  5. sutract: a/b - y/x | the result is a unit fraction***
  repeat the same process for y/x until one of the Bézout coefficients is 1
  
  the result is an Egyptian fraction expansion of a/b
  applying this process to a Cauchy sequence yields expansions for the reals
  however the expansion converges nicely only for roots (?)

  example for sqrt(2): 1+1/3+1/15+1/85+1/493+1/2871+1/16731+...

** The method works even for the condition ax-by=-1, but may result in an expansion with negative terms. 

*** a/b - y/x = (ax-by)/(by) = 1/(by) using (1) Q.E.D - the result is always a unit fraction


