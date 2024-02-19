/**
 *    You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
 */

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
