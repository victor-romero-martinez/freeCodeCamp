// @ts-check

/**
 * Verifica si un número es palíndromo
 * @param {number} n
 * @returns {boolean}
 */
function isPalindrome(n) {
  return String(n) === String(n).split("").reverse().join("");
}

/**
 * Encuentra el mayor palíndromo producto de dos números de n dígitos
 * @param {number} n
 * @returns {number}
 */
function largestPalindromeProduct(n) {
  let maxPalindrome = 0;
  const min = Math.pow(10, n - 1);
  const max = Math.pow(10, n) - 1;

  for (let i = max; i >= min; i--) {
    for (let j = i; j >= min; j--) {
      const product = i * j;
      if (product <= maxPalindrome) break; // No puede ser mayor
      if (isPalindrome(product)) {
        maxPalindrome = product;
      }
    }
  }
  return maxPalindrome;
}

console.log(largestPalindromeProduct(3)); // 906609
