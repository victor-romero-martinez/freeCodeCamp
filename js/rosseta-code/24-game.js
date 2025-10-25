// @ts-check

/**
 * @param {Array<string>} str
 * @returns {Array<Array<string>>}
 */
function getPermutations(str) {
  if (str.length === 1) return [str];

  /** @type {Array<Array<string>>} */
  const result = [];

  for (let i = 0; i < str.length; i++) {
    const rest = str.slice(0, i).concat(str.slice(i + 1));
    const perms = getPermutations(rest);
    for (const p of perms) result.push([str[i], ...p]);
  }

  return result;
}

/**
 * @param {Array<string>} ops
 * @returns {Array<Array<string>>}
 */
function getCombineOps(ops) {
  const combs = [];

  for (const op1 of ops) {
    for (const op2 of ops) {
      for (const op3 of ops) {
        combs.push([op1, op2, op3]);
      }
    }
  }

  return combs;
}

/**
 * @param {Array<Array<string>>} permute
 * @param {Array<Array<string>>} combine
 * @returns {Array<string>}
 */
function buldExpressions(permute, combine) {
  const expressions = [];

  for (const nums of permute) {
    const [a, b, c, d] = nums;

    for (const ops of combine) {
      const [op1, op2, op3] = ops;

      // 1. (((a op1 b) op2 c) op3 d)
      expressions.push(`(((${a}${op1}${b})${op2}${c})${op3}${d})`);
      // 2. ((a op1 b) op2 (c op3 d))
      expressions.push(`((${a}${op1}${b})${op2}(${c}${op3}${d}))`);
      // 3. (a op1 (b op2 (c op3 d))
      expressions.push(`(${a}${op1}(${b}${op2}(${c}${op3}${d}))`);
      // 4. (((a op1 b) op2 c) op3 d) same structure diferrent ops
      expressions.push(`(((${a}${op1}${b})${op2}${c})${op3}${d})`);
      // 5. (a op1 ((b op2 c) op3 d))
      expressions.push(`(${a}${op1}((${b}${op2}${c})${op3}${d}))`);
    }
  }

  return expressions;
}

/**
 * @param {string} expr
 * @returns {number|null}
 */
function evalExpression(expr) {
  try {
    const result = new Function(`return ${expr};`)();

    if (!isFinite(result)) return null;

    return result;
  } catch (error) {
    return null;
  }
}

/**
 * El Juego 24 pone a prueba la aritmética mental de una persona.
 * El objetivo del juego es organizar cuatro números de manera que, al evaluarlos, el resultado sea 24.
 *
 * @link {https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/24-game}
 * @param {string} numStr
 * @returns {string}
 */
function solve24(numStr) {
  const nums = numStr.split("");
  const ops = ["*", "+", "-", "/"];
  const permute = getPermutations(nums);
  const combineOps = getCombineOps(ops);
  const expressions = buldExpressions(permute, combineOps);

  const TARGET = 24;
  const EPSILON = 1e-6;

  for (const expr of expressions) {
    const result = evalExpression(expr);

    if (result) {
      if (Math.abs(result - TARGET) < EPSILON) {
        return expr.replace(/^\((.*)\)$/, "$1");
      }
    }
  }

  return "Solution not found!.";
}

console.log(solve24("4878")); // (8-8/8)*4
