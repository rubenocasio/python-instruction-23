/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

const cents5 = 93;
const expected5 = { quarter: 3, dime: 1, nickel: 1, penny: 3 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
  const coins = {}

  if(cents >= 25){
    //Returns the greatest integer less than or equal to its numeric argument.
    coins.quarter = Math.floor(cents / 25) //1
    cents -= coins.quarter * 25;
  }

  if(cents >= 10){
    //Returns the greatest integer less than or equal to its numeric argument.
    coins.dime = Math.floor(cents / 10) //1
    cents -= coins.dime * 10;
  }

  if(cents >= 5){
    //Returns the greatest integer less than or equal to its numeric argument.
    coins.nickel = Math.floor(cents / 5) //1
    cents -= coins.nickel * 5;
  }
  
  if(cents >= 1){
    //Returns the greatest integer less than or equal to its numeric argument.
    coins.penny = Math.floor(cents / 1) //1
    cents -= coins.penny * cents;
  }
  return coins
}

console.log(fewestCoinChange(cents1), 'should equal:', expected1);
console.log(fewestCoinChange(cents2), 'should equal:', expected2);
console.log(fewestCoinChange(cents3), 'should equal:', expected3);
console.log(fewestCoinChange(cents4), 'should equal:', expected4);
console.log(fewestCoinChange(cents5), 'should equal:', expected5);
