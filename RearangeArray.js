var rearrangeArray = function(nums) {
    var flag = 0,count = 0;
        for(var j = 1;j<=nums.length;){
            if(j == nums.length && flag < nums.length){
                j=1;
                flag = 0;
                count++;
                if(count == 3){
                    break;
                }
            }
            else{
                if(nums[j-1]+nums[j+1] == nums[j]*2){
                var temp =  nums[j-1];
                    nums[j-1] = nums[j];
                    nums[j] = temp;
                    
                    j++;


            }
            else{
                j++; 

                flag++;
            }
            }
        }
    return nums;
};