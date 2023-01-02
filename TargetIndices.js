var targetIndices = function(nums, target) {
    var arr = [];
    var a = 0;
    for(var k = 1;k<=nums.length;k++){
                for(var j =0;j<k; j++){
                   if(nums[k]<nums[j]){
                        var temp = nums[k];
                        nums[k]  = nums[j];
                        nums[j] = temp;
                    }                    
                }

 }
 for(var i = 0;i<nums.length;i++){
     if(nums[i] == target){
         arr[a++] = i;
     }
 }
 return arr;
};