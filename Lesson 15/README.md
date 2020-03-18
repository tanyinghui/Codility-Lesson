## Count Traingles

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
```
A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
```
For example, consider array A such that:
```
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
```
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

```python
def solution(A)
```

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:
```
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
```
the function should return 4, as explained above.

Write an **efficient** algorithm for the following assumptions:

* N is an integer within the range [0..1,000];
* each element of array A is an integer within the range [1..1,000,000,000].

## Abs Distinct
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:
```
  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
```
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

```python
def solution(A)
```

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:
```
  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
```
the function should return 5, as explained above.

Write an **efficient** algorithm for the following assumptions:

* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.