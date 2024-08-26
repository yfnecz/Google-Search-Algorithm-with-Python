```
Basic search engine

Description
Read the information about the network from the Standard Input in the following format:

an integer n specifying how many websites are in the network;

n strings separated by spaces which are the names of the websites;

n by n matrix of floats representing a link matrix for the internet;

a string which is a query for the search, a name of a website to look for.

The result of the program should be the top 5 matched websites for the query which are determined by these rules:

If there is a website that exactly matches the query (including partial match), it should go to the top of the list.

Other websites are sorted according to the PageRank in descending order.

In case there is a tie between two websites' PageRanks, a tie should be broken by reverse alphabetical order. (ie., if site "vk" has PageRank = 16.2 and "twitter" also has 16.2, then "vk" should be listed higher)

The damping parameter for calculating the page rank should be 0.5. If there are fewer than 5 websites on the internet, you should return as many as there are.

Examples
Example 1

Input:

5
google facebook vk twitter instagram
0.2 0.0 0.0 0.5 0.5
0.2 1.0 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0
0.2 0.0 0.5 0.0 0.0
0.2 0.0 0.0 0.5 0.5
instagram

The rank for the websites will be roughly the following:

google

21.6

facebook

24.3

vk

16.2

twitter

16.2

instagram

21.6

Output:

instagram
facebook
google
vk
twitter

Example 2

Input:

3
google facebook vk
0 0.333 0
1 0.333 0
0 0.333 1
facebook

The rank for the websites will be roughly the following:

google

22.2

facebook

33.3

vk

44.4

Output:

facebook
vk
google

Example 3

Input:

6
google facebook vk twitter instagram jetbrains
0.2 0.0 0.0 0.5 0.5 0.0
0.2 1.0 0.0 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0 0.0
0.2 0.0 0.0 0.5 0.5 0.0
0.0 0.0 0.0 0.0 0.0 1.0
jetbrains

The rank for the websites will be roughly the following:

google

18.0

facebook

20.3

vk

13.5

twitter

13.5

instagram

18.0

jetbrains

16.7


Output (Note - in this case, twitter wasn't printed because it tied with vk in PageRank, but vk is lower in the alphabet. Only 5 sites can be printed, so twitter doesn't make the cutoff):

jetbrains
facebook
instagram
google
vk
``` 
