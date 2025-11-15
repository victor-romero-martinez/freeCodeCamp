// @ts-check

/**
 * @link https://www.freecodecamp.org/espanol/learn/rosetta-code/rosetta-code-challenges/abc-problem
 * @param {string} word
 * @returns {boolean}
 */
function canMakeWord(word) {
  const characters = word.toUpperCase().split("");
  const block = [
    ["B", "O"],
    ["X", "K"],
    ["D", "Q"],
    ["C", "P"],
    ["N", "A"],
    ["G", "T"],
    ["R", "E"],
    ["T", "G"],
    ["Q", "D"],
    ["F", "S"],
    ["J", "W"],
    ["H", "U"],
    ["V", "I"],
    ["A", "N"],
    ["O", "B"],
    ["E", "R"],
    ["F", "S"],
    ["L", "Y"],
    ["P", "C"],
    ["Z", "M"],
  ];

  for (const char of characters) {
    const idx = block.findIndex((b) => b.includes(char));

    if (idx === -1) return false;

    block.splice(idx, 1);
  }

  return true;
}

console.log(canMakeWord("Bark")); //true
console.log(canMakeWord("book")); // false
