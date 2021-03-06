<h2>1263. Minimum Moves to Move a Box to Their Target Location</h2><h3>Hard</h3><hr><div><p>Storekeeper is a&nbsp;game&nbsp;in which the player pushes boxes around in a warehouse&nbsp;trying to get them to target locations.</p>

<p>The game is represented by a <code>grid</code> of size&nbsp;<code>m x n</code>, where each element is a wall, floor, or a box.</p>

<p>Your task is move the box <code>'B'</code> to the target position <code>'T'</code> under the following rules:</p>

<ul>
	<li>Player is represented by character <code>'S'</code>&nbsp;and&nbsp;can move up, down, left, right in the <code>grid</code> if it is a floor (empy cell).</li>
	<li>Floor is represented by character <code>'.'</code> that means free cell to walk.</li>
	<li>Wall is represented by character <code>'#'</code> that means obstacle&nbsp;&nbsp;(impossible to walk there).&nbsp;</li>
	<li>There is only one box <code>'B'</code> and one&nbsp;target cell <code>'T'</code> in the <code>grid</code>.</li>
	<li>The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a <strong>push</strong>.</li>
	<li>The player cannot walk through the box.</li>
</ul>

<p>Return the minimum number of <strong>pushes</strong> to move the box to the target. If there is no way to reach the target, return&nbsp;<code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/sample_1_1620.png" style="width: 520px; height: 386px;"></strong></p>

<pre><strong>Input:</strong> grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
&nbsp;              ["#",".",".","B",".","#"],
&nbsp;              ["#",".","#","#",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>We return only the number of times the box is pushed.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
&nbsp;              ["#",".",".","B",".","#"],
&nbsp;              ["#","#","#","#",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> -1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> grid = [["#","#","#","#","#","#"],
&nbsp;              ["#","T",".",".","#","#"],
&nbsp;              ["#",".","#","B",".","#"],
&nbsp;              ["#",".",".",".",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> 5
<strong>Explanation:</strong>  push the box down, left, left, up and up.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> grid = [["#","#","#","#","#","#","#"],
&nbsp;              ["#","S","#",".","B","T","#"],
&nbsp;              ["#","#","#","#","#","#","#"]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;grid.length</code></li>
	<li><code>n ==&nbsp;grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 20</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>grid</code> contains only characters&nbsp;<code>'.'</code>, <code>'#'</code>,&nbsp; <code>'S'</code> , <code>'T'</code>,&nbsp;or <code>'B'</code>.</li>
	<li>There is only one character&nbsp;<code>'S'</code>, <code>'B'</code>&nbsp;<font face="sans-serif, Arial, Verdana, Trebuchet MS">and&nbsp;</font><code>'T'</code>&nbsp;in the <code>grid</code>.</li>
</ul>
</div>