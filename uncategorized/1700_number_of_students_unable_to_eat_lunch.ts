function countStudents(students: number[], sandwiches: number[]): number {

    let squ = students.reduce((a,b) => a+b);
    let cir = students.length - squ;

    for(let [i,v] of sandwiches.entries()){
        if(v === 1){
            squ -=1;
        } else {
            cir -= 1;
        }
        if(squ<0 || cir<0){
            return sandwiches.length - i;
        }
    }

    return 0;
};