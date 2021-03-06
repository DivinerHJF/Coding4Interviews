# 题目描述

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# 示例

```
输入：head = [1,2,3]
输出：[3,2,1]
```

限制：`0 <= 链表长度 <= 10000`

# 方法一：递归

> 解题思路：先走至链表末端，回溯时依次将节点值加入列表 ，这样就可以实现链表值的倒序输出。

- 算法流程

  - **递推阶段：** 每次传入 `head.next` ，以 `head == None`（即走过链表尾部节点）为递归终止条件，此时返回空列表 `[]`
  - **回溯阶段：** 利用 Python 语言特性，递归回溯时 `当前list + 当前节点值 [head.val]` 进行列表组合，即可实现节点的倒序输出

- 复杂度分析

  - **时间复杂度 O(N)：** O(n)，递归 n 次，时间复杂度为 O(n)，递归函数中的操作时间复杂度为 O(1)，总时间复杂度为 O(n)×O(1) = O(n)
  - **空间复杂度 O(N)：** 系统递归需要使用 O(N) 的栈空间

![递归法](https://pic.leetcode-cn.com/1066f15bd86d99e7998519f4e2ffee070401ec67102f6e3626a61811987d99b5-Picture10.png)

# 方法二：反转

> 解题思路：从头到尾将链表打印到数组中，返回反转后的结果即可。

- 复杂度分析

  - **时间复杂度 O(N)：** O(n)，`reverse()` 的时间复杂度为 O(n)，遍历了一遍数组，复杂度也为 O(n)
  - **空间复杂度 O(N)：** O(n)

# 方法三：堆栈

> 解题思路：链表的特点是只能从前至后访问每个节点，而题目要求倒序输出节点值。这种 “先入后出” 的需求可以借助 “栈” 来实现。

- 算法流程

  - **入栈：** 遍历链表，将各节点值 `push` 入栈。Python​ 使用 `append()` 方法
  - **出栈：** 将各节点值 `pop` 出栈，存储于数组并返回。Python​ 直接返回 `stack` 的倒序列表

- 复杂度分析

  - **时间复杂度 O(N)：** O(n)，push 的时间复杂度为 O(n)，pop 的时间复杂度为 O(n)
  - **空间复杂度 O(N)：** O(n)，使用了额外的 `res` 和 堆栈。

![辅助栈法](https://pic.leetcode-cn.com/e5cb4ba143fd768601c94ee563197b2067e01c1bfe4284049162ec37cfee1b8e-Picture15.png)