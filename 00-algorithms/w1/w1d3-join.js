/* 
  Given an arr and a separator string, output a string of every item
  in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ', ';
const expected1 = '1, 2, 3';

const arr2 = [1, 2, 3];
const separator2 = '-';
const expected2 = '1-2-3';

const arr3 = [1, 2, 3];
const separator3 = ' - ';
const expected3 = '1 - 2 - 3';

const arr4 = [1];
const separator4 = ', ';
const expected4 = '1';

const arr5 = [];
const separator5 = ', ';
const expected5 = '';

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
  //Create an empty bucket/container (string) to hold the results
  let resultStr = '';

  //Iterate over each element in the array
  for (let i = 0; i < arr.length; i++) {

    //Append the current array element to our string results
    // console.log(i)
    // console.log(arr[i])
    resultStr += arr[i]
    // resultStr = resultStr += arr[i]

    //Check if the current element is not the last one in the array.
    if (i < arr.length - 1) {
      //Append the seperator to the result string
      resultStr += separator;
    }
  }
  //Return our bucket (string)
  // console.log(resultStr)
  return resultStr;
}

const result1 = join(arr1, separator1);
console.log(result1);

const result2 = join(arr2, separator2);
console.log(result2);

const result3 = join(arr3, separator3);
console.log(result3);

const result4 = join(arr4, separator4);
console.log(result4);

const result5 = join(arr5, separator5);
console.log(result5);