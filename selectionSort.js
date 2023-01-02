function selectionSort(arr,n){
    //code here
    var str = '';
    for(var i = 1;i<=n;i++){
        str = '';
        for(var j=0;j<i;j++){
            if(arr[i]<arr[j]){
                var temp = arr[i];
                arr[i]  = arr[j];
                arr[j] = temp;
            }
            str  = str + arr[j] + ' ';
        }
   
    }
 
   }