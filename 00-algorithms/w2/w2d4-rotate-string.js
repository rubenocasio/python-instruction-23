/* 
  String: Rotate String

  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = 'Hello World';

const rotateAmnt1 = 0;
const expected1 = 'Hello World';

const rotateAmnt2 = 1;
const expected2 = 'dHello Worl';

const rotateAmnt3 = 2;
const expected3 = 'ldHello Wor';

const rotateAmnt4 = 4;
const expected4 = 'orldHello W';

const rotateAmnt5 = 13;
const expected5 = 'ldHello Wor';
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) {
  amnt = amnt % str.length;
  // console.log("This is amnt", amnt)
  
  if(amnt < 0) {
    amnt += str.length
    // console.log("This is my if amnt", amnt)
  }
  // ..slice: Returns a section of a string. The index to the beginning of the specified portion of stringObj.
  let part1 = str.slice(0, str.length - amnt)
  let part2 = str.slice(str.length - amnt)
  // console.log("This is part1 slice", part1)
  // console.log("This is part2 slice", part2)
  // return part1 + part2
  return part2 + part1
}

console.log(rotateStr(str, rotateAmnt1), 'should equal', expected1);
console.log(rotateStr(str, rotateAmnt2), 'should equal', expected2);
console.log(rotateStr(str, rotateAmnt3), 'should equal', expected3);
console.log(rotateStr(str, rotateAmnt4), 'should equal', expected4);
console.log(rotateStr(str, rotateAmnt5), 'should equal', expected5);
