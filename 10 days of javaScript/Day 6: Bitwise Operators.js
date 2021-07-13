'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}


const getMaxLessThanK = (n,k) => {
    
    let m = Number.NEGATIVE_INFINITY ;
    const result = () =>{
        for(let i = 1 ;i<=n;i++){
            for(let j = i+1 ; j<=n ; j++){
                let a = i&j;
                (a > m && a<k)? m = a : m ;
                if( m == k-1 ) return m ;
            }
        }
        return m ;
    }
    return result();
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}
