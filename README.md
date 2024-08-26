This educational project is implementing a Basic Search Engine with the [PageRank](https://blog.majestic.com/company/understanding-googles-algorithm-how-pagerank-works/) algorithm.

The damping parameter used for calculation the page rank is 0.5.

The input information from the Standard Input includes:

- an integer n specifying how many websites are in the network;
- n strings separated by spaces which are the names of the websites;
- n by n matrix of floats representing a link matrix for the internet;
- a string which is a query for the search, a name of a website to look for.

The result of the program is the top 5 matched websites for the query which are determined by these rules:

- If there is a website that exactly matches the query (including partial match), it should go to the top of the list.
- Other websites are sorted according to the PageRank in descending order.
- In case there is a tie between two websites' PageRanks, a tie should be broken by reverse alphabetical order. (ie., if site "vk" has PageRank = 16.2 and "twitter" also has 16.2, then "vk" should be listed higher)
- If there are fewer than 5 websites on the internet, all of them are returned.

Example 1

Input:
```
5
google facebook vk twitter instagram
0.2 0.0 0.0 0.5 0.5
0.2 1.0 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0
0.2 0.0 0.5 0.0 0.0
0.2 0.0 0.0 0.5 0.5
instagram
```

Output:
```
instagram
facebook
google
vk
twitter
```

Example 2

Input:
```
3
google facebook vk
0 0.333 0
1 0.333 0
0 0.333 1
facebook
```

Output:
```
facebook
vk
google
```
Example 3

Input:
```
6
google facebook vk twitter instagram jetbrains
0.2 0.0 0.0 0.5 0.5 0.0
0.2 1.0 0.0 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0 0.0
0.2 0.0 0.5 0.0 0.0 0.0
0.2 0.0 0.0 0.5 0.5 0.0
0.0 0.0 0.0 0.0 0.0 1.0
jetbrains
```

Output (Note - in this case, twitter wasn't printed because it tied with vk in PageRank, but vk is lower in the alphabet. Only 5 sites can be printed, so twitter doesn't make the cutoff):
```
jetbrains
facebook
instagram
google
vk
``` 
