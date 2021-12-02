// read file
const fs = require("fs").promises;
async function getArray() {
  const data = await fs.readFile("inputs/1.txt", "utf8");
  const numbers = data.split("\n");
  return numbers.map((num) => Number(num));
}

async function question1() {
  const numbers = await getArray();
  return numbers.reduce((total, currentNum, idx, arr) => {
    if (idx === numbers.length - 1) {
      return total;
    }
    const nextNum = arr[idx + 1];
    if (nextNum > currentNum) {
      total++;
    }
    return total;
  }, 0);
}

async function question2() {
  const numbers = await getArray();
  return numbers.reduce((total, currentNum, idx, arr) => {
    if (idx === numbers.length - 3) {
      return total;
    }
    const currentWindow = currentNum + arr[idx + 1] + arr[idx + 2];
    const nextWindow = arr[idx + 1] + arr[idx + 2] + arr[idx + 3];
    if (nextWindow > currentWindow) {
      total++;
    }
    return total;
  }, 0);
}

(async function main() {
  console.log(await question1()); // 1451
  console.log(await question2()); // 1395
})();
