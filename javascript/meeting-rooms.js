let n = 2;
let arr = [
   [0, 10],
   [1, 5],
   [2, 7],
   [3, 4],
];

arr.sort((a, b) => a[0] - b[0]);
let rooms = new Array(n).fill(0);
let countRooms = new Array(n).fill(0);

for (var [start, end] of arr) {
   let index = rooms.findIndex((value) => value <= start);

   // Get the room whose meeting will end soonest
   if (index < 0) {
      index = rooms.indexOf(Math.min(...rooms));
   }

   countRooms[index]++;
   let lastEndTime = rooms[index];
   let endTime = start < lastEndTime ? lastEndTime - start + end : end;
   rooms[index] = endTime;
}

return countRooms.indexOf(Math.max(...countRooms));
