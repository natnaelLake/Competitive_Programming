var sortSentence = function(s) {
    var arr = s.split(' ');
    var allStr  = [];
    var str = [];
    var str1 = ''

    for(var i = 0;i<arr.length;i++){
        str[i] = arr[i].slice(-1);
        allStr[i] = arr[i].slice(0,-1);
        
    }
            for(var k = 1;k<=arr.length;k++){
                str1 = '';
                for(var j =0;j<k; j++){
                   if(str[k]<str[j]){
                       var temp1 = str[k];
                        str[k]  = str[j];
                        str[j] = temp1;
                        var temp = allStr[k];
                        allStr[k]  = allStr[j];
                        allStr[j] = temp;
                    }
                        str1  = str1 + allStr[j] + ' ';                      
                }

 }
 str1 = str1.trim();  
return str1;   
};