import numpy as np
import numpy.linalg as la


class PageRank:
    def __init__(self):
        self.dim = int(input())
        self.d = 0.5  # d is Damping Factor
        self.websites = input().split()
        my_list = []
        for _ in range(self.dim):
            my_list.append([float(x) for x in input().split()])
        self.L = np.array(my_list)  # L is undamped matrix
        self.query = input()
        self.page_rank = None

    def calculate_r_vector(self):
        J = np.ones((self.dim, self.dim))  # and J is a matrix where every element is 1
        M = self.d * self.L + (1 - self.d) / self.dim * J  # M is a new matrix that adds the probability of a random visit to a page that the current page doesn’t contain links to
        r_0 = 100 * np.ones(self.dim) / self.dim
        r_1 = np.matmul(M, r_0)
        while la.norm(r_1 - r_0) > 0.009:  # Apply the iteration method so that the difference between the r_i and r_i+1 is less or equal to 0.01
            r_0 = r_1
            r_1 = np.matmul(M, r_0)
        self.page_rank = r_1

    def search(self):
        match, match_site = None, None
        for i, site in enumerate(self.websites):
            if self.query in site:
                match = i
                match_site = site
                self.websites.remove(site)
                break
        if match is not None:
            self.page_rank = np.delete(self.page_rank, match)  # the matched site will be printed first
            print(match_site)
        my_dict = sorted(({self.websites[i]:self.page_rank[i] for i in range(len(self.websites))}).items(), reverse=True)
        my_dict = sorted(my_dict, key=lambda v:v[1], reverse=True)
        number_results = 5 - 1 * (match is not None) if 5 - 1 * (match is not None) < len(my_dict) else len(my_dict)
        for i in range(number_results):
            print(my_dict[i][0])


if __name__ =='__main__':
    p = PageRank()
    p.calculate_r_vector()
    p.search()
