/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.

  Ok to use a new array

  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
function dedupeSorted(nums) {
  const deduped = []

  for(let i = 0; i < nums.length; i++){
    // if(nums[i] !== nums[i-1])
    if(nums[i] !== nums[i - 1]){
      deduped.push(nums[i])
    }
  }
  return deduped
}

console.log(dedupeSorted(nums1), 'should equal', expected1);
console.log(dedupeSorted(nums2));
console.log(dedupeSorted(nums3));
console.log(dedupeSorted(nums4));

function dedupeSortedInPlace(nums) {
  // 'j' is used as an index to place unique elements in the array.
  let j = 0;

  // Iterate through each element in the array.
  for (let i = 0; i < nums.length; i++) {
      // Check if it's the first element or if it's different from the previous element.
      if (i === 0 || nums[i] !== nums[i - 1]) {
          // If it's the first element or a unique element, place it at index 'j' and increment 'j'.
          nums[j++] = nums[i];
      }
  }

  // After the loop, 'j' is the new length of the array without duplicates.
  // Resize the array to remove the duplicates that have been shifted to the end.
  nums.length = j;

  // Return the modified array, which now has only unique elements and no duplicates.
  return nums;
}

console.log(dedupeSortedInPlace(nums1), 'should equal', expected1);
console.log(dedupeSortedInPlace(nums2), 'should equal', expected2);
console.log(dedupeSortedInPlace(nums3), 'should equal', expected3);
console.log(dedupeSortedInPlace(nums4), 'should equal', expected4);
