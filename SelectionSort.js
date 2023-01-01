unction insertionSort1(n, arr) {
    // Write your code here
    var temp,str = "";
    for(var i = n-1;i>=0;i--){
        for(var j =i-1;j<i;j++){
            if(arr[i]<arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                for(var k = 0;k<n;k++){
                    str = str + arr[k] + " ";
                }
                console.log(str)
                arr[j] = temp;
                str = "";
            }            
            if(arr[j]<temp){
                arr[i] = temp;
                for(var k = 0;k<n;k++){
                    str = str + arr[k] + " ";
                }
                console.log(str)
                str = "";                
            }
        }
    }
}
