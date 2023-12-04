/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ['a', 'a', 'a'];
const expected1 = { a: 3};

const arr2 = ['a', 'b', 'a', 'c', 'B', 'c', 'c', 'd'];
const expected2 = {a: 2, b: 1, c: 3, B: 1, d: 1,};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {
  // Create an empty object to store frequency of each element.
  const freqTable = {};

  // Iterate over each element in the array.
  for (const elem of arr) {
      // Check if the element is not already a key in the freqTable.
      if (!freqTable.hasOwnProperty(elem)) {
          // If the element is not in the freqTable, add it with a count of 1.
          freqTable[elem] = 0;
      } else {
          // If the element already exists in the table, increment its count.
          freqTable[elem] += 1;
      }
  }

  // Return the completed frequency table.
  return freqTable;
}

const result1 = makeFrequencyTable(arr1);
console.log(result1);

const result2 = makeFrequencyTable(arr2);
console.log(result2);

const result3 = makeFrequencyTable(arr3);
console.log(result3);

module.exports = makeFrequencyTable;
