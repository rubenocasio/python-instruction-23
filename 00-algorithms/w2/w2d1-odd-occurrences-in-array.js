// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
belongs to a pair (the int is duplicated once)
return the only int that has no matching pair.
*/

const makeFrequencyTable = require('./w2d1-make-frequency-table');

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

/**
 * Given a non-empty array of odd length containing
 * ints where every int but one belongs to a pair
 * (the int is duplicated once), returns the only
 * lonely int.
 * @param {Number[]} nums
 * @returns {Number}
 */
function oddOccurrencesInArray(nums) {
    //Logic goes here
}

console.log(oddOccurrencesInArray(nums1), 'should equal', expected1);
console.log(oddOccurrencesInArray(nums2), 'should equal', expected2);
console.log(oddOccurrencesInArray(nums3), 'should equal', expected3);
console.log(oddOccurrencesInArray(nums4), 'should equal', expected4);
