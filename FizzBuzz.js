/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var arr = [],value = "";
    for(var i = 1;i<=n;i++){
        if(i % 3 ==0 && i % 5 ==0 ){
            arr[i-1] = "Fizz".concat("Buzz");
    }
    else if(i % 5 ==0 ){
        arr[i-1] = "Buzz"
    }
    else if(i % 3 ==0){
        arr[i-1] = "Fizz"
    }
    else{
        arr[i-1] = value.concat(i);
    }
    }
    return arr;
};