var smallerNumbersThanCurrent = function(nums) {
    var arr = [];
    var count;
    for(var i = 0;i<nums.length;i++){
        count = 0;
        for(var j = 0;j<nums.length;j++){
            if(i !== j){
                if(nums[i]>nums[j]){
                    count = count + 1;
                }
            }
        }
        arr[i] = count;
    }
    return arr;
};