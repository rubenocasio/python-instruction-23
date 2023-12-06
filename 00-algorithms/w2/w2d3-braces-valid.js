/* 
Braces Valid

Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = 'W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!';
const expected1 = true;

const str2 = 'D(i{a}l[ t]o)n{e';
const expected2 = false;

const str3 = 'A(1)s[O (n]0{t) 0}k';
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
  //Keep track of opening braces
  const stack = []
  const openersToClosers = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
  }
  for (const char of str){
    // console.log(char)
    //Determines whether an object has a property with the specified name.
    if(openersToClosers.hasOwnProperty(char)){
      stack.push(char)
      // console.log(char)
    }
    //.includes - Determines whether an array includes a certain element, returning true or false as appropriate.
    else if (Object.values(openersToClosers).includes(char)){
      //.pop - Removes the last element from an array and returns it. If the array is empty,
      //undefined is returned and the array is not modified.
      if(stack.length === 0 || openersToClosers[stack.pop()] !== char){
        return false
      }
    }
  }

  return stack.length === 0
}

console.log(bracesValid(str1), 'should equal', expected1);
console.log(bracesValid(str2), 'should equal', expected2);
console.log(bracesValid(str3), 'should equal', expected3);
