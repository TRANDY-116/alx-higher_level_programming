#!/usr/bin/node

const biggestInt = process.argv.slice(2).map(Number);

function SecondLargestInt (x) {
	  if (x.length <= 1) {
		      return 0;
		    }

	  let largestNum = Math.max(x[0], x[1]);
	  let secondLargest = Math.min(x[0], x[1]);

	  for (let i = 2; i < x.length; i++) {
		      if (x[i] > largestNum) {
			            secondLargest = largestNum;
			            largestNum = x[i];
			          } else if (x[i] > secondLargest && x[i] !== largestNum) {
					        secondLargest = x[i];
					      }
		    }
	  return secondLargest;
}
console.log(SecondLargestInt(biggestInt));
