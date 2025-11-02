// @ts-check

/**
 * @link https://www.freecodecamp.org/espanol/learn/rosetta-code/rosetta-code-challenges/9-billion-names-of-god-the-integer
 * @param {number} num
 * @returns {number}
 */
function numberOfNamesMemo(num) {
  //   partition(5,5)
  // = partition(5,4) + partition(0,5)
  // = partition(5,4) + 1
  // ...
  // → resultado final = 7

  /** @type {Record<string, number>} */
  const memo = {};

  /**
   * Esto se llama “partition number” en matemáticas.
   * @example p(n, m) = p(n, m-1) + p(n-m, m)
   *
   * @param {number} n
   * @param {number} m
   * @returns {number}
   */
  function permutation(n, m) {
    const key = `${n},${m}`;

    if (key in memo) return memo[key];
    if (n === 0) return 1;
    if (n < 0 || m === 0) return 0;

    const res = permutation(n, m - 1) + permutation(n - m, m);
    memo[key] = res;

    return res;
  }

  return permutation(num, num);
}

/**
 * @param {number} num
 * @returns {number}
 */
function numberOfNamesDynamicPrograming(num) {
  const dp = Array(num + 1).fill(0);
  dp[0] = 1;

  for (let i = 1; i <= num; i++) {
    for (let j = i; j <= num; j++) {
      dp[j] += dp[j - i];
    }
  }

  return dp[num];
}

console.log(numberOfNamesMemo(124)); //2552338241.
console.log(numberOfNamesDynamicPrograming(124)); //2552338241.
