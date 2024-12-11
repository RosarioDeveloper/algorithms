/**
 * Transpose Matrix
    You're given a 2D array of integers <span>matrix</span>. Write a function
    that returns the transpose of the matrix.

    The transpose of a matrix is a flipped version of the original matrix across
    its main diagonal (which runs from top-left to bottom-right); it switches
    the row and column indices of the original matrix.

    You can assume the input matrix always has at least 1 value; however its
    width and height are not necessarily the same.
 */

function transposeMatrix(matrix) {
   let res = [];
   for (var arr of matrix) {
      for (var i = 0; i < arr.length; i++) {
         if (!res[i]) {
            res[i] = [arr[i]];
         } else {
            res[i].push(arr[i]);
         }
      }
   }

   return res;
}

const result = transposeMatrix([
   [0, 4, 2, 42],
   [-1, 5, 3, 100],
   [-2, 6, -2, 30],
   [-3, 7, -3, -42],
]);

console.log(result);
