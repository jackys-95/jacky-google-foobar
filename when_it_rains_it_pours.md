    When trying to solve this problem, do not look
    at it from left to right. My initial solution tried
    that but it was stuck on the case where the tallest
    height was on the left half of the array. This is
    because to calculate the capacity, you find the
    tallest height and subtract any height less than it
    with the tallest height and add that to the solution.

    When I put the corresponding reversed array into my
    solution, it worked. So I tried iterating through
    both sides of the list in the same loop. I will explain
    by using the test case that my original solution that only
    iterated left to right was caught on. Unfortunately I did not
    save that solution (it had only got 4/5 of the test cases so
    I deleted it...)

    heights = [5, 1, 2, 3, 1, 1, 2]

                x
                x
                x00x
                x0xx00x
                xxxxxxx

    The flawed original solution would calculate 
    incorrectly because it never finds anything taller than 5.
    But if you go right to left, you will find increasing heights
    requisite for the calculation of

    (tallest_height_so_far - current_height)

    We are left with some conditions to make the loop work...
    
    Define left peak as the tallest discovered height so far
    on the left-to-right traversal and right peak as the
    tallest peak on the right-to-left traversal.

    If the left_peak is bigger than right_peak, traverse
    right instead of left. Remember this is because the
    shorter peak is the constraint on the calculation,
    because the shorter peak determines run-off.

    A key thing to remember is that these problems are easy for
    humans because we can see the whole picture and easily 
    fill in the values based upon the constraints. This is why
    I initially did the left to right only traversal, using a 
    stack to keep track of things that I needed to go back and 
    calculate, similar to humans can backtrack to fix a mistake
    once they encounter it.

    Keeping track of all those things was expensive in terms of space and 
    time complexity of redoing calculations and storing more and more data 
    so it was by no means optimal (IDK if this solution is even optimal).
    By going both directions w.r.t traversal, it gave the program
    the whole picture -> the information it needed to calculate the 
    correct solution.

    That way of thinking just got me adding more and more conditions
    to try and make the algorithm work based upon the test cases that
    broke it, but at some point I realized that the the algorithm was 
    flawed. I guess if you see this happening you can try to redo your
    approach. 

    How did I make test cases? Basically I tried different "shapes"
    of the different possible heights, thinking of the whole problem
    as peaks and valleys.
    
    
