function countingSort(arr) {
    // Write your code here
    var n = arr.length;
    let arrValue = new Array(100).fill(0);
    for(var i =0;i<n;i++){
        arrValue[arr[i]]++;
    }
    return arrValue;
}