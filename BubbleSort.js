function countSwaps(a) {
    // Write your code here
    var firstElement,lastElement,numSwaps = 0;
    for( var i = 0;i<a.length;i++){
        for( var j = 0;j<a.length-1-i;j++){
            if(a[j]>a[j+1]){
            var temp = a[j];
                a[j] = a[j + 1];
                a[j+1] = temp;
                numSwaps++;
            }
        }
    }
        firstElement = a[0];
        lastElement = a[a.length-1];
    console.log(`Array is sorted in ${numSwaps} swaps.`);
    console.log(`First Element: ${firstElement}`);
    console.log(`Last Element: ${lastElement}`)    
}
