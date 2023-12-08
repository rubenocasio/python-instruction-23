/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = '   hello world     ';
const expected1 = 'hello world';

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
  let start = 0
  let end = str.length - 1
  
  //Loop to move the start pointer past any false values
  while (str[start] == false){
    start++
  }
  //Loop to move the end pointer past any false values
  while (str[end] == false){
    end--
  }
  //.slice The index to the beginning of the specified portion of stringObj. Returns a section of a string.
  //The index to the end of the specified portion of stringObj.
  //The substring includes the characters up to, but not including,
  //the character indicated by end. If this value is not specified,
  //the substring continues to the end of stringObj.
  // console.log(str)
  return str.slice(start, end + 1)
}

console.log(trim(str1));
