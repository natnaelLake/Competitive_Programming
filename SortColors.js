/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(var i = 0;i<nums.length-1;i++){
         var min = i;
         for(var j = i+1;j<nums.length;j++){
             if(nums[j]<=nums[min]){
                 min = j;
             }
         }
         if(min != i){
             var temp = nums[i];
             nums[i] = nums[min];
             nums[min] = temp;
         }
    }
    return nums;
 };