/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is the same forwards and backwards
  
  Do not ignore spaces, punctuation or capitalization
 */

const str1 = 'a x a';
const expected1 = true;

const str2 = 'racecar';
const expected2 = true;

const str3 = 'Dud';
const expected3 = false;

const str4 = 'oho!';
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
  //For loop to loop over the string thats passed into the function
  for(let i = 0; i < Math.floor(str.length / 2); i++){
    //Compare strings from left side to right
    if(str[i] !== str[str.length -1 - i]){
      // console.log(str[i])
      //if there is mismatch is found return false
      return false
    }
  }
  return true

}
console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))


/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,

return whether or not there is at least 6 feet separating every person.

Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected5 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected6 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected7 = true;

const queue4 = [];
const expected8 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {}