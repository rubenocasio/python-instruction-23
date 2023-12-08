/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Is there a quick way to determine if they aren't an anagram before spending more time?

  Given two strings
  return whether or not they are anagrams
*/

const strA1 = 'yes';
const strB1 = 'eys';
const expected1 = true;

const strA2 = 'yes';
const strB2 = 'eYs';
const expected2 = true;

const strA3 = 'no';
const strB3 = 'noo';
const expected3 = false;

const strA4 = 'silent';
const strB4 = 'listen';
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
  if(s1.length !== s2.length){
    return false
  }
  const charCount = {}
  //Converts all the alphabetic characters in a string to lowercase.
  s1 = s1.toLowerCase()
  s2 = s2.toLowerCase()

  for(const char of s1){
    // console.log(char)
    charCount[char] = (charCount[char] || 0 ) +1
  }

  for(const char of s2){
    if(!charCount[char]){
      return false
    }
    charCount[char]--
    // console.log(charCount[char])
  }
  //Object that contains the properties and methods. 
  //.every - Determines whether all the members of an array satisfy the specified test.
  return Object.values(charCount).every(whatever => whatever === 0)
}

console.log(isAnagram(strA1, strB1), 'should equal', expected1);
console.log(isAnagram(strA2, strB2), 'should equal', expected2);
console.log(isAnagram(strA3, strB3), 'should equal', expected3);
console.log(isAnagram(strA4, strB4), 'should equal', expected4);
