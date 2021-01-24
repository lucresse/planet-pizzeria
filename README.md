
Question 1 (use problem name “planet”)

Mr. Little Z is on winter vacation, and he has decided to go to the planet Zearth. The only way of traveling through space is by using the aliens' teleportation machines. Mr. Little Z can teleport directly from planet Earth to the planet Zearth, but it is really risky. The aliens haven't perfected their teleportation machine. The greater the distance of traveling the bigger is risk. Because of this, the aliens have built more teleportation stations all throughout space. Teleporting through consecutive teleportation stations lowers the risk. Mr. Little Z wants to go to the planet Zearth using the path where the teleportations are as short as possible - the path where the longest teleportation on it is minimized. Mr. Little Z opened http://www.space-net.spc and found a list of all the space teleportation stations. He decided to use the least risky path, as described above. Help Mr. Little Z find the safest path from Earth to the planet Zearth: the path where the longest distance he has to teleport is minimized. INPUT: The first line of the standard input contains three real numbers, each from the interval [-10000.00, 10000.00], representing the 3D coordinates of the planet Zearth. The next line contains a number N , corresponding to the number of teleportation stations in space (1&lt;= N &lt;=2000). Each of the next N lines contains three real numbers each from the interval [-10000.00, 10000.00], representing the 3D coordinates for each station. Note: The 3D coordinates of Earth are (0.0, 0.0, 0.0). On the planets Earth and Zearth there are teleportation stations, too.  

OUTPUT: To the standard output write one real number to 2 decimal places, representing the maximum distance of the safest path on Mr. Little Z's way to Zearth.  

Input (stdin): 2.00 2.00 2.00 3 0.00 0.00 2.00 0.00 2.00 2.00 2.00 0.00 0.00 
Output (stdout): 2.00 
Additional example: 
Input: 2.00 2.00 2.00 3 1.00 1.00 1.00 1.00 2.00 2.00 2.00 2.00 1.00 
Output: 1.73  

1. Write down your brief thoughts on how you approached this problem. 
3. What is the complexity of your solution? Can it be improved?   

Question 2 (use problem name “pizzeria”)  

After a long deferment, the mayor of Z-city has allowed pizzerias to be opened in town. Pizzerias used to be unlawful because of health reasons (according to the mayor). The city is big, and suddenly there are pizzerias everywhere. We can imagine the city like a matrix with N x N squares, where every square represents one block of the city. Every pizzeria only delivers pizza to the nearby blocks. Specifically, every pizzeria delivers pizza to every block that is at most R blocks away from block the pizzeria's location. Distance is determined by the minimum number of blocks that the delivery guy must take if he is going East/West or North/South (moving diagonally is forbidden in Z-city). For example, let's say that N =5 and a pizzeria is located at the block (3, 3). It can deliver to a 2 block distance at most. The following map shows where the given pizzeria delivers pizzas.  00X00 0XXX0 XXXXX 0XXX0 00X00 Mr. Little Z loves pizza, so he wants to move to the block where he can have the greatest selection of pizzas (the block that has the maximum number of pizzerias delivering to it).  Help Mr. Little Z find that maximum. In other words, if he moves to the block with the greatest selection of pizzas, how many pizzerias will be able to deliver to his block? 

INPUT: The first line of the standard input contains the two numbers N and M , and both numbers are on the interval [1, 10000]. The number N represents the dimension of the city in blocks (the city has N x N blocks). M is the number of pizzerias in the city. The following M lines contain information about each pizzeria, given by the three numbers X, Y , R . The numbers X and Y represent the block where the pizzeria is located, (1 &lt;= X , Y &lt;= N ) and the number R represents the maximum distance that the given pizzeria's delivery guy will travel to deliver pizza (1 &lt;= R &lt;= 100).  

OUTPUT: Write one number to the standard output that represents the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas. 

Input (stdin): 5 2 3 3 2 1 1 2 Output (stdout): 2 

Explanation: The first pizzeria delivers pizzas to the following blocks: 00X00 0XXX0 XXXXX 0XXX0 00X00 and the second one 00000 00000 X0000 XX000 XXX00 So the number of pizzerias that deliver pizzas to each block is: 00100 01110 21111 12110 11200 So the maximum number is 2. 

1. Write down your brief thoughts on how you approached this problem. 
3. What is the complexity of your solution? Can it be improved?
