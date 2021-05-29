"""
    public int numberOfPatterns(int m, int n) {
        // Skip array represents number to skip between two pairs
        int skip[][] = new int[10][10];
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        boolean vis[] = new boolean[10];
        int rst = 0;
        // DFS search each length from m to n
        for(int i = m; i <= n; ++i) {
            rst += DFS(vis, skip, 1, i - 1) * 4;    // 1, 3, 7, 9 are symmetric
            rst += DFS(vis, skip, 2, i - 1) * 4;    // 2, 4, 6, 8 are symmetric
            rst += DFS(vis, skip, 5, i - 1);        // 5
        }
        return rst;
    }
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0 for _ in range(10)] for _ in range(10)]
        skip[1][3] = skip[3][1] = 2 
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6 
        skip[7][9] = skip[9][7] = 8 
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5 
        
        visited = [False] * 10 
        
        result = 0 
        
        for i in range(m, n+1):
            
            result += self.backtrack(skip, visited, 1, i-1) * 4     # because 1, 3, 7, 9 are all same 
            result += self.backtrack(skip, visited, 2, i-1) * 4     # because 2, 4, 8, 6 are all same 
            result += self.backtrack(skip, visited, 5, i-1)         # only 5 is unique
        
        return result 
    
    def backtrack(self, skip, visited, curr, remaining):
        # base case
        if remaining < 0:
            return 0 
        if remaining == 0:
            return 1
        
        # logic 
        # 1) action
        visited[curr] = True 
        result = 0 
        
        # 2) recurse
        for i in range(1, 9+1):
            if visited[i] == False and (skip[curr][i] == 0 or visited[skip[curr][i]] == True):
                result += self.backtrack(skip, visited, i, remaining - 1)
        
        # 3) backtrack
        visited[curr] = False 
        
        return result
        
"""
    int DFS(boolean vis[], int[][] skip, int cur, int remain) {
        if(remain < 0) return 0;
        if(remain == 0) return 1;
        vis[cur] = true;
        int rst = 0;
        for(int i = 1; i <= 9; ++i) {
            // If vis[i] is not visited and (two numbers are adjacent or skip number is already visited)
            if(!vis[i] && (skip[cur][i] == 0 || (vis[skip[cur][i]]))) {
                rst += DFS(vis, skip, i, remain - 1);
            }
        }
        vis[cur] = false;
        return rst;
    }
    
    
}
"""