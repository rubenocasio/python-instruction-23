/* 
   Decodes the given string by duplicating each character by the following int
   amount if there is an int after the character. 
*/

const str1 = 'a3b2c1d3';
const expected1 = 'aaabbcddd';

const str2 = 'a3b2c12d10';
const expected2 = 'aaabbccccccccccccdddddddddd';

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
  //Initialize an empty string to hold our decoded results
  let decoded = '';

  //Create a variable to keep track of the current char that is being processed
  let currentChar = '';

  for(let char = 0; char < str.length; char++){
    //Initialize an empty string to build a number string
    let digits = '';
    
    //Check if the current char is not a number
    if(isNaN(str[char])){
      
      //Set the current char
      currentChar = str[char];
      // console.log(currentChar)
      
      //Move to the next char
      char++
      
      //Loop through digits after the current char
      while(!isNaN(str[char])){
        //Append the digit to the digits string
        digits += str[char]
        // console.log(digits)
        
        //move to the next char
        char++
      }
    }
    
    for (let i = 1; i <= parseInt(digits); i++){
      decoded += currentChar
    }
    char--
  }

  //return our empty string
  return decoded
}

result1 = decodeStr(str1);
console.log(result1);

result2 = decodeStr(str2);
console.log(result2);
