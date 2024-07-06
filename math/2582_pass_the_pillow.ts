function passThePillow(n: number, time: number): number {

    let place = time % (n-1);
    let rounds = Math.floor(time / (n-1));

    if( rounds%2 ){
        return n-place
    } else {
        return 1+place
    }

};