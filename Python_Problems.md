# Python Problems

This will be a list of problems that people can work on. I'll try to order them from basic to advanced.

### Problems

1. Given an amount of money, determine the minimum number of bills and coins needed to make up that amount.
1. Make your own square root function.
1. Read a grid of numbers from a text file and rotate the grid 90º each way.
1. Read and solve a maze from a text file (made of # for walls, S for Start, E for Exit and . for the floor)

And of course, all the problems at https://projecteuler.net/archives

Another good set of problems is located at https://cs50.harvard.edu/2018/fall/psets/1/
 - change the /1/ at the end to /2/, /3/ and /4/ for more problem sets. They were designed for the C programming language,
 but Python should work just fine for most of it. The problem at /1/ is pretty basic.

### Suggestions

If you have any questions about them, edit this document and add a new line with `    * question.` and I'll answer.
(4 spaces before the * if you want it to look beautiful.)
Or just send me a message.

When doing these problems or any assignment for the purpose of learning,
I think it's good to plan out your solution before jumping into it.
Make a plan for what functions and subroutines you think you'll need.
What types of variables will you need and will you need to make any special variable classes.

Example: If you were going to make a program that analyzed the trajectory of a ball, you might do something like this:
* I'll need to get the initial conditions of the ball.
* I'll need a container to conveniently hold and move around that data (x, y, v<sub>x</sub>, v<sub>y</sub>, and maybe time).
* Next I'll need some functions to analyze the trajectory (i = initial conditions. It will use the container object mentioned above).
  * `maxHeight(i)`
  * `halfMaxHeight(i)`
  * `timeAloft(i)`
  * `maxDistance(i)`
  * `distanceAt(i,t)`
  * `heightAt(i,t)`
  * Maybe a few more once you get coding.
* Next it's good to think about how these functions will pass around data.
  * In this case it's pretty simple and self explanatory. But other problems might be more complicated.
    * As a general rule, I avoid using print() in any function that isn't named "printXYZ()". That way the program runs silently unless those print functions are included.
    * In this example, I could make another object/class that holds all the answers and that could get passed around and populated.
      * Actually, if this was made into a class, then it would store all of its values in the class automatically and... that would be a neat way to organize the data.
* Then make sure you've met all your requirements and start coding and testing.
  * I like to fully code and test each function as I go, if possible.
  * Sometimes functions will hold other functions and this isn't possible using real data, but you can use placeholder values in the meantime.
